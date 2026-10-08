# Experiment 6
# Naive Bayes Classification

# Training Data

data = [
    ("Sunny", "Hot", "No"),
    ("Sunny", "Cool", "No"),
    ("Rainy", "Cool", "Yes"),
    ("Rainy", "Hot", "Yes"),
    ("Sunny", "Hot", "No"),
    ("Rainy", "Cool", "Yes")
]

# Test Sample
test_weather = "Rainy"
test_temp = "Cool"

# Count Classes
yes_count = 0
no_count = 0

for row in data:
    if row[2] == "Yes":
        yes_count += 1
    else:
        no_count += 1

total = len(data)

# Prior Probabilities

p_yes = yes_count / total
p_no = no_count / total

# Conditional Probabilities

rainy_yes = 0
cool_yes = 0

rainy_no = 0
cool_no = 0

for row in data:

    weather = row[0]
    temp = row[1]
    decision = row[2]

    if decision == "Yes":

        if weather == "Rainy":
            rainy_yes += 1

        if temp == "Cool":
            cool_yes += 1

    else:

        if weather == "Rainy":
            rainy_no += 1

        if temp == "Cool":
            cool_no += 1

# Likelihood

p_rainy_yes = rainy_yes / yes_count
p_cool_yes = cool_yes / yes_count

p_rainy_no = rainy_no / no_count
p_cool_no = cool_no / no_count

# Naive Bayes Formula

prob_yes = p_yes * p_rainy_yes * p_cool_yes
prob_no = p_no * p_rainy_no * p_cool_no

print("Probability of YES =", prob_yes)
print("Probability of NO =", prob_no)

# Prediction

if prob_yes > prob_no:
    prediction = "Yes"
else:
    prediction = "No"

print("\nPrediction =", prediction)

# Confusion Matrix Example

actual = ["Yes","No","Yes","No","Yes","Yes"]
predicted = ["Yes","No","Yes","No","No","Yes"]

TP = TN = FP = FN = 0

for i in range(len(actual)):

    if actual[i] == "Yes" and predicted[i] == "Yes":
        TP += 1

    elif actual[i] == "No" and predicted[i] == "No":
        TN += 1

    elif actual[i] == "No" and predicted[i] == "Yes":
        FP += 1

    elif actual[i] == "Yes" and predicted[i] == "No":
        FN += 1

print("\nConfusion Matrix")
print("----------------")
print("TP =", TP)
print("TN =", TN)
print("FP =", FP)
print("FN =", FN)

accuracy = ((TP + TN) / len(actual)) * 100

print("\nAccuracy =", accuracy, "%")
