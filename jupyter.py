from IPython import get_ipython

magic_commands = [
    'load_ext autoreload',
    'autoreload 2',
    'matplotlib inline',
    'config InlineBackend.print_figure_kwargs = {"bbox_inches": None}',
]

magic_commands = [s.split(' ', 1) for s in magic_commands]

def jupyter_init():
    ipy = get_ipython()
    for (cmd, args) in magic_commands:
        ipy.run_line_magic(cmd, args)
