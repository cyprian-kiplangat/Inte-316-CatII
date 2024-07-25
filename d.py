import math

# Define the function f(x)
def f(x):
    return x**3 - 0.165*x**2 + 3.993e-4

# Define the derivative of f(x)
def f_prime(x):
    return 3*x**2 - 2*0.165*x

# Initial guess for the root
x0 = 0.055

# Number of iterations
num_iterations = 3

# List to store the estimates of the root at each iteration
x_values = [x0]

# List to store the absolute relative approximate error at each iteration
error_values = []

# Newton's method iterations
for i in range(num_iterations):
    x_n = x_values[i]
    x_n_plus_1 = x_n - f(x_n) / f_prime(x_n)
    x_values.append(x_n_plus_1)

    # Calculate the absolute relative approximate error
    error = abs((x_n_plus_1 - x_n) / x_n_plus_1) * 100
    error_values.append(error)

# Print the results
for i in range(num_iterations):
    print(f"Iteration {i+1}:")
    print(f"  Estimate of the root: {x_values[i+1]:.6f} meters")
    print(f"  Absolute relative approximate error: {error_values[i]:.6f}%")
