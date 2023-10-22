import turtle
paramater = 0
t = turtle.Turtle()
usercolor = input("What pen color? ")
t.pencolor(usercolor)
usersize = int(input("What pen size? "))
t.shapesize(stretch_wid=usersize, stretch_len=usersize, outline=usersize)
print("Type up() to not draw anything and move, and type down() to start drawing while moving.")
print("Type forward, backward, left, or right to move in that direction.")
print("Type stop to stop the program")
userinput = input("")
while userinput != "stop":
    print("Type up() to not draw anything and move, and type down() to start drawing while moving.")
    print("Type forward, backward, left, or right to move in that direction.")
    print("Type stop to stop the program")
    userinput = input("")
    if userinput == "up()":
        t.penup()
    elif userinput == "down()":
        t.pendown()
    elif userinput == "forward":
        paramater = int(input("How far? "))
        t.forward(paramater)
    elif userinput == "backward":
        paramater = int(input("How far? "))
        t.backward(paramater)
    elif userinput == "right":
        paramater = int(input("How far? "))
        t.right(paramater)
    elif userinput == "left":
        paramater = int(input("How far? "))
        t.left(paramater)
    else:
         print("You typed a invalid input")
    
    
