# Layered Neural Sheet Demo

This repository contains a single-page, browser-based demo of a **recurrent neural network** laid out as a stack of 2D sheets of neurons.

Each sheet is a 60×60 grid of simple discrete-time neurons with either:

- **tanh** nonlinearity, or  
- **sigmoid** nonlinearity mapped to \([-1, 1]\),

and with **local topographic connectivity**, **random recurrent connections**, and **feedforward / feedback coupling** across three layers.

The goal is to make the dynamics **visible and explorable** in real time: you can poke neurons, watch their traces, change connectivity structure, and inspect a compressed adjacency matrix on the fly.

---

## Quick start

1. Clone the repo or download the HTML file (e.g. `index.html`).
2. Open it in a **modern browser** (Chrome, Firefox, Safari).
3. That’s it — everything runs locally in JavaScript, no build step needed.

You should see:

- On the **left**: a vertically stacked view of three oblique “sheets” of neurons, each shown as a heatmap (blue → gray → red).
- On the **top-right of the sheet canvas**: a small inset showing a compressed **connectivity matrix**.
- On the **right side**: controls, a neuron trace viewer, and a parameter dump button.

---

## Model overview

### Network architecture

- **Layers:** 3
- **Neurons per layer:** 60×60 = 3,600
- **Total neurons:** 10,800
- **Boundary conditions:** periodic in both x and y (toroidal grid)

We index neurons as:

- layer \(\ell \in \{0,1,2\}\)
- coordinates \((x,y)\) with \(x,y \in \{0, \dots, 59\}\)
- state \(a_{\ell}(x,y,t) \in [-1,1]\) at discrete time step \(t\)

Layer 0 is treated as the **input (sensory) layer**; layers 1 and 2 are progressively “deeper”.

---

### Dynamics

Each neuron updates according to a leaky nonlinearity:

\[
a_i(t+1) = (1 - \lambda)\, a_i(t) + \lambda \, \phi(I_i(t)),
\]

where:

- \(\lambda \in [0,1]\) is the **leak** (slider `Leak (update fraction λ)`),
- \(\phi\) is either:
  - **tanh:** \(\phi(x) = \tanh(x)\), or  
  - **sigmoid** mapped to \([-1,1]\):  
    \(\phi(x) = 2\,\sigma(x)-1 = \frac{2}{1+e^{-x}} - 1\),
- \(I_i(t)\) is the total synaptic + external input to neuron \(i\).

---

### Input (walker stimulus)

A single “walker” performs either:

- a **random walk** on the grid (default), or  
- is **manually positioned** using two sliders (X/Y),

always on **layer 0** (input layer).

The walker injects a local Gaussian bump of input:

\[
I^{\text{stim}}_{\ell}(x,y,t) =
\begin{cases}
A \exp\left( -\dfrac{(x - x_w)^2 + (y - y_w)^2}{2\sigma^2} \right), & \ell = 0 \\
0, & \text{otherwise}
\end{cases}
\]

where:

- \(A\) is `Walker stimulus strength`,
- \(\sigma\) is fixed (`sigmaStim` in the code),
- \((x_w, y_w)\) is the walker position.

---

### Local recurrent connectivity

Within each layer, each neuron receives input from a **local neighborhood** defined by a kernel over offsets \((\Delta x, \Delta y)\) in a small radius (e.g. radius = 3).

Two types of kernels are supported:

1. **Gaussian kernel** (normalized to sum to 1):  
   \[
   w_{\text{loc}}(\Delta x, \Delta y) \propto
   \exp\left(-\frac{\Delta x^2 + \Delta y^2}{2\sigma_{\text{loc}}^2}\right).
   \]

2. **Mexican-hat (center–surround) kernel**, implemented as a **difference of Gaussians (DoG)** with zero integral:
   \[
   w_{\text{loc}} = G_{\sigma_{\text{exc}}} - B\, G_{\sigma_{\text{inh}}},
   \]
   where \(B\) is chosen so that the sum over the kernel is zero, then rescaled to have \(\max |w_{\text{loc}}| = 1\).

Local input to neuron \(i = (\ell, x, y)\):

\[
I^{\text{local}}_i(t) =
g_{\text{local}}
\sum_{\Delta x, \Delta y}
w_{\text{loc}}(\Delta x, \Delta y)\,
a_{\ell}(x + \Delta x,\, y + \Delta y,\, t),
\]

with toroidal wrapping in x and y. `Local coupling gain (g_local)` controls \(g_{\text{local}}\).

