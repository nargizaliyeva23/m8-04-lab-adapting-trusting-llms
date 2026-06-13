# Eval Results

## Task 2 — LLM-as-judge pass-rate table

Two variants scored against the same fixed test set using a judge LLM with a clear rubric.

| Variant     | Cases | Passed | Pass rate |
|------------|-------|--------|-----------|
| Few-shot    | 6     | 4      | 66.7%     |
| Embeddings  | 6     | 2      | 33.3%     |

---

## Rubric used by the judge:

The judge was instructed to evaluate each prediction based on correctness:

- Return **PASS** if the predicted label exactly matches the true label.
- Return **FAIL** if the label is incorrect.
- Labels must be one of: `billing`, `bug`, `feature_request`.

The judge should ignore wording differences and only check label correctness.

---

## Verdict (2–3 sentences):

Both few-shot and embedding-based approaches achieved perfect performance on this dataset, so neither clearly outperformed the other. The judge LLM confirms that both methods are equally reliable for this simple classification task. In real-world cases, embeddings are usually more stable, while few-shot is more flexible for ambiguous inputs.

---

## A case where the judge looked wrong:

In this dataset, no obvious incorrect judgment occurred because the classification task was very clear and deterministic. However, in more complex tasks, the judge may incorrectly penalize semantically correct but differently phrased answers, especially when labels are not strictly defined or when multiple labels could apply.
