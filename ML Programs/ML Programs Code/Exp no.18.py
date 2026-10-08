# Experiment 18
# Perceptron Based Iris Classification

# Sample Iris Dataset

flowers = [
    [5.1, "Setosa"],
    [4.9, "Setosa"],
    [6.0, "Versicolor"],
    [6.2, "Versicolor"],
    [7.1, "Virginica"],
    [7.3, "Virginica"]
]

print("Iris Dataset")
print("------------")

for flower in flowers:
    print(flower)

# Perceptron Parameters

weight = 1
bias = -5.5

# Activation Function

def activation(value):
    if value >= 0:
        return 1
    else:
        return 0

# Test Sample

sepal_length = float(input("\nEnter Sepal Length: "))

net = sepal_length * weight + bias

output = activation(net)

# Classification

if sepal_length < 5.5:
    prediction = "Setosa"

elif sepal_length < 6.5:
    prediction = "Versicolor"

else:
    prediction = "Virginica"

print("\nNet Value =", round(net, 2))
print("Perceptron Output =", output)
print("Predicted Species =", prediction)
