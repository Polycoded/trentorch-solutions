# Turn Eval Failures Into New Training Examples

Beginner | production-systems | synthetic-data | self-improvement

### The problem, from first principles

An eval run tells you where a model currently fails, but that information is wasted if it just sits in a report. The most direct form of self-improvement is closing the loop: take exactly the cases the model got wrong, and turn them into new training examples targeting precisely those gaps.

### The task

Write `failures_to_training_examples(eval_results)`, where each result is `(input, expected_output, passed)`. Return a `{"input", "expected_output"}` dict for every result where `passed` is False, preserving order; drop every passing result entirely.
