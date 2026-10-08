# Experiment 19
# Bank Loan Prediction using Naive Bayes

# Training Dataset

customers = [
    ["High", "Good", "Approved"],
    ["High", "Bad", "Rejected"],
    ["Low", "Good", "Approved"],
    ["Low", "Bad", "Rejected"],
    ["High", "Good", "Approved"]
]

print("Training Data")
print("-------------")

for row in customers:
    print(row)

# Test Customer

income = input("\nEnter Income (High/Low): ")
credit = input("Enter Credit History (Good/Bad): ")

# Naive Bayes Style Decision

approved = 0
rejected = 0

for row in customers:

    if row[0] == income and row[1] == credit:

        if row[2] == "Approved":
            approved += 1
        else:
            rejected += 1

# Prediction

if approved >= rejected:
    result = "Loan Approved"
else:
    result = "Loan Rejected"

print("\nResult =", result)
