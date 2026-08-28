# NeuroAI Explainers

A collection of self-contained, interactive explainers about computational neuroscience, dynamical systems, and neural networks. Most demos run entirely in the browser: open a link below and experiment with the controls.

## Live demos

GitHub Pages serves the demos directly from this repository.

### Neurons, sensory systems, and receptive fields

- [Adaptive exponential (AdEx) spiking neuron phase space](https://mrio.github.io/NeuroAI_explainers/Spiking%20Neuron%20%28AdEx%29/adex_phase_space_v5.html) — explore AdEx trajectories, nullclines, and firing behavior.
- [Adaptive exponential (AdEx) 2D phase space](https://mrio.github.io/NeuroAI_explainers/Spiking%20Neuron%20%28AdEx%29/2D_spking_phase_space.html) — an alternative version of the AdEx phase-space explorer.
- [LGN ON/OFF center-surround cells](https://mrio.github.io/NeuroAI_explainers/LGN_on_off_cells/lgn_on_off_center_surround.html) — interact with center-surround receptive fields.
- [DIY receptive field](https://mrio.github.io/NeuroAI_explainers/Receptive%20Field%20explainer/receptive_field_explainer.html) — build and probe a neuron's receptive field.
- [Reichardt–Hassenstein motion detector](https://mrio.github.io/NeuroAI_explainers/motion_detector/reichardt-hassenstein-explainer.html) — see how delay-and-correlate circuits detect visual motion.

### Networks and dynamics

- [E–I balanced LIF network](https://mrio.github.io/NeuroAI_explainers/E-I%20Networks/index.html) — explore excitation–inhibition balance in a Brunel-style spiking network.
- [E–I balanced network (standalone version)](https://mrio.github.io/NeuroAI_explainers/E-I%20Networks/E-I_balanced_network.html) — an alternate implementation of the balanced-network demo.
- [Feedforward neural networks](https://mrio.github.io/NeuroAI_explainers/FFNN%20explainer/FFNN_explainer.html) — a neuroscientist-oriented guide to feedforward computation.
- [Network propagation](https://mrio.github.io/NeuroAI_explainers/Network%20Propagation%20Demo/propagation_examples.html) — compare activity propagation through ring and feedforward networks.
- [Why delay kills stability](https://mrio.github.io/NeuroAI_explainers/Stability%20and%20Delays/delay_instability_explainer.html) — investigate how transmission delays destabilize feedback systems.
- [Vector Field Studio](https://mrio.github.io/NeuroAI_explainers/Vector%20Field%20Studio/vector-field-studio.html) — create and inspect two-dimensional dynamical systems.
- [RNN Eigenspace Explorer](https://mrio.github.io/NeuroAI_explainers/RNN%20eigen%20explorer/rnn_eigen_explorer.html) — connect recurrent weights, eigenvalues, and trajectories.
- [Small RNN Eigenspace Explorer](https://mrio.github.io/NeuroAI_explainers/small%20RNN%20eigenspace%20explorer/) — a compact version of the RNN eigenspace demo.

### Multilayer and mean-field experiments

- [Multilayer tanh/sigmoid stack](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/meanfield_layers_demo/) — the current logging-and-traces version.
- [Multilayer tanh stack v6](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_tanh_v6.html) — the standalone current version.
- Earlier stack experiments: [v1](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_v1.html), [v2](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_v2.html), [v3](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_tanh_v3.html), [v4](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_tanh_v4.html), and [v5](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_tanh_v5.html).
- Neural-grid experiments: [v1](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/tanh_grid_v1.html), [v2](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/tanh_grid_v2.html), [v3](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/tanh_grid_v3.html), [v4](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/tanh_grid_v4.html), and [v5](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/tanh_grid_v5.html).

## Running locally

Clone the repository and open any HTML file in a modern browser. The demos are static and generally require no build step, although some load JavaScript libraries from public CDNs and therefore need an internet connection.

## License

Released under the [MIT License](LICENSE).
