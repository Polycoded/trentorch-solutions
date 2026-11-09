# Message-Passing Between Two Agents Over Shared State

Beginner | agentic-systems | multi-agent | orchestration

### The problem, from first principles

One common way for multiple agents to coordinate without a rigid supervisor hierarchy is a shared blackboard: any agent can write a value under a named key, and any agent can read the current value of any key. There's no negotiation protocol, no locking — just a simple rule for what happens when two agents write the same key: whoever wrote most recently wins, and the system remembers who that was.

### From theory to code

You're given the full message log: `(sender, key, value)` triples, in order, where each message writes `value` into the shared state under `key`. Implement `process_message_log(messages)`. Process the messages in order. Return the final state: a dict from key to `(value, last_writer)`, reflecting whichever message most recently wrote that key.

### Constraints

- 0 to 1000 messages; any number of distinct agents and keys.

### Hints

<details>
<summary>Hint 1</summary>

One dict, updated in a single forward pass, is the entire solution — for each message, just overwrite `state[key]` with the new `(value, sender)` pair. There's no need to check whether the key already exists; overwriting unconditionally already implements "last write wins."

</details>

<details>
<summary>Hint 2</summary>

The same agent overwriting its own earlier write to the same key is not a special case — it's handled by the exact same unconditional overwrite as two different agents writing the same key.

</details>
