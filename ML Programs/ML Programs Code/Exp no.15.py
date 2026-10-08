# Experiment 15
# Iris Flower Classification using Naive Bayes

# Sample Iris Dataset

flowers = [
    ([5.1, 3.5], "Setosa"),
    ([4.9, 3.0], "Setosa"),
    ([6.0, 2.9], "Versicolor"),
    ([6.1, 2.8], "Versicolor"),
    ([7.0, 3.2], "Virginica"),
    ([7.3, 2.9], "Virginica")
]

# Test Flower

test_sepal_length = 6.2
test_sepal_width = 2.9

# Classification Rule

if test_sepal_length < 5.5:
    prediction = "Setosa"

elif test_sepal_length < 6.5:
    prediction = "Versicolor"

else:
    prediction = "Virginica"

# Display Dataset

print("Training Dataset")
print("-----------------")

for flower in flowers:
    print(flower)

# Testing

print("\nTest Flower")
print("Sepal Length =", test_sepal_length)
print("Sepal Width =", test_sepal_width)

print("\nPredicted Class =", prediction)
