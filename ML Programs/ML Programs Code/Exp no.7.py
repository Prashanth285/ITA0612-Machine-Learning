# Experiment 7
# Logistic Regression (Simple Demonstration)

import math

# Dataset
hours_studied = [1, 2, 3, 4, 5, 6]

# Pass = 1
# Fail = 0

result = [0, 0, 0, 1, 1, 1]

# Simple Weight and Bias

weight = 1
bias = -3.5

# Sigmoid Function

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

print("Training Data")

for i in range(len(hours_studied)):

    x = hours_studied[i]

    z = weight * x + bias

    probability = sigmoid(z)

    prediction = 1 if probability >= 0.5 else 0

    print("Hours =", x,
          "Probability =", round(probability, 4),
          "Prediction =", prediction)

# Testing New Sample

test_hours = 5

z = weight * test_hours + bias

probability = sigmoid(z)

prediction = 1 if probability >= 0.5 else 0

print("\nTest Hours =", test_hours)

print("Probability =", round(probability, 4))

if prediction == 1:
    print("Result = Pass")
else:
    print("Result = Fail")
