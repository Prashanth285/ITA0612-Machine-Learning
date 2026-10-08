# Experiment 12
# Iris Flower Classification using KNN

import math

# Sample Iris Dataset
# [Sepal Length, Sepal Width]

dataset = [
    ([5.1, 3.5], "Setosa"),
    ([4.9, 3.0], "Setosa"),
    ([6.0, 2.9], "Versicolor"),
    ([6.1, 2.8], "Versicolor"),
    ([7.2, 3.0], "Virginica"),
    ([7.4, 2.8], "Virginica")
]

# New Flower Data

test_flower = [6.2, 2.9]

k = 3

distances = []

# Calculate Euclidean Distance

for item in dataset:

    flower = item[0]
    species = item[1]

    distance = math.sqrt(
        (flower[0] - test_flower[0])**2 +
        (flower[1] - test_flower[1])**2
    )

    distances.append((distance, species))

# Sort by Distance

distances.sort()

# Select K Nearest Neighbours

neighbors = distances[:k]

# Count Species

setosa = 0
versicolor = 0
virginica = 0

for neighbor in neighbors:

    if neighbor[1] == "Setosa":
        setosa += 1

    elif neighbor[1] == "Versicolor":
        versicolor += 1

    else:
        virginica += 1

# Prediction

if setosa > versicolor and setosa > virginica:
    prediction = "Setosa"

elif versicolor > virginica:
    prediction = "Versicolor"

else:
    prediction = "Virginica"

# Output

print("Test Flower =", test_flower)

print("\nNearest Neighbours")

for n in neighbors:
    print(n)

print("\nPredicted Species =", prediction)
