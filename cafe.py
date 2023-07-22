# Creating a list called menu
menu = ["coffee", "tea", "cake", "sandwich"]

# Creating a dictionary called stock
stock = {
  "coffee": 20,
  "tea": 15,
  "cake": 10,
  "sandwich": 5
}

# Creating a dictionary called price
price = {
  "coffee": 2.5,
  "tea": 2.0,
  "cake": 3.0,
  "sandwich": 4.0
}

# Calculated the total stock worth in the cafe
total_stock = 0 # Initializing a variable to store the total stock value

# Loop through the menu list
for item in menu:
  # Calculate the item value by multiplying stock value by price value
  item_value = stock[item] * price[item]
  # Add the item value to the total stock value
  total_stock += item_value

# Print out the result
print("The total stock worth in the cafe is", total_stock, "dollars.")
