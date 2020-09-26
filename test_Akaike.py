from Akaike import Akaike
import numpy as np
from scipy.optimize import curve_fit
import unittest


class TestAkaike(unittest.TestCase):

    def test_linear(self):
        # Get some example data.
        data = np.loadtxt('CSIRO_Recons_gmsl_mo_2011.txt', skiprows=1)
        x, y = np.array(data[:, 0]), np.array(data[:, 1])
        n = len(x)

        # Do a test fit to check the output of the Akaike function.
        def test(x, a, b, c):
            return (a * np.sin(b * x)) + (c * np.cos(b * x))

        # Initial guess values.
        p0 = [1.0E-4, 1.0E-2, 1.0E-4]
        params, param_cov = curve_fit(test, x, y, p0)
        k = len(params)

        test_aic = Akaike(n, k, x, y, params)
        # Not sure if this test is correct.
        self.assertAlmostEqual(test_aic, 52080, places=0)


    def test_quadratic(self):
        # Get some example data.
        test_data = np.loadtxt('CSIRO_Recons_gmsl_mo_2011.txt', skiprows=1)
        x, y = np.array(test_data[:, 0]), np.array(test_data[:, 1])
        n = len(x)

        # Do a sample fit to test the Akaike.
        def test(x, a, b, c):
            return a + (b * x) + (c * (x ** 2))

        p0 = [-150, 1.5, 1.0]
        params, param_cov = curve_fit(test, x, y, p0)
        k = len(params)

        test_aic = Akaike(n, k, x, y, params)
        self.assertAlmostEqual(test_aic, 6305, places=0)


if __name__ == "__main__":
    unittest.main()