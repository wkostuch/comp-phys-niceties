import numpy as np
from typing import Callable, Tuple


def step_1(f: Callable[..., float], x: float, y: np.array, params: Tuple,\
    h: float) -> np.array:
    """
    Computes the first step of RK4 for a differential equation with an 
    arbitrary number of derivatives.

    Parameters
    ----------
    - f (function): The equation which RK4 is being used to evaluate.
    - x (float): The x coordinate for which the values are being measured.
    - y (1-d array): A vector of the values of the lower-order derivatives.
    - params (n-tuple): Any additional parameters of f.
    - h (float): The step size of x.

    Returns
    -------
    - y_int (1-d array): The vector of integrated values at position x.
    """

    # Initialize the output vector.
    n = len(y)
    y_int = np.zeros(n)

    # Find dym/dx using the given function, then use it to compute dym-1/dx.
    y_int[0] = f(x, y, *params) * h

    # Starting with dym-1/dx, compute the other values down to y/dx.
    for i in range(1, n):
        y_int[i] = y[n-i] * h

    # Reverse the output vector so y/dx is on top.
    y_int = np.flipud(y_int)

    return y_int


def step_2(f: Callable[..., float], x: float, y: np.array, params: Tuple,\
    h: float, k1: np.array) -> np.array:
    """
    Computes the second step of RK4 for a differential equation with an 
    arbitrary number of derivatives.

    Parameters
    ----------
    - f (function): The equation which RK4 is being used to evaluate.
    - x (float): The x coordinate for which the values are being measured.
    - y (1-d array): A vector of the values of the lower-order derivatives.
    - params (n-tuple): Any additional parameters of f.
    - h (float): The step size of x.
    - k1 (1-d array): A vector containing the values of the previous RK4 step.

    Returns
    -------
    - y (1-d array): The vector of derivative values at position x.
    """

    # Initialize the output vector.
    n = len(y)
    y_int = np.zeros(n)

    # Find dym/dx using the given function, then use it to compute dym-1/dx.
    y_int[0] = f(x + (h / 2), y + (k1 / 2), *params) * h

    # Starting with dym-1/dx, compute the other values down to y/dx.
    for i in range(1, n):
        y_int[i] = (y[n-i] + (k1[n-i] / 2)) * h

    # Reverse the output vector so y/dx is on top.
    y_int = np.flipud(y_int)

    return y_int


def step_3(f: Callable[..., float], x: float, y: np.array, params: Tuple,\
    h: float, k2: np.array) -> np.array:
    """
    Computes the third step of RK4 for a differential equation with an 
    arbitrary number of derivatives.

    Parameters
    ----------
    - f (function): The equation which RK4 is being used to evaluate.
    - x (float): The x coordinate for which the values are being measured.
    - y (1-d array): A vector of the values of the lower-order derivatives.
    - params (n-tuple): Any additional parameters of f.
    - h (float): The step size of x.
    - k2 (1-d array): A vector containing the values of the previous RK4 step.

    Returns
    -------
    - y (1-d array): The vector of derivative values at position x.
    """

    # Initialize the output vector.
    n = len(y)
    y_int = np.zeros(n)

    # Find dym/dx using the given function, then use it to compute dym-1/dx.
    y_int[0] = f(x + (h / 2), y + (k2 / 2), *params) * h

    # Starting with dym-1/dx, compute the other values down to y/dx.
    for i in range(1, n):
        y_int[i] = (y[n-i] + (k2[n-i] / 2)) * h

    # Reverse the output vector so y/dx is on top.
    y_int = np.flipud(y_int)

    return y_int


def step_4(f: Callable[..., float], x: float, y: np.array, params: Tuple,\
    h: float, k3: np.array) -> np.array:
    """
    Computes the fourth step of RK4 for a differential equation with an 
    arbitrary number of derivatives.

    Parameters
    ----------
    - f (function): The equation which RK4 is being used to evaluate.
    - x (float): The x coordinate for which the values are being measured.
    - y (1-d array): A vector of the values of the lower-order derivatives.
    - params (n-tuple): Any additional parameters of f.
    - h (float): The step size of x.
    - k3 (1-d array): A vector containing the values of the previous RK4 step.

    Returns
    -------
    - y (1-d array): The vector of derivative values at position x.
    """

    # Initialize the output vector.
    n = len(y)
    y_int = np.zeros(n)

    # Find dym/dx using the given function, then use it to compute dym-1/dx.
    y_int[0] = f(x + h, y + k3, *params) * h

    # Starting with dym-1/dx, compute the other values down to y/dx.
    for i in range(1, n):
        y_int[i] = (y[n-i] + k3[n-1]) * h

    # Reverse the output vector so y/dx is on top.
    y_int = np.flipud(y_int)

    return y_int


def Runge_Kutta_4(diff_fun: Callable[..., float],\
    x_range: Tuple[float, float, float], initial_value: np.array,\
    params: Tuple) -> Tuple[np.array, np.array]:
    """
    Uses the 4th-order Runge-Kutta algorithm to numerically integrate an 
    arbitrary differential function.

    Parameters
    ----------
    - diff_fun (function): A function of the form f(x, Y, *args) that returns 
    the value of the highest-order derivative, where x is a float passed to the 
    y function and derivatives as y(x), and Y is a vector of values of y(x) and
    any derivatives before that which f(x, Y, *args) returns.
    - x_range (3-tuple): A tuple of the form (min, max, step) for the values 
    over which x will be evaluated.
    - initial_value (1-d array): An array representing a vector of the initial 
    values for the function and its derivatives.
    - params (n-tuple): A tuple of any additional parameters for diff_fun.

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
        k1 = step_1(diff_fun, x[n-1], y[n-1], params, dx)
        k2 = step_2(diff_fun, x[n-1], y[n-1], params, dx, k1)
        k3 = step_3(diff_fun, x[n-1], y[n-1], params, dx, k2)
        k4 = step_4(diff_fun, x[n-1], y[n-1], params, dx, k3)
        y[n] = y[n-1] + ((k1 + (2 * k2) + (2 * k3) + k4) / 6)

    return x, y
