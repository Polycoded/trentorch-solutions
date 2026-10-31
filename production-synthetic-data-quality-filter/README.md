# Filter Low-Quality Synthetic Examples

Beginner | production-systems | synthetic-data

### The problem, from first principles

Generating synthetic training data mechanically (templates, model self-generation) produces volume, but not every generated example is actually usable -- some are too short to carry any real signal, and some are degenerate model outputs like a refusal or a disclaimer that leaked into what should have been a clean training example.

### The task

Write `filter_quality(examples, min_length, banned_phrases)` that keeps only examples at least `min_length` characters long and containing none of `banned_phrases`, case-insensitively, preserving original order.
