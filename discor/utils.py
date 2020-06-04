from collections import deque
import numpy as np


def update_params(optim, loss, retain_graph=False):
    optim.zero_grad()
    loss.backward(retain_graph=retain_graph)
    optim.step()


def disable_gradients(network):
    for param in network.parameters():
        param.requires_grad = False


def soft_update(target, source, tau):
    for t, s in zip(target.parameters(), source.parameters()):
        t.data.copy_(t.data * (1.0 - tau) + s.data * tau)


class RunningMeanStats:

    def __init__(self, n=10):
        assert isinstance(n, int) and n > 0
        self._stats = deque(maxlen=n)

    def append(self, x):
        self._stats.append(x)

    def get(self):
        return np.mean(self._stats)