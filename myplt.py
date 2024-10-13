
from IPython.display import display
from IPython import get_ipython
import matplotlib.pyplot as plt
import numpy as np


def display_inline(fig, dpi=100, **kwargs):
    #get_ipython().run_line_magic('matplotlib', 'macosx')
    """ Save a copy of a plt figure inline if the current backend is external
        (e.g. 'macosx'). Useful for when you are using a high-performance
        external backend for live interaction (e.g. browsing 3D point clouds),
        but also want to store a copy of the figure inside the notebook
        (for archival purposes).

        On macOS, using `%matplotlib macosx` inside a Jupyter cell will
        force plt.show() to launch in a standalone window. Make sure you run
        `%matplotlib inline` somewhere prior, since if `%matplotlib macosx`
        is run first, it will produce an error.

        Does nothing if the current backend is already 'inline'.
    """
    if plt.get_backend() == 'inline':
        return
    orig_dpi = fig.dpi
    fig.dpi = dpi
    display(fig, **kwargs)
    fig.dpi = orig_dpi


def plot_func(ax: plt.Axes, f, a=-1, b=1, parametric=False,
              steps=1000, **kwargs):
    if parametric:
        xys = np.array([
            f(i) for i in np.linspace(a, b, steps, endpoint=False)
        ]).T
        xs, ys = xys[0], xys[1]
    else:
        xs = np.linspace(a, b, steps)
        ys = [f(x) for x in xs]
    ax.plot(xs, ys, **kwargs)