# Experiment 9
# Linear Regression vs Polynomial Regression

# Dataset

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# -------------------------------------------------
# Linear Regression
# -------------------------------------------------

n = len(x)

mean_x = sum(x) / n
mean_y = sum(y) / n

numerator = 0
denominator = 0

for i in range(n):
    numerator += (x[i] - mean_x) * (y[i] - mean_y)
    denominator += (x[i] - mean_x) ** 2

m = numerator / denominator
c = mean_y - m * mean_x

test_x = 6

linear_prediction = m * test_x + c

# -------------------------------------------------
# Polynomial Regression (Degree 2)
# -------------------------------------------------

# Since the dataset follows Y = X²

polynomial_prediction = test_x ** 2

# -------------------------------------------------
# Output
# -------------------------------------------------

print("Dataset")

for i in range(n):
    print(x[i], "->", y[i])

print("\nLinear Regression Prediction")
print("For X =", test_x)
print("Predicted Y =", linear_prediction)

print("\nPolynomial Regression Prediction")
print("For X =", test_x)
print("Predicted Y =", polynomial_prediction)
