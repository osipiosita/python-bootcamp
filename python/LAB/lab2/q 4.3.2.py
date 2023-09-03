import turtle
def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)
bob = turtle.Turtle()
square(bob, 200)
turtle.mainloop()