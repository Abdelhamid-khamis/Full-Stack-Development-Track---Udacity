import turtle                           # import car
# Creates a new turtle data object in memory, and give it a name
fred = turtle.Turtle()                  # fred is a turtle 
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
    triangled_turtle.forward(100)
    triangled_turtle.left(120)
    


# A Method to draw a pentagon
def pentagon():
    import turtle
    penta_amy = turtle.Turtle()
    penta_amy.color("green")

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
    
    
