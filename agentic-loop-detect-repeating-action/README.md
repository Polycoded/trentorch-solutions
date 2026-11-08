# Detect a Repeating Action and Break the Loop

Intermediate | agentic-systems | agent-loop | reliability

### The problem, from first principles

A model stuck in a bad pattern doesn't always fail loudly — sometimes it just calls the exact same tool with the exact same arguments over and over, each time apparently confident this attempt will be different, never actually making progress. This looks completely different from the "consecutive failures" pattern in the earlier self-reflection question: the observations here might not look like failures at all (the tool might succeed every time!) — the problem is purely that the _same action_ keeps recurring, which is its own distinct signal that something's wrong.

### From theory to code

You're given every step's `(action, action_input)` pair, in order, a `window` size, and a `repeat_threshold`. Implement `detect_repeating_action(actions, window, repeat_threshold)`. Walk the steps in order. After each step, look at only the last `window` steps seen so far (fewer if not enough steps have happened yet) and count how many of them exactly match the action just taken. The moment that count reaches `repeat_threshold`, return the current 1-indexed step number. Return `None` if it never happens.

### Constraints

- 1 to 500 steps; `window >= 1`, `repeat_threshold >= 1`.

### Hints

<details>
<summary>Hint 1</summary>

A fixed-size sliding window is exactly what `collections.deque(maxlen=window)` gives you for free — appending past capacity automatically drops the oldest entry, so you never need to manually trim anything.

</details>

<details>
<summary>Hint 2</summary>

Count matches _within the current window only_, not across the whole history — a `deque` with `maxlen` set already only ever contains the most recent `window` items, so counting within it is automatically counting within the window.

</details>
