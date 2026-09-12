from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def test_the_skill_is_fetched_not_vendored() -> None:
    assert not (ROOT / "skills" / "lieflat-charts").exists()


def test_readme_sync_check_still_passes() -> None:
    result = subprocess.run(
        ["bash", str(ROOT / "scripts" / "check-readme-sync.sh")],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


# --- behavioural checks against a local fixture repo -------------------------------------