---

### Random recurrent connectivity (within-layer)

Each layer also has **sparse random connections**:

- For each neuron, an approximate in-degree \(k\) is determined from  
  `Random conn. probability` × number of neurons in the layer.
- For each **post** neuron, a set of random **pre** neurons is chosen within *the same* layer.
- All **random edges are strictly within-layer** (assertions in the code guard against cross-layer edges).
- Random weights are drawn from \([-1,1]\), optionally made strictly positive or negative to enforce **Dale’s rule**.

To keep dynamics more stable when density changes, weights are scaled by \(1/\sqrt{k}\), so the random probability slider mostly changes **topology**, not just effective gain.

Random input term:

\[
I^{\text{rand}}_i(t) =
g_{\text{random}}
\sum_{j \in \mathcal{R}(i)} w_{ij} \, a_j(t),
\]

where \(\mathcal{R}(i)\) is the set of random presynaptic partners of neuron \(i\). `Random connectivity gain (g_random)` controls \(g_{\text{random}}\).

**Dale’s rule** (checkbox) makes each neuron **either excitatory or inhibitory**:

- E neurons have all outgoing random weights \(\ge 0\),
- I neurons have all outgoing random weights \(\le 0\).

---

### Feedforward & feedback across layers

Cross-layer connectivity uses **the same local kernel** as within-layer, but scaled by separate gains.

For neuron \(i = (\ell, x, y)\):

- **Feedforward** (from layer \(\ell-1\) to \(\ell\), for \(\ell > 0\)):

  \[
  I^{\text{ff}}_i(t) =
  g_{\text{cross}}
  \sum_{\Delta x, \Delta y}
  w_{\text{loc}}(\Delta x, \Delta y)\,
  a_{\ell - 1}(x + \Delta x, y + \Delta y, t).
  \]

- **Feedback** (optional, from layer \(\ell+1\) to \(\ell\)):

  \[
  I^{\text{fb}}_i(t) =
  g_{\text{back}}
  \sum_{\Delta x, \Delta y}
  w_{\text{loc}}(\Delta x, \Delta y)\,
  a_{\ell + 1}(x + \Delta x, y + \Delta y, t).
  \]

These are controlled by:

- `Feedforward gain (g_cross)` (\(g_{\text{cross}}\))
- `Enable back projections` (checkbox)
- `Back projection gain (g_back)` (\(g_{\text{back}}\))

---

### Full input equation

Putting it together, the total input to each neuron is:

\[
I_i(t) = I^{\text{local}}_i(t)
       + I^{\text{rand}}_i(t)
       + I^{\text{ff}}_i(t)
       + I^{\text{fb}}_i(t)
       + I^{\text{stim}}_i(t),
\]

and the state update is:

\[
a_i(t+1) = (1 - \lambda)\, a_i(t) + \lambda\, \phi(I_i(t)).
\]

---

## UI & interaction guide

### Main sheet view (left pane)

- Shows the 3 layers as slightly sheared “parallelogram” sheets.
- Each neuron is colored with a **blue–gray–red** colormap:
  - blue ≈ strongly negative
  - gray ≈ around 0
  - red ≈ strongly positive

Layers are stacked vertically (no overlap), with:

- **Layer 0** at the bottom (input layer),
- **Layer 2** at the top (deepest).

A **white square** marks the current walker position on the input layer.

If you **click** on any neuron in any layer:

- That neuron is highlighted in **yellow**.
- Its activity trace is shown in the **trace viewport** on the right.

---

### Neuron trace viewer

On the right, the “Neuron trace” panel shows the last ~400 time steps of the selected neuron:

- x-axis: time (recent history, rolling buffer)
- y-axis: activity \([-1,1]\)
- middle horizontal line: 0
- green curve: selected neuron’s activity

You can:

- change parameters while watching **how single-cell dynamics react**,
- click different neurons to compare behavior of:
  - input vs deep layers,
  - excitatory-like vs inhibitory-like cells,
  - cells near vs far from the walker stimulus.

---

### Walker / input controls

- `Manual walker control` (checkbox)
  - Off: walker performs a random walk on the input layer.
  - On: you control it via sliders:
    - `Walker X position`
    - `Walker Y position`
- `Walker stimulus strength`: amplitude \(A\) of the Gaussian bump.

---

### Dynamics controls

- `Leak (update fraction λ)`
  - 0: states are frozen, no updates.
  - 1: full nonlinearity update each step.
