# NeuroAI Explainers

A collection of self-contained, interactive explainers about computational neuroscience, dynamical systems, and neural networks. Most demos run entirely in the browser: open a link below and experiment with the controls.

## Live demos

GitHub Pages serves the demos directly from this repository.

### Neurons, sensory systems, and receptive fields

- [Shishi-odoshi leaky integrate-and-fire neuron](https://mrio.github.io/NeuroAI_explainers/LIF%20neuron%20shishi-odoshi/) — explore input current, leak, threshold, reset, and refractoriness through a simulated Japanese water clapper.
  - Explanation: [project README](LIF%20neuron%20shishi-odoshi/README.md)
- [Adaptive exponential (AdEx) spiking neuron phase space](https://mrio.github.io/NeuroAI_explainers/Spiking%20Neuron%20%28AdEx%29/adex_phase_space_v5.html) — explore AdEx trajectories, nullclines, and firing behavior.
  - Explanation: [project README](Spiking%20Neuron%20%28AdEx%29/README.md)
- [LGN ON/OFF center-surround cells](https://mrio.github.io/NeuroAI_explainers/LGN_on_off_cells/lgn_on_off_center_surround.html) — interact with center-surround receptive fields.
  - Explanation: [project README](LGN_on_off_cells/README.md)
- [DIY receptive field](https://mrio.github.io/NeuroAI_explainers/Receptive%20Field%20explainer/receptive_field_explainer.html) — build and probe a neuron's receptive field.
  - Explanation: [project README](Receptive%20Field%20explainer/README.md)
- [Reichardt–Hassenstein motion detector](https://mrio.github.io/NeuroAI_explainers/motion_detector/reichardt-hassenstein-explainer.html) — see how delay-and-correlate circuits detect visual motion.
  - Explanation: [project README](motion_detector/README.md)

### Networks and dynamics

- [E–I balanced LIF network](https://mrio.github.io/NeuroAI_explainers/E-I%20Networks/index.html) — explore excitation–inhibition balance in a Brunel-style spiking network.
  - Explanation: [project README](E-I%20Networks/README.md)
- [E–I balanced network (standalone version)](https://mrio.github.io/NeuroAI_explainers/E-I%20Networks/E-I_balanced_network.html) — an alternate implementation of the balanced-network demo.
  - Explanation: [project README](E-I%20Networks/README.md)
- [Feedforward neural networks](https://mrio.github.io/NeuroAI_explainers/FFNN%20explainer/FFNN_explainer.html) — a neuroscientist-oriented guide to feedforward computation.
  - Explanation: [project README](FFNN%20explainer/README.md)
- [Network propagation](https://mrio.github.io/NeuroAI_explainers/Network%20Propagation%20Demo/propagation_examples.html) — compare activity propagation through ring and feedforward networks.
  - Explanation: [project README](Network%20Propagation%20Demo/README.md)
- [Why delay kills stability](https://mrio.github.io/NeuroAI_explainers/Stability%20and%20Delays/delay_instability_explainer.html) — investigate how transmission delays destabilize feedback systems.
  - Explanation: [project README](Stability%20and%20Delays/README.md)
- [Vector Field Studio](https://mrio.github.io/NeuroAI_explainers/Vector%20Field%20Studio/vector-field-studio.html) — create and inspect two-dimensional dynamical systems.
  - Explanation: [project README](Vector%20Field%20Studio/README.md)
- [RNN Eigenspace Explorer](https://mrio.github.io/NeuroAI_explainers/RNN%20eigen%20explorer/rnn_eigen_explorer.html) — connect recurrent weights, eigenvalues, and trajectories.
  - Explanation: [project README](RNN%20eigen%20explorer/README.md)
- [Small RNN Eigenspace Explorer](https://mrio.github.io/NeuroAI_explainers/small%20RNN%20eigenspace%20explorer/) — a compact version of the RNN eigenspace demo.
  - Explanation: [project README](small%20RNN%20eigenspace%20explorer/README.md)

### Multilayer and mean-field experiments

- [Multilayer tanh/sigmoid stack](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/meanfield_layers_demo/) — the current logging-and-traces version.
  - Explanation: [project README](Multi%20Layer%20Meanfield%20Network/meanfield_layers_demo/README.md)
- [Multilayer tanh stack v6](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_tanh_v6.html) — the standalone current version.
  - Explanation: [project README](Multi%20Layer%20Meanfield%20Network/README.md)
- Earlier stack experiments: [v1](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_v1.html), [v2](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_v2.html), [v3](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_tanh_v3.html), [v4](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_tanh_v4.html), and [v5](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/multi_layer_tanh_v5.html).
  - Explanation: [project README](Multi%20Layer%20Meanfield%20Network/README.md)
- Neural-grid experiments: [v1](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/tanh_grid_v1.html), [v2](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/tanh_grid_v2.html), [v3](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/tanh_grid_v3.html), [v4](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/tanh_grid_v4.html), and [v5](https://mrio.github.io/NeuroAI_explainers/Multi%20Layer%20Meanfield%20Network/tanh_grid_v5.html).
  - Explanation: [project README](Multi%20Layer%20Meanfield%20Network/README.md)

## Running locally

Clone the repository and open any HTML file in a modern browser. The demos are static and generally require no build step, although some load JavaScript libraries from public CDNs and therefore need an internet connection.

## License

Released under the [MIT License](LICENSE).
