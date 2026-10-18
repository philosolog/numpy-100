import numpy as np

import generators as ge

rng = np.random.default_rng()


def question(n):
    print(f'{n}. ' + ge.QHA[f'q{n}'])


def hint(n):
    print(ge.QHA[f'h{n}'])


def answer(n):
    print(ge.QHA[f'a{n}'])


def pick():
    n = rng.integers(1, 101)
    question(n)
