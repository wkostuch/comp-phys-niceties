# Monte Carlo simulation from class

import numpy as np
import matplotlib.pyplot as plt

# Linear regression/least squares method from class, used in Monte Carlo
def least_squares(x: list, y: list):
    """Calculates the least squares regression for the x and y data.
        Returns a tuple of (A, sigma_A, B, sigma_B)."""
    # Initialize some variables
    N = len(x)
    #y_uncertainty = np.std(y)
    
    # Perform the sums
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.inner(x,x) # Dot product for the arrays
    sum_xy = np.inner(x, y) 

    # Now calculate the coefficients
    delta = (N * sum_xx) - sum_x**2
    A = (sum_xx * sum_y  -  sum_x * sum_xy) / delta
    B = (N * sum_xy  -  sum_x * sum_y) / delta
    sigma_A = np.sqrt(sum((y-(A+B*x))**2/(N-2)))*np.sqrt(sum_xx/delta)
    sigma_B = np.sqrt(sum((y-(A+B*x))**2/(N-2)))*np.sqrt(N/delta)

    return (A, sigma_A, B, sigma_B)




# Our data for this example
data = np.loadtxt("Global_O2_Concentration_2010_2020.txt", skiprows=1, usecols=(2, 3, 4))
x = data[:,0]
y = data[:,1]
sig_y = data[:,2]

coefficients = least_squares(x, y)
A, sigma_A, B, sigma_B = coefficients


# Another way to see what's going on with the data: Monte Carlo (random variation)

# How many times to roll the dice in the estimation
number_of_trials = 1000
# Some other variables
array_fit_parameters = np.array([])
# Create arrays for values of A, B, and their uncertainties 
A_values = np.zeros(number_of_trials)
B_values = np.zeros(number_of_trials)
sigma_A = np.zeros(number_of_trials) # A and B uncertainty
sigma_B = np.zeros(number_of_trials)
N = x.size
y_error = np.sqrt(sum((y-(A+B*x))**2)/(N-2))
x_min = x[0]
x_max = x[-1]


# Create our random data
# Crux of the Monte Carlo method: making new values in the range of our values, uniformely random
for j in range(number_of_trials):
    x_trial = np.random.uniform(x_min, x_max, size=N) # Uniform random distribution for x values
    y_trial = A + B*x_trial + np.random.normal(loc=0, scale=y_error, size=N) # Add some randomness to our y data, still fit it though
    A_values[j], sigma_A[j], B_values[j], sigma_B[j] = least_squares(x_trial, y_trial)
plt.hist(A_values, bins=50) # Distribution of A values
plt.title("Distribution of A values from Monte Carlo simulation")
plt.show()

# Average the values created via Monte Carlo methods and print them out
A = np.mean(A_values)
B = np.mean(B_values)
sigma_A = np.mean(sigma_A)
sigma_B = np.mean(sigma_B)
print("The best straight line fit is y = ({0:4.2e} +/- {1:4.2e} +/- ({2:4.2e} +/- {3:4.2e})x)".format(A, sigma_A, B, sigma_B))




######################
# Very nice way to set up graphs vs each other
# multiaxis histogram for Monte Carlo stuff
fig = plt.figure(figsize=(6, 6))
fig.suptitle('Monte Carlo Estimation of Parameters')
grid = plt.GridSpec(4, 4, hspace=0.4, wspace=0.5)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# scatter points on the main axes
main_ax.plot(A_values, B_values , 'ok', markersize=2, alpha=0.2)

# histogram on the attached axes
x_hist.hist(A_values, 50, histtype='stepfilled',
orientation='vertical', color='blue')
x_hist.invert_yaxis()
y_hist.hist(B_values, 50, histtype='stepfilled',
orientation='horizontal', color='red')
y_hist.invert_xaxis()

plt.show()