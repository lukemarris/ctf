from examples.functions2d.utils import function_example
from ctf.functions1d import *

minima = [Absolute]

name = ["absolute"]

for Func, name in zip(minima, name):
    func = Func()
    function_example(func, name)