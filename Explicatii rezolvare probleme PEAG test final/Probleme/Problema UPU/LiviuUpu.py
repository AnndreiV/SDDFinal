import numpy as np


def fitness(x, fr, n):
    val = 0
    for i in range(n):
        for j in range(n):
            val += fr[i, j] * (1.7 + 3.4 * np.sqrt((i - x[0]) ** 2 + (j - x[1]) ** 2))
    return val  # transformare in problema de maxim, normal era <return val>


def gen_pop(ff, dim):
    fr = np.genfromtxt(ff)
    n = len(fr)
    pop = []
    for i in range(dim):
        x = np.random.randint(0, n, 2)
        val = fitness(x, fr, n)
        x = list(x)
        x += [val]
        pop += [x]
    return np.asarray(pop)
