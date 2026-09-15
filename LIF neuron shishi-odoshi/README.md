# Shishi-odoshi Neuron

A leaky integrate-and-fire neuron as a Japanese water clapper. The water is a real
position-based-fluids (SPH) simulation; the bamboo tube is tipped by the actual torque of the
particles inside it, so the threshold crossing, the reset and the refractory period are all
emergent rather than scripted.

`index.html` is completely self-contained — no build step, no dependencies, no data files.
Double-clicking it works offline (fonts fall back to the system stack without a network).

## Rationale for NeuroAI students

This explainer is relevant because it turns the leaky integrate-and-fire model into a physical system students can reason about. Input, leak, threshold, reset, and refractoriness become visible causes rather than symbols in an equation, which makes the abstraction easier to carry back into spiking neuron models.

For NeuroAI students, it also helps connect mechanistic neuroscience to computation. Spike timing, rheobase, and reset dynamics are core ideas in biological modeling, neuromorphic computing, and event-based AI systems, and this demo gives those ideas a memorable concrete anchor.

## Put it online with GitHub Pages

1. Create a repository, e.g. `shishi-odoshi-neuron`.
2. Drop `index.html` and `preview.png` in at the top level and push.
3. Repo **Settings → Pages → Build and deployment → Deploy from a branch**, branch `main`, folder `/ (root)`.
4. A minute later it is live at `https://USERNAME.github.io/REPO/`.

## Two placeholders to replace first

Search `index.html` for these and swap them:

- `USERNAME.github.io/REPO` — in the `og:image`, `og:url` and source-link tags. These make the
  link unfurl with a picture in Slack, Mastodon, WhatsApp and email. They must be absolute URLs,
  so they only work once you know the final address.
- `YOUR NAME` — the attribution line in the footer.

## Other ways to hand it out

- **Brightspace**: upload `index.html` under Course Content; it renders inline.
- **Jupyter**: `from IPython.display import IFrame; IFrame('index.html', width='100%', height=760)`.
  Use an iframe rather than `HTML(...)` — the water uses an SVG filter with a fixed id that can
  collide with other cells' output.
- **Email / USB**: it is one file and runs from a local double-click.

## Knobs worth pointing students at

- Spout flow is the input current *I*; the leak hole is *g*<sub>L</sub>; the counterweight is the
  threshold θ.
- Turn the flow to about 15 with the leak up and the firing stops entirely — the leak drains the
  tube as fast as the spout fills it. That is rheobase, shown rather than asserted.
- The overshoot above θ during the tip is real: as the tube rotates, the water slides toward the
  mouth and its lever arm grows, so the torque runs away. It is the mechanical analogue of the
  spike upstroke.

## License

CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
