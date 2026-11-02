# Generate Single-Perturbation Adversarial Variants

Beginner | production-systems | synthetic-data | evaluation

### The problem, from first principles

Testing whether a model is robust to small, targeted changes -- swapping one word for a synonym, replacing "ignore" with "disregard" in an injection attempt -- needs a systematic way to generate those small variants from a base example, rather than hand-writing each one.

### The task

Write `generate_adversarial_variants(base_example, perturbations)`, where `perturbations` maps a substring to find to its replacement. For each perturbation whose substring actually appears, replace its _first_ occurrence and add the result to the output; skip perturbations that don't apply. `base_example` itself is never modified.
