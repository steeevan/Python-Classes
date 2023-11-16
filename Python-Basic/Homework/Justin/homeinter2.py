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
    turtle.done()
        
random_shape(1)


          









def random_walk(number):
    number = int(input("how many steps do you want turtle to walk?: "))
    for i in range(number):
        t.forward(random.randint(1, 150))
        t.right(random.randint(1,360))
random_walk(10)
