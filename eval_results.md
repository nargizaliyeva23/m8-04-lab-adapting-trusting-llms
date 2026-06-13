# Eval Results

## Task 2 — LLM-as-judge pass-rate table

| Variant | Cases | Passed | Pass rate |
|----------|----------|----------|----------|
| Few-shot | 10 | 7 | 70% |
| Embeddings | 10 | 6 | 60% |

## Rubric used by the judge

PASS:
- predicted label matches expected label

FAIL:
- predicted label does not match expected label

## Verdict

The few-shot classifier achieved a higher pass rate than the embeddings classifier. It was better at understanding the meaning of unseen tickets and generalizing beyond the training examples.

I do not fully trust the judge in this task because the correct labels are already known. Direct comparison against ground-truth labels is more reliable. However, LLM-as-judge becomes valuable when evaluating open-ended tasks that do not have a single correct answer.

## A case where the judge looked wrong

The password reset and account settings tickets were difficult because similar examples were not present in the training set. In such cases, both the classifier and the judge may make decisions that are reasonable but still differ from the expected label.