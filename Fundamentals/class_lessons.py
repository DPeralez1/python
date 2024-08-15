#---------- Challenge 1 ----------
# Create a class for animals with the properties name, pet, sound
# Create a method called speak and print the animal sound
# Create a method called pet_info, print off the animals info (properties)

# Create two objects with different values
# Call the methods with your objects

class Animals():
    def __init__(self, name, pet, sound):
        self.name = name
        self.pet = pet
        self.sound = sound

    def speak(self):
        print(self.sound)

    def pet_info(self):
        print(f"My {self.pet} {self.name} makes the sound {self.sound}")

baby1 = Animals("TARS", "dog", "bark")
baby2 = Animals("CASE", "dog", "bark")

baby1.pet_info()
baby2.pet_info()
baby1.speak()

#---------- Challenge 2 ----------
# We are working with the NBA, we need a class Player
# This class has 3 properties: name, score and team. Team is initially set to empty
# Create a method called show_stats, this will print off the info about the Player
# Create a method called select_team, this will ask for an input and set the value of the team property

# Create an object for Player
# Call the methods
# How can you show the updated player details after entering a team?

class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score
        # empty "" or None will work
        self.team = None

    def show_stats(self):
        print(f"Player info: {self.name}, {self.score}, {self.team}")

    def select_team(self):
        team = input("Enter team name: ")
        self.team = team

player1 = Player("David", 45)
player1.show_stats()

player1.select_team()
player1.show_stats()


#---------- Challenge 3 ----------
# We are building a class to find the perimeter and area of a rectangle, what perimeters do we need to solve this?
# Create a method to show the basic info about the rectangle
# Create a method to calculate the perimeter (length + width * 2), then return the value
# Create a method to calculate the area (length * width), then return the value
# Create a method that'll shorten the length of the rectangle, it'll take one perimeter and return the updated parameter

# Gather the length and width through 2 inputs
# Create an object giving it the arguments needed
# print off the basic info about the rectangle
# print off the perimeter of the retangle
# print off the area of the retangle

# Ask for an input to reduce the length of the current rectangle
# print off the updated rectangle


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_info(self):
        print(f"Rectangle with the length: {self.length} and width of: {self.width}")

    def calc_perimeter(self):
        self.perimeter = (self.length + self.width) * 2
        return self.perimeter

    def calc_area(self):
        self.area = self.length * self.width
        return self.area

    def update(self, length):
        self.updated = (self.length - length) * self.width
        return self.updated


a = int(input("Enter the length: "))
b = int(input("Enter the width: "))

rect = Rectangle(a, b)
rect.print_info()
print(f"Perimeter: {rect.calc_perimeter()}")
print(f"Area: {rect.calc_area()}")

c = int(input("Enter the number to subtract from length: "))
print(f"Updated area: {rect.update(c)}")
