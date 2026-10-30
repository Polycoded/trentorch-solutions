# Generate Synthetic Examples From Templates

Beginner | production-systems | synthetic-data

### The problem, from first principles

Hand-writing thousands of training or eval examples is slow. If a whole family of examples shares the same structure -- "What is {n1} + {n2}?" with different numbers plugged in -- a template plus a list of values to substitute generates as many examples as needed, mechanically and consistently.

### The task

Write `generate_pairs(templates, variable_sets)` that fills in every template with every variable set (a cross product), in template-major order: all of the first template's fills before moving to the second template.
