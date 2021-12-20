import turtle
turtle.showturtle()
turtle.shape("classic")

def estrella(turtle, n, d=100):
    angulo=360/n
    if n%2==0:
        puntas=[]
        for a in range(0, n):
            turtle.penup()
            puntas.append(turtle.pos())
            turtle.circle(d, angulo)
    

        return angulo