import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    """
    Generates a unit step signal.
    u[n] = 1 for n >= 0, else 0
    """
    u = np.where(n >= 0, 1, 0)
    plt.stem(n, u, basefmt=" ")
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("u[n]")
    plt.grid(True)
    plt.show()
    return u

def unit_impulse(n):
    """
    Generates a unit impulse signal.
    δ[n] = 1 at n = 0, else 0
    """
    delta = np.where(n == 0, 1, 0)
    plt.stem(n, delta, basefmt=" ")
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("δ[n]")
    plt.grid(True)
    plt.show()
    return delta

def ramp_signal(n):
    """
    Generates a ramp signal.
    r[n] = n for n >= 0, else 0
    """
    r = np.where(n >= 0, n, 0)
    plt.stem(n, r, basefmt=" ")
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("r[n]")
    plt.grid(True)
    plt.show()
    return r
