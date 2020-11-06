import numpy as np
from typing import Callable, Tuple


def step_1(f: Callable[..., float], x: float, y: np.array, h: float)\
    -> np.array:
    """
    Computes the first step of RK4 for a differential equation with an 
    arbitrary number of derivatives.

    Parameters
    ----------
    - f (function): The equation which RK4 is being used to evaluate.
    - x (float): The x coordinate for which the values are being measured.
    - y (1-d array): A vector of the values of the lower-order derivatives.
    - h (float): The step size of x.

    Returns
    -------
    - y (1-d array): The vector of derivative values at position x.
    """

    n = len(y)
    y[n-1] = f(x, y) * h

    for i in range(2, n):
        y[n-i] = y[n-i+1] * h

    return y


def step_2(f: Callable[..., float], x: float, y: np.array, h: float,\
    k1: np.array) -> np.array:
    """
    Computes the second step of RK4 for a differential equation with an 
    arbitrary number of derivatives.

    Parameters
    ----------
    - f (function): The equation which RK4 is being used to evaluate.
    - x (float): The x coordinate for which the values are being measured.
    - y (1-d array): A vector of the values of the lower-order derivatives.
    - h (float): The step size of x.
    - k1 (1-d array): A vector containing the values of the previous RK4 step.

    Returns
    -------
    - y (1-d array): The vector of derivative values at position x.
    """

    n = len(y)
    y[n-1] = f(x + (h / 2), y + (k1 / 2)) * h

    for i in range(2, n):
        y[n-i] = (y[n-i+1] + (k1 / 2)) * h

    return y


def step_3(f: Callable[..., float], x: float, y: np.array, h: float,\
    k2: np.array) -> np.array:
    """
    Computes the third step of RK4 for a differential equation with an 
    arbitrary number of derivatives.

    Parameters
    ----------
    - f (function): The equation which RK4 is being used to evaluate.
    - x (float): The x coordinate for which the values are being measured.
    - y (1-d array): A vector of the values of the lower-order derivatives.
    - h (float): The step size of x.
    - k2 (1-d array): A vector containing the values of the previous RK4 step.

    Returns
    -------
    - y (1-d array): The vector of derivative values at position x.
    """

    n = len(y)
    y[n-1] = f(x + (h / 2), y + (k2 / 2)) * h

    for i in range(2, n):
        y[n-i] = (y[n-i+1] + (k2 / 2)) * h

    return y


def step_4(f: Callable[..., float], x: float, y: np.array, h: float,\
    k3: np.array) -> np.array:
    """
    Computes the fourth step of RK4 for a differential equation with an 
    arbitrary number of derivatives.

    Parameters
    ----------
    - f (function): The equation which RK4 is being used to evaluate.
    - x (float): The x coordinate for which the values are being measured.
    - y (1-d array): A vector of the values of the lower-order derivatives.
    - h (float): The step size of x.
    - k3 (1-d array): A vector containing the values of the previous RK4 step.

    Returns
    -------
    - y (1-d array): The vector of derivative values at position x.
    """

    n = len(y)
    y[n-1] = f(x + h, y + k3) * h

    for i in range(2, n):
        y[n-i] = (y[n-i+1] + k3) * h

    return y


def Runge_Kutta_4(diff_fun: Callable[..., float],\
    x_range: Tuple[float, float, float], initial_value: np.array)\
    -> Tuple[np.array, np.array]:
    """
    Uses the 4th-order Runge-Kutta algorithm to numerically integrate an 
    arbitrary differential function.

    Parameters
    ----------
    - diff_fun (function): A function of the form f(x, Y) that returns the 
    value of the highest-order derivative, where x is a float passed to the y
    function and derivatives as y(x), and Y is a vector of values of y(x) and
    any derivatives before that which f(x, Y) returns.
    - x_range (3-tuple): A tuple of the form (min, max, step) for the values 
    over which x will be evaluated.
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
    for n in range(1, num_steps):
        k1 = step_1(diff_fun, x[n-1], y[n-1], dx)
        k2 = step_2(diff_fun, x[n-1], y[n-1], dx, k1)
        k3 = step_3(diff_fun, x[n-1], y[n-1], dx, k2)
        k4 = step_4(diff_fun, x[n-1], y[n-1], dx, k3)
        y[n] = y[n-1] + ((k1 + (2 * k2) + (2 * k3) + k4) / 6)

    return x, y
