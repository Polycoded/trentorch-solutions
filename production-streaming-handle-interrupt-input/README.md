# Handle User Input While an Agent Is Mid-Task

Beginner | production-systems | streaming | real-time-agents

### The problem, from first principles

A real-time agent doesn't have the luxury of finishing one task before hearing from the user again -- messages can arrive while it's still working. Some of those messages genuinely need to interrupt what's happening ("stop, forget it"); most should just wait their turn.

### The task

Write `handle_interrupt_input(current_task, new_input, interrupt_keywords)`. If `new_input` contains any interrupt keyword (case-insensitive), return `"INTERRUPT_AND_SWITCH"` regardless of whether a task is running. Otherwise, return `"START_NEW_TASK"` if there's no current task, or `"QUEUE_AFTER_CURRENT"` if there is.
