# A Handoff Mechanism: Route to the Right Agent

Beginner | agentic-systems | multi-agent | orchestration

### The problem, from first principles

A conversation doesn't always stay in one agent's wheelhouse — it might start as a general question and turn into a refund request, or a bug report. A handoff mechanism watches for that shift and moves the conversation to whichever agent is actually built to handle it, rather than making one generalist agent muddle through every topic.

### From theory to code

You're given `current_agent`, the latest `message`, and `routing_rules` — an ordered list of `(keyword, target_agent)` pairs, checked in order with case-insensitive substring matching. Implement `route_handoff(current_agent, message, routing_rules)`. Return the `target_agent` of the **first** rule whose keyword appears anywhere in `message`. If no rule matches, stay with `current_agent` (no handoff).

### Constraints

- `routing_rules` has 0 to 50 entries; keyword matching is case-insensitive, plain substring (no word-boundary requirement).

### Hints

<details>
<summary>Hint 1</summary>

Lowercase the message once, up front, and compare against each rule's lowercased keyword — this handles case-insensitivity cleanly without repeatedly re-lowercasing the same message inside the loop.

</details>

<details>
<summary>Hint 2</summary>

Return the moment the first matching rule is found — don't scan the rest of the rules once a match has already been decided. The rule order matters precisely because the first match wins.

</details>
