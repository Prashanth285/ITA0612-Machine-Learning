# Experiment 10
# Expectation Maximization Algorithm

# Dataset

data = [2, 4, 5, 10, 12, 14]

# Initial Means

mean1 = 3
mean2 = 11

print("Initial Means")
print("Mean 1 =", mean1)
print("Mean 2 =", mean2)

for iteration in range(3):

    cluster1 = []
    cluster2 = []

    # E-Step
    for point in data:

        d1 = abs(point - mean1)
        d2 = abs(point - mean2)

        if d1 < d2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    # M-Step

    mean1 = sum(cluster1) / len(cluster1)
    mean2 = sum(cluster2) / len(cluster2)

    print("\nIteration", iteration + 1)

    print("Cluster 1 =", cluster1)
    print("Cluster 2 =", cluster2)

    print("Updated Mean 1 =", round(mean1, 2))
    print("Updated Mean 2 =", round(mean2, 2))

print("\nFinal Clusters")
print("Cluster 1 =", cluster1)
print("Cluster 2 =", cluster2)
