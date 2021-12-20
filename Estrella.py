import turtle
turtle.getscreen()

turtle.shape("classic")

def estrella(n, d=100):
    angulo=360/n
    if n%2==0:
        lineas=[]
        for a in range(0, n):
            turtle.penup()
            lineas.append(turtle.pos())
            turtle.circle(d, angulo)
        for b in range(0, len(lineas)):
            if b%2==0:
                turtle.pendown()
                turtle.goto(lineas[b][0], lineas[b],[1])
    