# Experiment 11
# Credit Score Classification

# Sample Customer Data

customers = [
    ("Ravi", 450),
    ("Priya", 620),
    ("Arun", 780),
    ("Kiran", 510),
    ("Meena", 820)
]

print("Customer Credit Classification")
print("--------------------------------")

for customer in customers:

    name = customer[0]
    score = customer[1]

    if score < 500:
        category = "Poor"

    elif score < 750:
        category = "Average"

    else:
        category = "Good"

    print("Name =", name)
    print("Credit Score =", score)
    print("Category =", category)
    print()

# Testing New Customer

new_score = int(input("Enter Credit Score: "))

if new_score < 500:
    result = "Poor"

elif new_score < 750:
    result = "Average"

else:
    result = "Good"

print("Credit Rating =", result)
