# Echo State Decoder: Reservoir To Figure-Eight Arm

## Rationale for NeuroAI students

This explainer shows how an echo state network can use a fixed random recurrent reservoir as a dynamical memory, then train only a simple readout to produce useful behavior. Here, the target behavior is a two-joint arm tracing a figure-eight path, so students can see how reservoir state, decoded joint angles, and movement unfold together.

For NeuroAI students, the demo is relevant because it separates recurrent dynamics from supervised output learning. That makes reservoir computing a clear example of how rich neural dynamics can provide a reusable computational substrate, while a lightweight decoder learns to extract the task-relevant variables.

## Open

- [Local demo](index.html)
