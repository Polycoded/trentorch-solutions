# Process an Event Queue That Arrives Out of Order

Beginner | production-systems | streaming | real-time-agents

### The problem, from first principles

A real-time agent's events don't always arrive in the order they were produced -- network jitter, retries, or multiple concurrent producers (a tool result racing a token chunk) can deliver them out of sequence. Processing them in arrival order rather than in the order they actually happened can render a response with its own steps scrambled.

### The task

Write `process_event_queue(events, handlers)`. Each event is `(timestamp, event_type, payload)`. Sort by timestamp first, then for each event whose `event_type` has an entry in `handlers` (a format string with one `{}` placeholder), append `handlers[event_type].format(payload)` to the result. Skip event types with no handler.
