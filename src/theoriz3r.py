"""
exec(open('theoriz3r.py').read())
pip3 install z3-solver
"""

import z3
from z3 import Not, ForAll, Exists, Implies, And, Or, Function
import itertools
import cProfile

exec(open('../src/utilities.py').read())
exec(open('../src/text_processing.py').read())
exec(open('../src/inputs.py').read())
exec(open('../src/checking.py').read())

