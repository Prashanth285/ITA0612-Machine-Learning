# Experiment 5
# K-Nearest Neighbour Algorithm

import math

# Training Data
dataset = [
    ([1, 2], "Class A"),
    ([2, 3], "Class A"),
    ([3, 3], "Class A"),
    ([6, 5], "Class B"),
    ([7, 7], "Class B"),
    ([8, 6], "Class B")
]

# Test Sample
test_point = [5, 5]

k = 3

distances = []

# Calculate Euclidean Distance
for data in dataset:

    point = data[0]
    label = data[1]

    distance = math.sqrt(
        (point[0] - test_point[0]) ** 2 +
        (point[1] - test_point[1]) ** 2
    )

    distances.append((distance, label))

# Sort Distances
distances.sort()

# Select K Nearest Neighbours
neighbors = distances[:k]

# Count Classes
countA = 0
countB = 0

for neighbor in neighbors:

    if neighbor[1] == "Class A":
        countA += 1
    else:
        countB += 1

# Prediction
if countA > countB:
    prediction = "Class A"
else:
    prediction = "Class B"

# Output

print("Test Point =", test_point)

print("\nNearest Neighbours:")

for neighbor in neighbors:
    print(neighbor)

print("\nPredicted Class =", prediction)
