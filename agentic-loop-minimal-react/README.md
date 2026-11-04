# A Minimal ReAct Loop: Thought -> Action -> Observation

Beginner | agentic-systems | agent-loop | orchestration

### The problem, from first principles

Every "agent" that does more than answer one question in one shot is running some version of the same tiny loop: the model reasons about what to do next (a _thought_), decides on a concrete _action_ to take, and gets back an _observation_ — the real-world result of that action — which feeds into its next thought. Repeat until the model decides it has enough to answer. This loop, ReAct (Reason + Act), is the base pattern underneath almost every agent framework; everything more sophisticated (retries, routing, multi-agent handoffs) is a variation layered on top of this same three-part cycle.

### From theory to code

You're given the model's full scripted sequence of `(thought, action, action_input)` turns — as if already generated, no real model call needed here — and a lookup table of what each action call actually returns. Implement `run_react_loop(steps, observations, max_steps)`. Process `steps` in order, up to `max_steps`. For each step, look up its observation from `observations` (using `"NO_OBSERVATION_FOUND"` if that exact `(action, action_input)` was never scripted), and append `(thought, action, action_input, observation)` to the trace. The moment `action == "finish"`, stop immediately — record that step with an empty observation and don't consult `observations` at all for it.

Return the trace built so far.

### Constraints

- 1 to 50 steps in the log; `max_steps >= 1`.
- `action` is never the literal string `"finish"` except to signal the loop should stop.

### Hints

<details>
<summary>Hint 1</summary>

Check the step budget _before_ processing each step, not after — that's what makes `max_steps` an exact cap on how many entries the returned trace can have, rather than an off-by-one over- or under-count.

</details>

<details>
<summary>Hint 2</summary>

The `"finish"` check has to come before the observation lookup, not after. If a `"finish"` entry accidentally has an entry in `observations` too, it must still never be consulted — finishing is a different kind of action, not just another tool call.

</details>
