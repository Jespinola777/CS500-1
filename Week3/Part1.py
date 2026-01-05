# Module 3 - Part 1

# This program calculates the total cost of a meal including tax and tip.
meal_cost = float(input("How much was the meal you purchased? $"))

# Calculate tip and tax and round to 2 decimal places
meal_tip = round(meal_cost * 0.18, 2)
meal_tax = round(meal_cost * 0.07, 2)

# Calculate total cost and round to 2 decimal places
total_cost = round(meal_cost + meal_tip + meal_tax, 2)

# Display the results
print(f"With the tax being ${meal_tax}, and the tip being ${meal_tip}, the total cost of your meal comes out to: ${total_cost}")

