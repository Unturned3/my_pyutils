
from IPython.display import display
from matplotlib.axis import Axis
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def display_inline(fig, dpi=100, **kwargs):
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


#def set_tick_label_spacing(spacing: int, *args: Axis):
#    for axis in args:
#        axis.set_major_locator(matplotlib.ticker.MaxNLocator(spacing))


def half_label_spacing(*args: Axis):
    for axis in args:
        for label in axis.get_ticklabels()[::2]:
            label.set_visible(False)


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


def new_gizmo_3d():
    return np.array([
        0, 0, 0,
        0, 0, 1,
        0, 0, 0,
        0, 1, 0,
        0, 0, 0,
        1, 0, 0,
    ]).reshape(3, 2, 3)

def plot_gizmo_3d(ax: Axes3D, gizmo: np.array):
    assert gizmo.shape == (3, 2, 3)
    for v in gizmo:
        ax.quiver(*v[0], *v[1])
