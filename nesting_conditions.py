#---------- Challenge 1 ----------
# Ask a user if they want to watch a movie
# If they answer yes, ask them the genre they want to see
# if they say comedy, Tell them to watch the Hangover trilogy
# Otherwise tell them to watch Top Gun
# If they don't want to watch a movie, tell them to watch a TV series


movie = input("Would you like to watch a movie (Y/N)?: ").lower()

if movie == 'y':
    genre = input("What genre? ").lower()
    if genre == "comedy":
        print("Watch the Hangover Trilogy")
    else:
        print("Watch Top Gun")
else:
    print("Watch a TV series.")


#---------- Challenge 2 ----------
# Ask the user if they want a hotel or resort
# If they want a resort, ask them for the max price they want to spend per night
# If their max price is 350 or over, tell them to book at the six senses resort
# otherwise tell them to go to the four seasons
# If they want a hotel, tell them to go to the nearest Hilton

# location = input("Would you like to stay in a hotel or resort? ").lower()
# if location == "resort":
#     max_price = int(input("What is the max price you want to spend per night? "))
#     if max_price >= 350:
#         print("Book the Six Senses Resort.")
#     else:
#         print("Go to the Four Seasons")
# else:
#     print("Go to the nearest Hilton")


#---------- Challenge 3 ----------
# Ask the user for 3 different prices for 3 different products
# If the 3rd product is the most expensive, give them 50% off
# If the 1st product is the most expensive, give them 66% off
# print off their total


item1 = int(input("What is the price of item 1? "))
item2 = int(input("What is the price of item 2? "))
item3 = int(input("What is the price of item 3? "))

total = item1 + item2 + item3

if item1 < item2 and item2 < item3:
    total = total * 0.5
    print("Discount of 50%!")

if item1 > item2 and item2 > item3:
    total = total * .33
    print("Discount of 66%!")

print(f"Total: {total}")

#---------- Challenge 4 ----------
# Ask the user for a cost and current time in hour format (24 hour)
# If the time is from/between 7-9 then they get 20% off, give them a new total
# also if the time is from/between 10-6, there is no discount
# Any other time, thell them the store is closed

cost = int(input("Enter the price: "))
time = int(input("What is the current hour? "))

if time >= 7 and time <= 9:
    cost = cost * 0.80
    print(f"Total: {cost}")
elif time >= 10 and time <= 18:
    print("There is no discount")
else:
    print("The store is closed.")


#---------- Challenge 5 ----------
# Gather a review from a customer (1 - 10)
# If the rating is 9 or over, thank them!
# also if the rating is less than 9 and 5 or more, ask them how we can improve
# print off what the user entered and say we will work harder
# Any other rating, tell them We are sorry to hear that!

rating = int(input("Leave review (1-10): "))

if rating >= 9:
    print("Thank you!")
elif rating < 9 and rating >= 5:
    improve = input("How can we imporve? ")
    print(f"You said: {improve}")
    print("We will work harder")
else:
    print("Sorry to hear about that.")
