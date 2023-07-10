"""
Erin Seepersad 4/17/23	CSCI-UA 2 - 006
Assignment #9 Problem #2EC
i worked with beverly ajao
"""
# at the beginning of your program, right after you create your graphics window
  
# tell the program to not draw any graphics to the screen - your picture will exist
# in your computer's memory but will not be painted to the screen
#turtle.tracer(0)


# now do all of your graphics work



# at the very end of your program

# tell the program to draw everything in memory onto the screen all at once
#turtle.update()


import turtle
#look at turtle library for help
#canvas size
turtle.setup(500,500)
turtle.tracer(0)
draw=open("imageData.txt","r")#open
for x in draw:
    data=x.strip().split(",")#line has to split into x and u along with the color components
    xcoord=int(data[0])
    ycoord=int(data[1])
    turtle.colormode(255)
    #pen color
    turtle.pencolor(int(data[2]),int(data[3]),int(data[4]))
    turtle.fillcolor(int(data[2]),int(data[3]),int(data[4]))
    turtle.pensize(7)
    turtle.penup()
    #turtle.begin_fill()
    turtle.goto(xcoord-15,-ycoord+250)#move
    #can also do turtle.window_width()/2 and turtle.window_height()/2
    turtle.pendown()
    #pixel
    turtle.begin_fill()
    turtle.forward(1)
    turtle.backward(250)
    turtle.left(90)
    turtle.backward(250)
    turtle.left(90)
    turtle.backward(250)
    turtle.left(90)
    turtle.backward(250)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
turtle.update()#you gotta update the screen for it to show 
turtle.done()
#MARIO!
