# Experiment 4
# Artificial Neural Network using Backpropagation

# Training Data (AND Gate)

training_data = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1)
]

# Initial Weights and Bias
w1 = 0.1
w2 = 0.1
bias = 0.1

learning_rate = 0.1

# Activation Function
def activation(x):
    if x >= 0:
        return 1
    else:
        return 0

# Training
for epoch in range(20):

    total_error = 0

    for inputs, target in training_data:

        x1 = inputs[0]
        x2 = inputs[1]

        net = x1*w1 + x2*w2 + bias

        output = activation(net)

        error = target - output

        total_error += abs(error)

        # Weight Update
        w1 = w1 + learning_rate * error * x1
        w2 = w2 + learning_rate * error * x2
        bias = bias + learning_rate * error

    print("Epoch", epoch + 1, "Error =", total_error)

# Testing

print("\nFinal Weights")
print("w1 =", round(w1, 2))
print("w2 =", round(w2, 2))
print("Bias =", round(bias, 2))

print("\nTesting Network")

for inputs, target in training_data:

    x1 = inputs[0]
    x2 = inputs[1]

    net = x1*w1 + x2*w2 + bias

    output = activation(net)

    print(inputs, "Predicted =", output,
          "Actual =", target)
