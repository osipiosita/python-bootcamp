import turtle
def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)
bob = turtle.Turtle()
polygon(bob, 200,5)
turtle.mainloop()