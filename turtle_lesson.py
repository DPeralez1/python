from turtle import *

# Fullscreen the canvas
screen = Screen()
screen.setup(1.0, 1.0)
#---------- Challenge 1 ----------
# Create an object and draw a hexagon with the turtle module
# The drawing needs to stay on the screen when done
# Begin!

t = Turtle()
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)

# screen.mainloop()
#---------- Challenge 2 ----------

# Complete the same task as above with a loop, draw wtih 3 lines of code
# The objects must have a width of 5 and a color of your choice
# The drawing needs to stay on the screen when done

t = Turtle()
t.width(5)
t.color("orange")

for i in range(6):
  t.forward(100)
  t.left(60)

exitonclick()

#---------- Challenge 3 ----------

# Create 3 objects, give them each the same width with a different color
# Draw 3 triangles in a column
# Make sure the triangles are a solid color when completed
# The drawing needs to stay on the screen when done

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.width(5)
t2.width(5)
t3.width(5)

t1.color("red")
t2.color("orange")
t3.color("blue")

t1.penup()
t2.penup()
t3.penup()

t1.goto(-150, 150)
t2.goto(-150, 50)
t3.goto(-150, -50)

t1.pendown()
t2.pendown()
t3.pendown()

t1.begin_fill()
t2.begin_fill()
t3.begin_fill()

for i in range(3):
  t1.forward(100)
  t1.left(120)
  t2.forward(100)
  t2.left(120)
  t3.forward(100)
  t3.left(120)

t1.end_fill()
t2.end_fill()
t3.end_fill()

exitonclick()

#---------- Challenge 4 ----------

# Create two functions, one function draws a square, the other draws a triangle
# Each function taks two parameters, an object and a size
# Create your object, then call both functions
# The drawing needs to stay on the screen when done

def square(t, size):
  for i in range(4):
    t.forward(size)
    t.left(90)

def triangle(t, size):
  for i in range(3):
    t.forward(size)
    t.left(120)

t = Turtle()
square(t, 100)
triangle(t, 100)

exitonclick()
#---------- Challenge 5 ----------

# Refactor the code from above
# Create an input asking which shape you want to draw
# If user enters square, call the square function
# If user enters triangle, call triangle function
# Otherwise, print "We can't do that yet!"


def square(t, size):
  for i in range(4):
    t.forward(size)
    t.left(90)

def triangle(t, size):
  for i in range(3):
    t.forward(size)
    t.left(120)


ask = input("Square or Triangle?").lower()
t = Turtle()
while ask != "quit":
  if ask == "square":
    size = int(input("Enter the size? "))
    square(t,size)
  elif ask == "triangle":
    size = int(input("Enter the size? "))
    triangle(t,size)
  else:
      print("shape not here")
  ask = input("Square or Triangle?").lower()
