#!/usr/bin/env python3
"""Check a selected stdio MCP initialize handshake without registering the server."""
import argparse
import json
import os
import queue
import signal
import subprocess
import sys
import threading
import time


def check(command, timeout):
    options = {"start_new_session": True} if os.name != "nt" else {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP}
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.DEVNULL, text=True, bufsize=1, **options)
    messages = queue.Queue()

    def read():
        for line in process.stdout:
            messages.put(line)
        messages.put(None)

    threading.Thread(target=read, daemon=True).start()
    request = {"jsonrpc": "2.0", "id": 1, "method": "initialize",
               "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                          "clientInfo": {"name": "agent-config-check", "version": "1.0"}}}
    try:
        process.stdin.write(json.dumps(request) + "\n")
        process.stdin.flush()
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            try:
                line = messages.get(timeout=max(0.01, deadline - time.monotonic()))
            except queue.Empty:
                break
            if line is None:
                raise ValueError("Server exited before initialize completed")
            try:
                response = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(response, dict) or response.get("id") != 1:
                continue
            result = response.get("result", {})
            if "error" in response or not isinstance(result, dict) or not result.get("serverInfo") or not result.get("protocolVersion"):
                raise ValueError("Server rejected initialize or returned an incomplete response")
            process.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n")
            process.stdin.flush()
            return {"status": "initialize-passed", "server": result["serverInfo"]}
        raise ValueError(f"Initialize did not complete within {timeout} seconds")
    finally:
        if os.name == "nt":
            subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
        else:
            try:
                os.killpg(process.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            if os.name == "nt":
                process.kill()
            else:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            process.wait(timeout=5)
        process.stdin.close()
        process.stdout.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("Pass the server command after --")
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    try:
        print(json.dumps(check(command, args.timeout)))
    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
