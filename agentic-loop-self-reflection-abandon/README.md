# Self-Reflection: Critique the Last Step Before Continuing

Intermediate | agentic-systems | agent-loop | reliability

### The problem, from first principles

An agent that never looks back at its own last step will happily repeat a failing action forever, burning its step and time budgets on something that was never going to work. A minimal form of self-reflection is much cheaper than a full model-based critique: just watch for observations that look like failures, and give up once too many have happened _in a row_ — a single isolated failure is normal and worth retrying past, but a run of consecutive failures is a strong signal something is fundamentally broken, not just unlucky.

### From theory to code

You're given every step's observation text, in order, a list of `failure_keywords`, and a `max_consecutive_failures` threshold. Implement `find_abandon_point(observations, failure_keywords, max_consecutive_failures)`. An observation "looks like a failure" if it contains **any** of `failure_keywords` as a substring. Track a running count of _consecutive_ failure-looking observations — any success resets the count to zero. Return the 1-indexed step at which that running count first reaches `max_consecutive_failures`, or `None` if it never does.

### Constraints

- 1 to 200 observations; keyword matching is case-sensitive, plain substring (no regex).

### Hints

<details>
<summary>Hint 1</summary>

One running counter, reset to zero on any success and incremented on any failure, is the entire piece of state you need — no need to look backward at a window of previous observations each time.

</details>

<details>
<summary>Hint 2</summary>

`any(keyword in observation for keyword in failure_keywords)` checks "does this specific observation look like a failure" in one line — don't build a combined regex or loop-within-a-loop by hand.

</details>
