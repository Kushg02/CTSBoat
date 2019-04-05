# Import the modules.
import turtle
# Set the shape of the boat
turtle.shape('square')
# Set the color of the turtle.
turtle.color('red', 'black')
turtle.pencolor('red')
#Set Turtle Speed (Higher for sake of demo)
turtle.speed('25')






# 2) Mosquito Sweep of squarish body
for i in range(4):
  turtle.forward(100)
  turtle.left(90)


# 3) Mosquito Sweep of Odd shaped water body
turtle.clear()
turtle.speed('30')
numberOfSides = 5
degrees = 360 / numberOfSides
for x in range(numberOfSides):
  turtle.forward(100)
  turtle.left(degrees)

# 4) Spot Clean Mode 1 (Slower dissolving)
turtle.clear()
turtle.speed('20')
side = 10
for x in range(20):
  turtle.forward(side)
  turtle.left(90)
  side += 20

# 4) Spot Clean Mode 2 (Fast dissolving)
turtle.clear()
turtle.penup()
turtle.speed('20')
turtle.home()
turtle.pendown()
angle = 20
for x in range(20):
  turtle.circle(angle, 180)
  angle += 20


print("yes")


# Sample of a more complicated shape
turtle.clear()
turtle.penup()
turtle.speed('10')
turtle.home()
turtle.pendown()
angle = 0
for x in range(6):
  for x in range(3):
    turtle.forward(100)
    turtle.right(120)
  turtle.left(120)
  turtle.forward(100)
  turtle.left(180)
angle += 30
