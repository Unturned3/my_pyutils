
import time
from typing import Literal

class Timer():

    valid_units = ['s', 'ms', 'us', 'ns']

    def __init__(self, prefix: str = 'Elapsed time: ',
                 fmt: str = '{prefix}{dt:.5f} {unit}',
                 *args, end: str = '\n', unit: str = 's',
                 **kwargs):
        assert unit in Timer.valid_units
        self.prefix = prefix
        self.fmt = fmt
        self.end = end
        self.args = args
        self.unit = unit
        self.kwargs = kwargs

    def start(self):
        self.start = time.time()

    def stop(self, *args, **kwargs):
        scale = 10 ** (3 * Timer.valid_units.index(self.unit))
        self.dt = time.time() - self.start
        print(self.fmt.format(prefix=self.prefix, dt=self.dt * scale,
                              unit=self.unit, *args, **kwargs))

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *_):
        self.stop(*self.args, **self.kwargs)
