# Detect a Tool Call Marker as It Streams In

Beginner | production-systems | streaming | real-time-agents

### The problem, from first principles

A streaming model often signals a tool call with a special marker embedded in its output (e.g. `<tool_call>`), but that marker isn't guaranteed to land inside a single chunk -- streaming APIs split text at arbitrary byte or token boundaries, so the marker can easily be cut in half across two consecutive chunks.

### The task

Write `detect_early_tool_call(chunks, marker)` that returns the index of the first chunk after which the accumulated text contains `marker`, or `None` if it never appears.
