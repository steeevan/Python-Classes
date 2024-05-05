#1-3
import random
import turtle as tk
screen=tk.Screen()
bob=tk.Turtle()
screen.setup(width=800,height=600)
radius=10
angle=90
bob.shape("turtle")

bob.speed(5)
radius = 10
angle = 90
for i in range(3):
    color = (random.random(), random.random(), random.random())
    bob.pencolor(color)
    bob.circle(radius)
    radius += 5
    angle -= 1
bob.width(10)
colors = ["red","green", "blue","orange","purple"]
for i in range(5):
  bob.color(random.choice(colors))
  bob.forward(100)
  bob.right(144)


for i in range(4):
  bob.forward(10)
  bob.right(90)
  bob.forward(50)
  bob.left(90)
  bob.forward(10)

