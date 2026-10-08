# Experiment 20
# Future Sales Prediction

# Historical Sales Data

months = [1, 2, 3, 4, 5]
sales = [100, 120, 140, 160, 180]

n = len(months)

# Calculate Mean

mean_x = sum(months) / n
mean_y = sum(sales) / n

# Calculate Slope

numerator = 0
denominator = 0

for i in range(n):

    numerator += (months[i] - mean_x) * (sales[i] - mean_y)

    denominator += (months[i] - mean_x) ** 2

m = numerator / denominator

# Calculate Intercept

c = mean_y - m * mean_x

print("Slope =", round(m, 2))
print("Intercept =", round(c, 2))

# Predict Future Month

future_month = int(input("\nEnter Future Month Number: "))

predicted_sales = m * future_month + c

print("\nPredicted Sales =",
      round(predicted_sales, 2))
