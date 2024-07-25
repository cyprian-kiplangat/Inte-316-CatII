# Define the function to integrate
def f(x):
	return x**2

# Define the limits of integration
a = 0  # Lower limit
b = 1  # Upper limit

# Define the number of subintervals
n = 4

# Calculate the width of each subinterval
h = (b - a) / n

# Initialize the sum of trapezoidal areas
area = 0

# Iterate through the subintervals
for i in range(n):
	# Calculate the x values at the endpoints of the subinterval
	x0 = a + i * h
	x1 = a + (i + 1) * h

	# Calculate the area of the trapezoid
	area += (f(x0) + f(x1)) * h / 2

# Print the result
print(f"The approximate area under the curve from {a} to {b} is: {area}")