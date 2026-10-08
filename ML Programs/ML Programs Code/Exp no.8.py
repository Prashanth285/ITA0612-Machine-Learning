# Experiment 8
# Linear Regression

# Training Data

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

n = len(x)

# Calculate Mean

mean_x = sum(x) / n
mean_y = sum(y) / n

# Calculate Slope (m)

numerator = 0
denominator = 0

for i in range(n):
    numerator += (x[i] - mean_x) * (y[i] - mean_y)
    denominator += (x[i] - mean_x) ** 2

m = numerator / denominator

# Calculate Intercept (c)

c = mean_y - m * mean_x

print("Slope (m) =", m)
print("Intercept (c) =", c)

# Prediction

test_x = 6

predicted_y = m * test_x + c

print("\nTest Input =", test_x)
print("Predicted Output =", predicted_y)
