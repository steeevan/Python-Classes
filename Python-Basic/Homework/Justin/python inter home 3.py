import turtle
import random
screen=turtle.Screen()
t=turtle.Turtle()
t.shape("turtle")
t.speed(0)




def random_shape(times):
    times=int(input("how many random shapes do you wanna draw"))
    for i in range(times):
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        t.penup()
        t.goto(x,y)
        t.pendown()
        angle = [120, 90, 64, 60, 45]
        r=random.choice(angle)
        f=random.randint(1, 150)
        t.forward(f)
        t.right(r)
        turtle.clear()
        
random_shape(1)















def move_turtle(turtle_obj):
          distance = random.randint(1,50)
          turtle_obj.forward(distance)


def has_reached_finish_line(turtle_obj,finish_line):
     return turtle_obj.xcor() >= finish_line
     

def get_racers():
     num_turtle = int(input("Enter the number of turtles in the race:"))
     finish_line = 200

     
     turtle.speed(2)
     turtle.hideturtle()
     turtle.penup()

  
     turtles = []
     for i in range(num_turtle):
          new_turtle = turtle.Turtle()
          new_turtle.shape("turtle")
          new_turtle.color(random.random(),random.random(),random.random())
          new_turtle.penup()
          new_turtle.goto(-200,-150 + i *50) 
          turtles.append(new_turtle)

     winner = None
     while not winner:
          for t in turtles:
               move_turtle(t)
               if has_reached_finish_line(t,finish_line):
                    winner = t
                    break
     turtle.goto(0,0)
     turtle.color("black")
     turtle.write(f"The winner is Turtle {turtles.index(winner) + 1}!" ,align="center")

     
get_racers()
turtle.exitonclick()
