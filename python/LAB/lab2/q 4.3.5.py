import turtle
import turtle

def polygon(t, length, n, turn_angle):
    for _ in range(n):
        t.fd(length)
        t.lt(turn_angle//n)

def circle(t,radius,angle):
    polygon(t,radius, 20, angle)
bob = turtle.Turtle()
circle(bob,30, 360)
turtle.mainloop()
