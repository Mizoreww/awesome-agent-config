# Clear, Precise Writing

Apply these rules in the user's language. The tables provide editing examples; use the replacement wording while preserving the facts.

## 1. Use standard terminology

Use established terms for concepts that already have conventional names. Do not invent alternative labels.

| Original wording | Replacement |
| --- | --- |
| Overlength / whether it is overlength | Truncation / whether the length limit is reached |
| Ray's port collides with itself | Ray instances from multiple tasks compete for the same port |
| Arm | Approach |
| Look only at the length line | Length-heuristic baseline |
| Farming rewards | The reward is optimized without improvement in evaluation metrics |
| Archive | Checkpoint |

## 2. Avoid metaphors

If readers must infer what a phrase refers to, name the subject or mechanism directly. Do not introduce metaphors as technical terms.

| Original wording | Replacement |
| --- | --- |
| Pedigree | Base-model origin |
| Eight different pedigrees | Models based on eight different base models |
| That is a size difference, not a pedigree difference | The original range comprised Qwen 14B, 32B, and 72B; the difference comes from parameter count |
| Already ate up half the space | Already covers half the interval |
| Turned into a retriever that recognizes questions | Degraded to question recognition, unrelated to learning value |
| The selected questions look much healthier | The selected questions have a lower truncation rate |
| The error range still covers the baseline | The confidence interval overlaps the baseline |

## 3. Use neutral headers, categories, and status labels

Use neutral nouns such as Problem, Observation, Impact, and Result for table headers and category names.

| Original wording | Replacement |
| --- | --- |
| Pitfalls / costs and lessons | Problems / impact |
| How sure we are | Degree of confirmation |
| How it was done | Experimental setup |
| How much still overlaps after picking again | Overlap rate after resampling |
| How many different values there are | Number of distinct values |
| Still running | In progress |
| A switch that must be turned off | Filter to disable |

Keep status labels consistent across sections. If earlier sections use Completed, Confirmed, Below baseline, and Conclusion pending, continue using the appropriate labels for the actual status. Replace later labels such as Got it working, Unexpected discovery, Needs fixing, and Did not get what we paid for with the corresponding neutral labels.

## 4. Avoid "X, not Y" framing

State the finding, measured difference, or relationship directly. Avoid rhetorical contrasts such as "It is X, not Y."

| Original wording | Replacement |
| --- | --- |
| Gradient alignment: noise, not signal | Gradient alignment: all three checks produced results within the noise range |
| We bought pedigree diversity but did not buy capability diversity | The new models cover more base models, but all accuracies are below the original interval's lower bound |
| The test and the use do not match | Evaluation uses pairwise comparisons, which differs from actual usage |
| Stability was bought with coarseness | Metrics with fewer distinct values have higher overlap rates |
| Stable metrics cannot distinguish anything; discriminative metrics are unstable | Overlap rate is inversely related to the number of distinct values |

## 5. Allow entries without numbers or conclusions

A table entry may simply describe what happened. Each entry does not need a number, a conclusion, or a comparison with another approach.

For example:

> The control group consists of 32 randomly selected questions.

This statement is complete. Do not add an explanation of how other approaches relate to the control group merely to extend it.

## 6. State when the cause is undetermined

When the cause has not been established, write "Cause undetermined" in the user's language. After stating this, do not add unverified explanations later in the document. Identify relationships that remain unverified explicitly.

| Original wording | Replacement |
| --- | --- |
| This may also explain the earlier observation | The relationship between this observation and truncation has not been verified |

Retain findings whose mechanisms have been confirmed. For example, material following a section such as Chapter 10, "The mechanism was later established," can remain when supported by the verified results.

## 7. Avoid colloquial wording

Use precise, neutral descriptions. Remove exaggeration, conversational filler, and unnecessary narrative transitions.

| Original wording | Replacement |
| --- | --- |
| Won decisively | The difference is 0.030 |
| Measured more accurately / more roughly | Higher / lower estimation precision |
| Very little room to choose | Small candidate range |
| Basically drawing lots | Close to random selection |
| Could not tell which was better anyway | The true difference is below the resolvable range |
| A wasted run / wasting occupancy | Ineffective run / idle resource occupancy |
| It did not come for free | Requires 79 GPU-hours |
| A fatal problem | Main problem |
| Looks like an after-the-fact justification | The split was determined after observing the results |
| The reason is not complicated | Omit |
| Since prediction does not work, let us take a step back | Omit and proceed directly to the experimental setup |

Use numerical replacements only when the stated values are supported by the results; these examples do not supply data for other tasks.

## 8. Avoid anthropomorphism

Describe systems, mechanisms, and changes literally, without assigning human characteristics or intentions.

| Original wording | Replacement |
| --- | --- |
| Born needing hundreds to thousands of samples | The signal requires hundreds to thousands of samples |
| Once it goes over, it creates unevenness | Truncation increases reward variance |
| Twenty-four training steps only moved it by 0.05 | Accuracy changed by 0.05 after 24 training steps |
| The more severely it overshoots, the more stable it becomes | Higher truncation rates correspond to lower reward variance |
| How good or bad the answers themselves are varies | Differences in answer quality |
