
import nengo
import numpy as np

model = nengo.Network(label="Brunel E/I Balance")
with model:
    # Parameters
    N_E = 400   # excitatory neurons
    N_I = 100   # inhibitory neurons
    p = 0.1     # connection probability
    tau = 0.05  # synaptic time constant
    tau_rc = 0.02
    # Populations
    E = nengo.Ensemble(N_E, 1, neuron_type=nengo.LIF())
    I = nengo.Ensemble(N_I, 1, neuron_type=nengo.LIF())
    
    # Background noise
    stim = nengo.Node(lambda t: np.random.randn() * 0.001)
    nengo.Connection(stim, E, synapse=None)
    nengo.Connection(stim, I, synapse=None)
    
    # Scaling sliders
    w_e = nengo.Node([1.0])   # excitatory weight scale
    w_i = nengo.Node([1.0])   # inhibitory weight scale

    # Random connectivity masks
    mask_EE = (np.random.rand(N_E, N_E) < p).astype(float)
    mask_EI = (np.random.rand(N_I, N_E) < p).astype(float)
    mask_IE = (np.random.rand(N_E, N_I) < p).astype(float)
    mask_II = (np.random.rand(N_I, N_I) < p).astype(float)

    # Use neuron-to-neuron connections (pre=neurons, post=neurons)
    conn_EE = nengo.Connection(E.neurons, E.neurons,
                               transform=mask_EE, synapse=tau)
    conn_EI = nengo.Connection(E.neurons, I.neurons,
                               transform=mask_EI, synapse=tau)
    conn_IE = nengo.Connection(I.neurons, E.neurons,
                               transform=-mask_IE, synapse=tau)
    conn_II = nengo.Connection(I.neurons, I.neurons,
                               transform=-mask_II, synapse=tau)

    # # To scale weights live, connect nodes into the transform
    # nengo.Connection(w_e, conn_EE.transform)  # excitatory scaling
    # nengo.Connection(w_e, conn_EI.transform)
    # nengo.Connection(w_i, conn_IE.transform)  # inhibitory scaling
    # nengo.Connection(w_i, conn_II.transform)

    # # Probes for spikes
    # p_e = nengo.Probe(E.neurons, 'spikes')
    # p_i = nengo.Probe(I.neurons, 'spikes')