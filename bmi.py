# Create a module for the BMI calculator we did last lesson
# The functions should be stored in a seperate file from the main
# Import ONLY the function that you need

from bmi_functions import show_results

people = int(input("Enter number of people: "))
for i in range(people):
    weight = float(input("Enter weight: "))
    height = float(input("Enter height: "))
    show_results(weight, height)
