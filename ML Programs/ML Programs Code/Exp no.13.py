# Experiment 13
# Car Price Prediction

# Training Data

car_age = [1, 2, 3, 4, 5]
car_price = [900000, 800000, 700000, 600000, 500000]

n = len(car_age)

# Mean

mean_x = sum(car_age) / n
mean_y = sum(car_price) / n

# Find slope

numerator = 0
denominator = 0

for i in range(n):

    numerator += ((car_age[i] - mean_x) *
                  (car_price[i] - mean_y))

    denominator += (car_age[i] - mean_x) ** 2

m = numerator / denominator

# Intercept

c = mean_y - m * mean_x

print("Slope =", m)
print("Intercept =", c)

# Test Data

test_age = int(input("\nEnter Car Age: "))

predicted_price = m * test_age + c

print("\nPredicted Car Price = Rs.",
      round(predicted_price, 2))
