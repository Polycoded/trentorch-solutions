# Find Where a Stream Was Cancelled

Beginner | production-systems | streaming | real-time-agents

### The problem, from first principles

A real-time agent can be cancelled mid-response -- a user closes the chat, navigates away, or explicitly hits stop. Whatever was received before that cancellation is still valid and worth keeping; anything after it never happened as far as the user is concerned and shouldn't be processed.

### The task

Write `find_cancel_point(events)`, where each event is `(event_type, payload)` and `event_type` is one of `"chunk"`, `"tool_call"`, `"done"`, or `"cancel"`. Return the index of the first `"cancel"` event, or `None` if the stream was never cancelled.
