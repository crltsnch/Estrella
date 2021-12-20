import turtle
def estrella(turtle, n, d):
    angulo=(180-((180*(n-2)))/n)*2
    for i in range(n):
        turtle.forward(d)
        turtle.left(144)

    return angulo