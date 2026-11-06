# Decompose a Goal Into an Ordered Sub-Task List

Intermediate | agentic-systems | agent-loop | planning

### The problem, from first principles

Deciding _what_ the sub-tasks of a goal are is a creative, model-driven step — genuinely hard to test deterministically, since there's rarely one "correct" decomposition. But once the sub-tasks and their dependencies are known ("research the topic" has to happen before "write the draft," which has to happen before "proofread"), deciding what _order_ to actually run them in is a completely mechanical problem: find any order that never runs a sub-task before something it depends on.

### From theory to code

You're given every sub-task's name and a list of `(before, after)` dependency pairs — `before` must be scheduled strictly earlier than `after`. The dependency graph is guaranteed acyclic (no sub-task can depend on itself, directly or transitively). Implement `order_subtasks(subtasks, dependencies)`. Produce a valid execution order respecting every dependency. When more than one sub-task is available to schedule next (no unscheduled dependency blocking it), prefer whichever one comes **first in the original `subtasks` list** — this is what makes the answer unique instead of "any valid order."

Return the full ordered list of sub-task names.

### Constraints

- 1 to 100 sub-tasks, distinct names.
- 0 to 500 dependency pairs; the dependency graph never contains a cycle.

### Hints

<details>
<summary>Hint 1</summary>

This is the standard "topological sort" problem, but the tie-break rule (prefer whatever's earliest in the original list) means you can't just use any topological sort algorithm off the shelf unmodified — a priority-queue-based approach keyed on "earliest in the original list among currently-schedulable tasks" is the direct way to get this specific tie-break, though a simple repeated linear scan over the original list works fine too at these bounds.

</details>

<details>
<summary>Hint 2</summary>

Track each sub-task's remaining "blockers" count (how many not-yet-scheduled dependencies it has). A sub-task becomes eligible to schedule the moment that count hits zero — recompute it incrementally as you schedule things, rather than rescanning the full dependency list on every step.

</details>
