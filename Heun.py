import numpy as np
from typing import Callable, Tuple


def Heun(func: Callable[..., float], params: Tuple,\
    frange: Tuple[float, float, float], y0: float)\
    -> Tuple[np.ndarray, np.ndarray]:
    """
    A generic implementation of Heun's method for finding the antiderivative of 
    a given function.

    Parameters
    ----------
    - func (function): A function of the form func(x, y, *args, **kwargs).
    - params (n-tuple): Any additional parameters other than x and y for func. 
    Elements should be in the order the parameters are passed to func.
    - frange (3-tuple): The range of x values to be passed into func in the 
    form (min, max, step).
    - y0 (float): The value of y at the minimum value of x given in frange.

    Returns
    -------
    - x (ndarray): The x values of the antiderivative over the given range.
    - y (ndarray): The y values of the antiderivative over the given range.
    """

    # Unpack the range tuple into useable values. Don't unpack params here, 
    # because it is of arbitrary size.
    x_min, x_max, step = frange

    x: np.ndarray[float] = np.arange(x_min, x_max, step)
    n: int = len(x)
    y: np.ndarray[float] = np.zeros(n)
    y[0] = y0

    # Fill out the arrays using Heun's method to refine the estimate given by 
    # Euler's method.
    for i in range(1, n):
        y_euler = y[i-1] + (func(x[i-1], y[i-1], *params) * step)
        y[i] = y[i-1] + ((1 / 2) * (func(x[i-1], y[i-1], *params)\
            + func(x[i], y_euler, *params)) * step)

    return x, y