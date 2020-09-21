"""                 Milestone 2 - Intro to Python
"""

"""
                        Turtles and Code

"""

import turtle                           # import car

# Creates a new turtle data object in memory, and give it a name
# Create a new turtle named amy.
fred = turtle.Turtle()                  # Run the Turtle code which in the turtle Module
                                        # fred is a turtle 
                                        # corola = cars.Toyota()
# fred will use the color red in drawing
fred.color("red")                       # corola.color("red")

# telling fred what to draw, which is, make the four sides of a square.
fred.forward(140)                       # corola.forward(100)
fred.right(135)
fred.forward(190)
fred.right(135)
fred.forward(140)


# draw a triangle using left method and the complementary angle
triangled_turtle = turtle.Turtle()
triangled_turtle.color("yellow")

for side in [1, 2, 3, 4, 5]:            # list of sides of the shape
                                        # the numbers inside the list don't matter; 
                                        # only the fact that there are five of them matters.
    triangled_turtle.forward(100)
    triangled_turtle.left(120)
    


# A Method to draw a pentagon
def pentagon():
    # Import the turtle module.
    import turtle
    
    # Create a new turtle named penta_amy.
    penta_amy = turtle.Turtle()
    
    # Set penta_amy's color.
    penta_amy.color("green")

    # Have penta_amy draw a square
    for side in [1, 2, 3, 4]:
        penta_amy.forward(100)
        penta_amy.right(72)
        
    penta_amy.forward(100)
    penta_amy.right(72)
pentagon()


# another method to draw a pentagon, by adding the number of sides to the list of sides
import turtle
penta_amy2 = turtle.Turtle()
penta_amy2.color("green")

for side in [1, 2, 3, 4, 5]:
    penta_amy2.forward(100)
    penta_amy2.right(72)

# Draw a Hexagon
import turtle
hexa_amy = turtle.Turtle()
hexa_amy.color("green")
for side in [1, 2, 3, 4, 5, 6]:         # 6 sides = count the sides of the Hexagon
    hexa_amy.forward(100)
    hexa_amy.right(60)
    
# Draw a Star
import turtle
star_amy = turtle.Turtle()
star_amy.color("yellow")
for side in [1,2,3,4,5,6,7,8]:          # 8 sides = count the sides of the star
    star_amy.forward(100)
    star_amy.right(90+45)


"""
DESCRIPTION

ITEM

A file with some useful code, which we can import into our program.
[a module]


A named block of code that can be called to get the turtle to do something.
[a method]


The name of one of the methods we've been using.
[forward]


An example of a method call.
[created_turtle.forward(100)]



"""    
    


# Creates a different colors 4 sides square
import turtle
amy = turtle.Turtle()

# Make the first red side
favorite_color = "cyan"
amy.color(favorite_color)
amy.forward(100)
amy.right(90)

# Make the  yellow sides
amy.color("yellow")
for side in[1,2]:
    amy.forward(100)
    amy.right(90)

# Make the fourth green side
amy.color("green")
amy.forward(100)




# Practice — Using variables (2/2)
import turtle
mary = turtle.Turtle()

fav_color = "purple"
sides = [1, 2, 3, 4, 5]
distance = 100
angle = 72

mary.color(fav_color )
for side in sides:
    mary.forward(distance)
    mary.right(angle)












# Practice — More loop variables (2/2)
import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three red lines, with space in between


colors_list =["red","orange","yellow"]

for color in colors_list:
    amy.color(color)
    amy.forward(50)
    amy.penup()
    amy.forward(50)
    amy.pendown()
amy.penup()
amy.back(50)





for a in [1, 2, 3]:
    # code here will run 3 times.
    for b in [4, 5, 6]:
        # code in here will run 9 times
        amy.left(90)
    # but code here will run only 3 times!
    
    
    
    
    
    
    
    
    
    #               Drawing The Rainbow
import turtle

amy =turtle.Turtle()
amy.width(10)
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw a rainbow colored Hexagon
# how to draw the shape
for color in rainbow:
    amy.color(color)
    amy.forward(70)
    amy.right(60)           # 360 degrees / number of shape sides
amy.penup()    
        
        
     
# Draw a rainbow colored flag
amy.right(90)
amy.forward(150)
amy.pendown()

for color in rainbow:
    amy.color(color)
    amy.left(90)
    amy.forward(70)
    amy.back(70)
    amy.penup()
    amy.pendown()
    amy.right(90)
    amy.forward(10)
    amy.hideturtle()




"""
                        Functions, Part One
"""

import turtle

# Set the number of sides here.
sides = 50

# Set the length of a side here.
length = 25

t = turtle.Turtle()
t.color("orange")
for side in range(sides):
    t.forward(length)
    t.right(360 / sides)
    
    
"""
DESCRIPTION

TERM

a block of code that has a name, but that doesn't run until we tell it to run
[Function]

a statement that makes a function run
[Function Call]

a value that we can pass to a function when we call that function
[Argument]

a function that's associated with an object
(Mary.forward(50) - اندهللى على الميثود فورارد الخاصة بالاوبجكت مارى)
[method]
"""