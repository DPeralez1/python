#---------- Challenge 1 ----------
# Let's begin with a simple one, we will use the Animal class from the last lesson
# Create a child class called fish
# Create a method called swim, if the sound is equal to None, print I am a fish, I don't have a sound
# Otherwise print, "Are you sure you're a fish"
# Create a 2nd method called ocean, ask the fish which ocean they live in and print off
# -> example "nemo is a fish who lives in the pacific ocean"
# Create an object and call all 4 methods

# class Animal():
#     def __init__(self, name, pet, sound):
#         self.name = name
#         self.pet = pet
#         self.sound = sound

#     def speak(self):
#         print(self.sound)

#     def pet_info(self):
#         print(f"My {self.pet} {self.name} makes the sound {self.sound}")

# class Fish(Animal):
#     def swim(self):
#         if self.sound == None:
#             print("You are a fish")
#         else:
#             print("Are you sure you're a fish? ")

#     def ocean(self):
#         question = input("Which ocean do you live in? ")
#         print(f"{self.name} is a {self.pet} who lives in {question} ocean")

# nemo = Fish("Nemo", "fish", None)
# nemo.speak()
# nemo.pet_info()

# nemo.swim()
# nemo.ocean()

#---------- Challenge 2 ----------
# We need a superclass for Vehicles
# Our constructor needs a cars info: make, model, year and price
# Create a method to check if the make is ford, chevy or tesla, if so return "American Made"
# Otherwise return "Imported"
# Create a method that returns the Vehicles model
# Create a method that checks if the car year is newer than 2000, is so return "Car from the 21st century"
# Otherwise return "This car is old!"
# Create a method that accepts a max_price you're willing to pay, this method checks if the car price is under your budget.
# If yes, return "Within your budget" Otherwise return "Over your budget"

# Create a child class called Style
# This class accepts a superclass, and also has a parameter of num_of_doors
# Create a method, if num_of_doors is 4 return Family car, Otherwise return Sports Car

# Create 3 objects.  1 uses the superclass, 2 use the child class
# The 2 other objects using the child class, call 3 or more methods
# use the child method and get_price method

# class Vehicles():
#     def __init__(self,make, model, year, price):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price

#     def get_make(self):
#         if self.make == "ford" or self.make == "chevy" or self.make == "tesla":
#             return "American Made"
#         else:
#             return "Imported"

#     def get_model(self):
#         return self.model

#     def get_year(self):
#         if self.year >= 2000:
#             return "Car from the 21st century"
#         else:
#             return "This car is old!"

#     def get_price(self, max_price):
#         if self.price < max_price:
#             return "Good buy, within price"
#         else:
#             return "Over budget"

# class Style(Vehicles):
#     def __init__(self, make, model, year, price, num_doors):
#         super().__init__(make, model, year, price)
#         self.num_doors = num_doors

#     def get_doors(self):
#         if self.num_doors == 4:
#             return "Family car"
#         else:
#             return "Sports car"


# # truck = Vehicles("ford", "lighting", 2023, 15000)
# # print(truck.get_make())
# # print(truck.get_price(12000))


# # car = Style("Toyota", "Camry", 2001, 9000, 4)
# # print(car.get_doors())

# sports_car = Style("Lamborghini", "Aventador", 2022, 350000,2)
# print(sports_car.get_make())
# print(sports_car.get_price(400000))
# print(sports_car.get_doors())


#---------- Challenge 3 ----------
# Creating a class for our Agents, James Bond and Ethan Hunt
# NOTE -> Try completing this without using the slides!
# Create a superclass that takes name, health and car
# Create a superclass method that prints the Agents info

# Create a child class called Spy, this inherits everything from the parent class
# Add 3 additional properties of Agency, location and killed (killed is set to False)

# (Ethan hunt will be the bad guy)
# Create a method to attack/assassinate the other agent, this takes an object as a parameter
# If the enemys health is greater than 0, subtract 20 from their health.  Show who has lost 20 health and show their updated health level
# If the enemy is less than 0, then killed becomes True, print off [enemy name] is dead

# Create 2 instances of the Spy class, one for James Bond the other for Ethan hunt
# Call the method to show the Agents info, then wait 5 seconds
# While ethan hunt health is greater than 0, both objects call assassinate
# After every attack the program waits 2 seconds before the next
from time import sleep

class Agent():
    def __init__(self, name, health, car):
        self.name = name
        self.health = health
        self.car = car

    def agent_info(self):
        print(f"Agents name: {self.name}, health: {self.health}, car: {self.car}")


class Spy(Agent):
    def __init__(self, name, health, car, agency, location):
        super().__init__(name, health, car)
        self.agency = agency
        self.location = location
        self.killed = False

    def assassinate(self, bad_guy):
        if bad_guy.health > 0:
            bad_guy.health -= 20
            print(f"{bad_guy.name} has lost 20 from their health")
            print(f"{bad_guy.name} has a health level of: {bad_guy.health}")
            if bad_guy.health <= 0:
                self.killed = True
                print(f"{bad_guy.name} is dead... {self.killed}")



james_bond = Spy("James Bond", 100, "Jaguar", "MI6", "London")
ethan_hunt = Spy("Ethan Hunt", 40, "Ferrari", "CIA", "Dubai")

james_bond.agent_info()
ethan_hunt.agent_info()
sleep(5)
while ethan_hunt.health > 0:
    james_bond.assassinate(ethan_hunt)
    ethan_hunt.assassinate(james_bond)
    sleep(2)
