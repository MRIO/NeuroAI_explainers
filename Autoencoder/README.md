# Through the Keyhole: Autoencoders

## Rationale for NeuroAI students

Autoencoders are a compact way to study representation learning: the network must rebuild its input after squeezing it through a narrow latent bottleneck. This explainer makes the full loop visible, from pixels to latent units to reconstructed pixels, so students can see how reconstruction error drives changes in both encoder and decoder weights.

For NeuroAI students, the demo is relevant because it connects neural-network learning to ideas that also matter in neuroscience: compression, latent variables, receptive fields, projective fields, dimensionality reduction, and sparse parts-based representations. By changing the bottleneck and inspecting the learned units, students can reason about what information is preserved, what is discarded, and how internal features emerge without explicit labels.

## Open

- [Local demo](autoencoder_explainer.html)
