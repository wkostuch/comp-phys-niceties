import numpy as np
from typing import Callable, Tuple


def Runge_Kutta_4(diff_fun: Callable[..., float],\
    x_range: Tuple[float, float, float], initial_value: np.array)\
    -> Tuple[np.array, np.array]:
    """
    Uses the 4th-order Runge-Kutta algorithm to numerically integrate an 
    arbitrary differential function.

    Parameters
    ----------
    - diff_fun (function): A function of the form f(x, Y) that returns a vector 
    of the form [dy1/dx, dy2/dx, ..., dym/dx], where t is a float passed the y 
    function and derivatives as y(t), and Y is a vector of the same form as the 
    function output.
    - x_range (3-tuple): A tuple of the form (min, max, step) for the values 
    over which t will be evaluated.
    - initial_value (1-d array): An array representing a vector of the initial 
    values for the function and its derivatives.

    Returns
    -------
    - x (1-d array): The t values over the given range.
    - y (2-d array): A matrix of containing the values of the input vector for 
    each t value.
    """

    # Extract the time step for ease of use and readability.
    dx = x_range[2]
    # Get the size of the parameter vector.
    vec_size = len(initial_value)
    # Initialize the output arrays.
    x = np.arange(x_range[0], x_range[1] + dx, dx)
    num_steps = len(x)
    y = np.array([np.zeros(vec_size) for i in range(num_steps)])
    y[0] = initial_value

    # Numerically compute the differential equation's parameters over the given 
    # range.
    for n in range(0, num_steps):
        k1 = diff_fun(x[n-1], y[n-1]) * dx
        k2 = diff_fun(x[n-1] + (dx / 2), y[n-1] + (k1 / 2)) * dx
        k3 = diff_fun(x[n-1] + (dx / 2), y[n-1] + (k2 / 2)) * dx
        k4 = diff_fun(x[n-1], y[n-1] + k3) * dx
        y[n] = y[n-1] + ((k1 + (2 * k2) + (2 * k3) + k4) / 6)

    return x, y