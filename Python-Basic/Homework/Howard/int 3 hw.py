# exercise 1
import random
import turtle
def shapes():
    screen = turtle.Screen()
    t = turtle.Turtle()

    t.speed(0)

    user_input = int(input("Please input the numbers of shapes you want: "))
    
    for i in range(user_input):
        random_size = random.randint(2,7)
        for i in range(random_size):
            t.color(random.random(),random.random(),random.random())
            distance = random.randint(50,100)
            t.forward(distance)
            turn_angle = random.randint(int((360/random_size)/2),int(360/random_size))
            t.right(turn_angle)
        t.goto(0,0)


# exercise 2
# function to move a turtle forward by a random distance
def move_turtle(turtle_obj):
    distance = random.randint(1,5)
    turtle_obj.forward(distance)


# function to cheak if a turtle has reached the finish line
def has_reached_finish_line(turtle_obj,finish_line):
    return turtle_obj.xcor()>=finish_line


# get users input for the race
def get_racers():
    num_turtle = int(input("Enter the number of turtle racers you want in the race: "))
    finish_line = 200

    # set up turtle race
    turtle.speed(2)
    turtle.hideturtle()
    turtle.penup

    # create the turtle and set up their initial starting place
    turtles = []
    for i in range(num_turtle):
        new_turtle = turtle.Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(random.random(),random.random(),random.random())
        new_turtle.penup()
        new_turtle.goto(-200,-150+i*50)# adjust y-coord for each turtle
        turtles.append(new_turtle)

    winner = None
    while not winner:
        for t in turtles:
            move_turtle(t)
            if has_reached_finish_line(t,finish_line):
                winner = t
                break
    # display winner
    turtle.goto(0,0)
    turtle.color("black")
    turtle.write(f"The winner is Turtle{turtles.index(winner)+ 1}!",align="center")

