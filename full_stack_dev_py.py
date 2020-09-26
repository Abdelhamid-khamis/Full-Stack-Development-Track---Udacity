"""                 Milestone 2 - Intro to Python
"""

"""
                        Turtles and Code

"""

import turtle                           # import car

# Creates a new turtle data object in memory, and give it a name
# Create a new turtle named fred.
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
    for side in [1, 2, 3, 4, 5]:
        penta_amy.forward(100)
        penta_amy.right(72)             # 360 / 5       no of shape sides
pentagon()


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
    amy.right(90)
    amy.pendown()
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






#           Draw some artistic big circle made of lots and lots of squares
import turtle

jack = turtle.Turtle()
jack.color("yellow")
sides = 4
jack.speed(0)

def draw_square(length1):
    for side in range(sides):
        jack.forward(length1)
        jack.right(90)
        
for square in range(80):
    draw_square(150)
    jack.forward(5)
    jack.left(5)
        


#               draw a random shapes with random colors and distances
import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t = turtle.Turtle()
t.width(20)
t.penup()
t.back(100)
t.pendown()


def temperature_color():
    if step < 20:
        return random.choice(colors)
    elif step >= 20 and step < 40:
        return random.choice(colors)
    elif step >= 40 and step <60:
        return random.choice(colors)
    else:
        return random.choice(colors)
    
for step in range(100):
    # Change this to use a random number.
    angle = random.randint(20,90)
    distance = random.randint(5,70)
    
    t.color(temperature_color())
    t.right(angle)
    t.forward(distance)





#           shape turtle + xcor
import turtle

t = turtle.Turtle()
t.color("lime")
t.width(3)
t.penup()
t.shape("turtle")

for step in range(2000):
    t.forward(1)
    # Add your code here
    if t.xcor() >= 170 or t.xcor() <= -170:
        t.right(180)
        
        
        


import unicodedata
unicodedata.lookup("snake")
unicodedata.lookup('LEFT CURLY BRACKET')
unicodedata.name('/')
unicodedata.decimal('9')
unicodedata.category('A')  # 'L'etter, 'u'ppercase




# Write your function definition here
def start_K(word):
    if word.lower()[0] == "k":
        return True
    return False
# A function call like this should return True:
print(start_K("Kelly"))

# And one like this should return False:
print(start_K("Abe"))





#       predicates — methods that return True or False
def possible_tag(word):
    if word.startswith("<") and word.endswith(">"):
        print(word, "could maybe be an HTML tag")
    else:
        print(word, "is definitely not an HTML tag (but might contain one)")




words = ["echidna", "dingo", "crocodile", "bunyip"]
words.append("platypus")
words.extend("abc")
words.extend(["kangaroo", "wallaby"])
words.reverse()
words.sort()
print(words)


my_list_append = [1, 2, 3]
my_list_extend = [1, 2, 3]
my_list_append.append([4, 5, 6])
my_list_extend.extend([4,5,6])
my_list_append
my_list_extend