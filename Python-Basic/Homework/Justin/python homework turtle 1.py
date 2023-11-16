import turtle
t=turtle.Turtle()
t.speed(0)



#square
for i in range(4):
    t.forward(100)
    t.right(90)


    
#triangle
for i in range(3):
    t.forward(100)
    t.right(120)


    
#circle
t.circle(100)



#pattern
'''for i in range(100):
    t.forward(i)
    t.right(91)
'''



#problem 3
hi = 0
while hi != 10:
    hi = int(input("pick a number 1-4 10 is quit:  "))

    if hi == 1:
        t.forward(25)
    elif hi == 2:
        t.right(90)
    elif hi == 3:
        t.backward(25)
    elif hi == 4:
        t.left(90)
        
    
