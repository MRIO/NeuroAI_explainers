# Stabilizing Hebbian Learning: Oja's Rule

## Rationale for NeuroAI students

Hebbian learning is one of the simplest ideas linking neural activity to synaptic change, but the plain rule is unstable: weights keep growing because stronger weights create stronger postsynaptic responses. This explainer shows why Oja's extra decay term is not just a mathematical patch, but a local stabilizing mechanism that a synapse can compute from the input, output, and its own weight.

For NeuroAI students, the demo is relevant because it connects plasticity, normalization, and representation learning. Oja's rule turns a biologically motivated Hebbian update into a principal-component learner, making it a compact bridge between synaptic plasticity, unsupervised learning, dimensionality reduction, and the emergence of feature-selective neurons.

## Open

- [Local demo](oja_rule.html)
