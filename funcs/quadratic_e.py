import numpy as np


def qe(a, b, c):
    D = b**2 - 4*a*c
    if D >= 0:
        root1 = (b + np.sqrt(D))/2*a
        root2 = (b - np.sqrt(D))/2*a
        return (root1, root2, D)
    return ("D is smaller than 0", "\n", D)
