import numpy as np


def Akaike(n, k, x, y, params):
    """
    Computes the Akaike Information Criterion (AIC) for the given data.

    Parameters
    ----------
    - n (int): The number of data points in the set.
    - k (int): The number of parameters in the fitted line.
    - x (Numpy array): An array of size n with the x-values of the data set.
    - y (Numpy array): An array of size n with the y-values of the data set.
    - params (Numpy array): An array of size k with the parameters of the fitted
    equation listed from lowest-order to highest-order term.

    Returns
    -------
    - aic (float): The Akaike Information Criterion.
    """

    # Compute the residuals of the sum of the squares first.
    rss = 0
    if k == 2:
        a, b = params
        rss = np.sum((y - (a + (b * x))) ** 2)
    elif k == 3:
        a, b, c = params
        rss = np.sum((y - (a + (b * x) + (c * (x ** 2)))) ** 2)

    # Compute the AIC.
    aic = (n * np.math.log(rss / n)) + (2 * k)

    return aic