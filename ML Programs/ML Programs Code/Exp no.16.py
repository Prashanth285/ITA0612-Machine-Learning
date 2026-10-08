# Experiment 16
# Comparison of Classification Algorithms

actual = [
    "Yes",
    "No",
    "Yes",
    "Yes",
    "No",
    "Yes"
]

knn_pred = [
    "Yes",
    "No",
    "Yes",
    "No",
    "No",
    "Yes"
]

nb_pred = [
    "Yes",
    "No",
    "Yes",
    "Yes",
    "No",
    "No"
]

dt_pred = [
    "Yes",
    "No",
    "Yes",
    "Yes",
    "No",
    "Yes"
]

def accuracy(actual, predicted):

    correct = 0

    for i in range(len(actual)):

        if actual[i] == predicted[i]:
            correct += 1

    return (correct / len(actual)) * 100
knn_accuracy = accuracy(actual, knn_pred)
nb_accuracy = accuracy(actual, nb_pred)
dt_accuracy = accuracy(actual, dt_pred)

print("Classification Algorithm Comparison")
print("------------------------------------")

print("KNN Accuracy =", knn_accuracy, "%")
print("Naive Bayes Accuracy =", nb_accuracy, "%")
print("Decision Tree Accuracy =", dt_accuracy, "%")

best_accuracy = max(
    knn_accuracy,
    nb_accuracy,
    dt_accuracy
)

if best_accuracy == knn_accuracy:
    best = "KNN"
elif best_accuracy == nb_accuracy:
    best = "Naive Bayes"
else:
    best = "Decision Tree"

print("\nBest Classifier =", best)
