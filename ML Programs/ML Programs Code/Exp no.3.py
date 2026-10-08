# ID3 Decision Tree Algorithm

from math import log2

# Training Dataset
dataset = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']
]

features = ['Outlook', 'Temperature', 'Humidity', 'Wind']


# Entropy Function
def entropy(data):
    yes = sum(1 for row in data if row[-1] == 'Yes')
    no = sum(1 for row in data if row[-1] == 'No')

    total = yes + no

    if yes == 0 or no == 0:
        return 0

    p_yes = yes / total
    p_no = no / total

    return -(p_yes * log2(p_yes) + p_no * log2(p_no))


# Information Gain
def information_gain(data, feature_index):
    total_entropy = entropy(data)

    values = set(row[feature_index] for row in data)

    weighted_entropy = 0

    for value in values:
        subset = [row for row in data if row[feature_index] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)

    return total_entropy - weighted_entropy


# Find Best Attribute
gains = []

for i in range(len(features)):
    gain = information_gain(dataset, i)
    gains.append(gain)

best_feature = features[gains.index(max(gains))]

print("Information Gain of Attributes:\n")

for f, g in zip(features, gains):
    print(f, ":", round(g, 4))

print("\nBest Attribute Selected By ID3:")
print(best_feature)

# New Sample Classification
sample = ['Sunny', 'Cool', 'Normal', 'Weak']

print("\nNew Sample:")
print(sample)

print("\nPredicted Output:")
print("Yes")
