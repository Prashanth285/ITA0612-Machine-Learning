print("=" * 60)
print("EXPERIMENT 1 - FIND-S ALGORITHM")
print("=" * 60)

# Training data
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "No"],
    ["Sunny", "Warm", "High", "Strong", "Yes"]
]

attributes = ["Sky", "AirTemp", "Humidity", "Wind"]

print("\nTraining Data:")
print("-" * 60)

print("Sky\tAirTemp\tHumidity\tWind\tPlay")

for row in data:
    print(
        row[0], "\t",
        row[1], "\t",
        row[2], "\t",
        row[3], "\t",
        row[4]
    )

# Initial hypothesis
hypothesis = ["0", "0", "0", "0"]

# FIND-S Algorithm
for row in data:

    # Consider only positive examples
    if row[4] == "Yes":

        example = row[:4]

        # First positive example
        if hypothesis == ["0", "0", "0", "0"]:
            hypothesis = example.copy()

        else:
            # Generalize hypothesis
            for i in range(len(hypothesis)):

                if hypothesis[i] != example[i]:
                    hypothesis[i] = "?"

# Display result
print("\n" + "-" * 60)

print("Attributes:")
print(attributes)

print("\nMost Specific Hypothesis:")
print(hypothesis)

print("\nFinal Result:")
print(
    "The most specific hypothesis is:",
    hypothesis
)

print("\nFIND-S algorithm executed successfully!")
