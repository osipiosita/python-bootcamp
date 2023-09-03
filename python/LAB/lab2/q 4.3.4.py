import turtle, math

def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,radius):
    polygon(t, radius, 50)
bob = turtle.Turtle()
circle(bob,20)
turtle.mainloop()

