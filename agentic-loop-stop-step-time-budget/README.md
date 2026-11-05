# Stop an Agent Loop With a Step and Time Budget

Beginner | agentic-systems | agent-loop | orchestration

### The problem, from first principles

A ReAct loop needs more than one way to stop. The model finishing on its own is the happy path, but nothing guarantees it ever will — a confused model can loop forever, chasing the same dead end. Two independent safety nets exist for exactly this: a hard cap on the number of steps, and a hard cap on wall-clock time, since a handful of very slow tool calls could blow the time budget long before the step count does. A real loop has to check all three conditions, every step, in a well-defined order.

### From theory to code

You're given the full log of steps a run actually took: `(elapsed_seconds_after_this_step, action)`, in order, where `elapsed_seconds` is cumulative from the run's start. Implement `find_loop_stop(steps, max_steps, max_seconds)`. Walk the steps in order (1-indexed), and at each step check, **in this priority order**, the first condition that applies:

1. `action == "finish"` -> `(step_number, "FINISHED")`
2. `step_number >= max_steps` -> `(step_number, "STEP_BUDGET")`
3. `elapsed_seconds >= max_seconds` -> `(step_number, "TIME_BUDGET")`

Return `(stop_step, reason)` for whichever condition trips first.

### Constraints

- 1 to 50 steps in the log; `max_steps >= 1`, `max_seconds > 0`.
- The log is guaranteed to trip at least one of the three conditions by its last entry.

### Hints

<details>
<summary>Hint 1</summary>

Check the three conditions in the exact order given, as three separate `if` statements each returning immediately — not as a single combined boolean expression. When more than one condition is true at the same step, the priority order (not evaluation order of an `or` chain) is what decides which reason gets reported.

</details>

<details>
<summary>Hint 2</summary>

`"finish"` always wins, even on a step that would _also_ have tripped the step or time budget. Check it first, unconditionally, before touching either budget.

</details>
