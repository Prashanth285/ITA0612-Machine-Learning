# Experiment 14
# House Price Prediction

# Training Data

area = [1000, 1200, 1500, 1800, 2000]
price = [20, 24, 30, 36, 40]   # Price in Lakhs

n = len(area)

# Mean

mean_x = sum(area) / n
mean_y = sum(price) / n

# Calculate Slope

numerator = 0
denominator = 0

for i in range(n):

    numerator += (area[i] - mean_x) * (price[i] - mean_y)

    denominator += (area[i] - mean_x) ** 2

m = numerator / denominator

# Calculate Intercept

c = mean_y - (m * mean_x)

print("Slope =", round(m, 4))
print("Intercept =", round(c, 4))

# Test Data

test_area = int(input("\nEnter House Area (sq.ft): "))

predicted_price = (m * test_area) + c

print("\nPredicted House Price =",
      round(predicted_price, 2),
      "Lakhs")
