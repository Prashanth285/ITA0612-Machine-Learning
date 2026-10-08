# Experiment 17
# Mobile Price Prediction

# Mobile Dataset

mobiles = [
    [4, 64, "Budget"],
    [6, 128, "Mid-Range"],
    [8, 128, "Premium"],
    [12, 256, "Premium"],
    [4, 128, "Mid-Range"]
]

print("Mobile Dataset")
print("----------------")

for mobile in mobiles:
    print(mobile)

# Input from user

ram = int(input("\nEnter RAM (GB): "))
storage = int(input("Enter Storage (GB): "))

# Prediction Logic

if ram >= 8 and storage >= 128:
    category = "Premium"

elif ram >= 4 and storage >= 64:
    category = "Mid-Range"

else:
    category = "Budget"

print("\nPredicted Mobile Category =", category)
