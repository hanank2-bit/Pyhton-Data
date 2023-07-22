

city_flight = input("Which city do you want to fly to? Choose from London, Paris, or New York: ")
num_nights = int(input("How many nights do you want to stay at a hotel? "))
rental_days = int(input("How many days do you want to rent a car? "))

# hotel_cost: This function will take the num_nights as an argument,
# and return a total cost for the hotel stay (You can choose the price
# per night charged at the hotel).
def hotel_cost(num_nights):
    return num_nights * 110

# plane_cost: This function will take the city_flight as an argument
# and return a cost for the flight (hint: use if/else if statements in the
# function to retrieve a price based on the chosen city).
def plane_cost(city_flight):
  if city_flight == "London":
    return 235
  elif city_flight == "Paris":
    return 185
  elif city_flight == "New York":
    return 370
  else:
    return 0

# car_rental: This function will take the rental_days as an argument
# and return the total cost of the car rental.
def car_rental(rental_days):
    return rental_days * 52

# holiday_cost: This function will take the three arguments
# hotel_cost, plane_cost, car_rental. Using these three
# arguments, you can call all three of the above functions with
# respective arguments and finally return a total cost for your
# holiday.
def holiday_cost(num_nights, city_flight, rental_days):
    hotel = hotel_cost(num_nights)
    plane = plane_cost(city_flight)
    car = car_rental(rental_days)
    return hotel + plane + car


print("Holiday Details:")
print("City Flight: ", city_flight)
print("Number of Nights: ", num_nights)
print("Rental Days: ", rental_days)
print("Total Cost: £", holiday_cost(num_nights, city_flight, rental_days))