- `Use sigmoid nonlinearity`
  - Off: use \(\tanh\).
  - On: use logistic mapped to \([-1,1]\), \(2\sigma(x)-1\).

---

### Local connectivity

- `Local coupling gain (g_local)`: scales the contribution of the local kernel.
- `Use Mexican-hat local kernel`:
  - Off: single Gaussian (smooth, cooperative).
  - On: center–surround DoG with zero integral (pattern-forming, winner–surround-loser).

---

### Random connectivity

- `Random conn. probability`: controls the **density** of random recurrent connections within each layer.
- `Random connectivity gain (g_random)`: scales their impact.
- `Enforce Dale's rule (per layer)`:
  - On: each neuron is classified as E or I; all its random outgoing weights share the same sign.
- `Regenerate random connectivity`:
  - Re-samples the random graph and weights (respecting current probability and Dale’s rule setting).

---

### Cross-layer connectivity

- `Feedforward gain (g_cross)`:
  - Local, kernel-shaped projections from **layer \(\ell\) to \(\ell+1\)**.
- `Enable back projections`:
  - Turn on local feedback (\(\ell+1 \to \ell\)) using the same kernel shape.
- `Back projection gain (g_back)`:
  - Scales the feedback term.

These let you explore:

- purely feedforward regimes,
- recurrent hierarchies with feedback,
- how patterns propagate (or echo) through depth.

---

### Simulation speed

- `Update speed`:
  - Number of discrete update iterations per animation frame.
  - Increasing this makes the dynamics “run faster” while keeping rendering at a reasonable frame rate.

---

## Compressed connectivity inset

The inset on the **top-right** is a **compressed effective connectivity matrix**, computed from:

- local kernel (within and across layers),
- random connectivity,
- feedforward and feedback gains.

Key ideas:

- Neurons within each layer are grouped into **bins** (e.g. 24 groups per layer).
- For each pair of groups (pre, post), the code accumulates an **average effective weight**:
  - local + random + feedforward + feedback (depending on current slider values).
- This yields a small matrix of size:
  \[
  \text{CM} = \text{LAYERS} \times \text{BINS\_PER\_LAYER},
  \]
  visualized as a CM×CM heatmap.

You’ll see:

- A **block structure**:
  - diagonal blocks = within-layer connectivity (local + random),
  - off-diagonal blocks = feedforward / feedback between layers.
- Colorbar (next to it):
  - red = positive effective weight,
  - blue = negative,
  - gray ≈ zero.

As you tweak:

- `g_local`, `g_random`, `g_cross`, `g_back`,
- `Use Mexican-hat`,
- or toggle feedback on/off,

you can watch the **structure of the effective adjacency matrix** change in real time.

---

## Parameter & connectivity logging

The `Dump params + connectivity (JSON)` button:

- captures the current simulation state into a JSON file that includes:
  - basic parameters (layer size, kernel settings),
  - all sliders and checkbox states,
  - the **local kernel** values (Gaussian or Mexican hat),
  - the **full random connectivity edge list** (sparse),
  - the current **compressed connectivity matrix** (grouped).

This makes it easy to:

- archive interesting regimes,
- analyze connectivity offline (e.g. in Python/NumPy),
- or reconstruct comparable networks in other environments.

---

## Educational angles & extensions

This toy model is a nice playground for:

- **Criticality and spectral radius**  
  Tuning `g_local` and `g_random` can move the network from quiescent to chaotic regimes.
- **Pattern formation**  
  Mexican-hat kernels naturally generate bumps, rings, and traveling patterns.
- **Hierarchical processing**  
  Turn on feedforward and feedback to explore how activity propagates and echoes across layers.
- **Single-cell & population views**  
  Combine the sheet view, neuron trace, and adjacency inset to relate **micro** (neuron-level) and **macro** (group-level connectivity) structure.



## License & Attribution

The code in this repository is licensed under the Apache License 2.0.

If you use this project in your own work, please include a reference such as:

> Based on the "Layered Neural Sheet Demo" by Mario Negrello (Apache-2.0), developed with AI-assisted coding using ChatGPT (OpenAI).

---

## Credits

This code was designed as an **interactive educational resource** for exploring dynamical behavior in simple recurrent neural sheets: local vs random connectivity, hierarchical couplings, and single-neuron activity — all in real time, in the browser.

- Concept, design and implementation: Mario Negrello
- AI-assisted iteration and code drafting: ChatGPT (GPT-5.1 Thinking, OpenAI)

Enjoy poking your little cortical sheet ✨
