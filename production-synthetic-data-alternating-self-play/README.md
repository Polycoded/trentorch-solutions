# Simulate an Alternating Self-Play Transcript

Beginner | production-systems | synthetic-data | self-improvement

### The problem, from first principles

Self-play generates training data by having two copies of a model (or two roles -- a proposer and a critic, a debater on each side) take turns interacting, with the resulting transcript itself becoming a new training example. Simulating this turn-taking correctly is the harness logic underneath any self-play data-generation pipeline.

### The task

Write `simulate_self_play(agent_a_moves, agent_b_moves, max_turns)`. Agents "A" and "B" alternate turns starting with A, each drawing from its own pre-scripted move list in order. Build the `(agent_name, move)` transcript for up to `max_turns` turns, stopping early the moment the agent whose turn it is has no move left.
