import turtle
import random

pont_jobb = 0
pont_bal = 0

ablak = turtle.Screen()
ablak.bgcolor('black')
ablak.setup(800, 600)
ablak.title('Pong')
ablak.tracer()
#----------------------------
b = turtle.Turtle()
b.shape('square')
b.color('white')
b.shapesize(5, 1)
b.speed(0)
b.penup()
b.goto(-350, 0)

j = turtle.Turtle()
j.shape('square')
j.color('white')
j.shapesize(5, 1)
j.speed(0)
j.penup()
j.goto(350, 0)

labda = turtle.Turtle()
labda.shape('circle')
labda.color('white')
labda.shapesize(1, 1)
labda.speed(20)
labda.penup()
labda.goto(0, 0)
labda.dx = 3.5
labda.dy = 3.5

score = turtle.Turtle()
score.shape('square')
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f'bal:{pont_bal}   jobb: {pont_jobb}', align='center', font = ('Courier', 24, 'normal') )
def b_fel():
    y = b.ycor()
    y += 20
    b.sety(y)
    
def b_le():
    y = b.ycor()
    y -= 20
    b.sety(y)
    
def j_fel():
    y = j.ycor()
    y += 20
    j.sety(y)

def j_le():
    y = j.ycor()
    y -= 20
    j.sety(y)
    
ablak.listen()
ablak.onkeypress(b_fel, "w")
ablak.onkeypress(b_le, "s")
ablak.onkeypress(j_fel, "Up")
ablak.onkeypress(j_le, "Down")

while True:
    ablak.update()
    
    labda.x = labda.xcor()    
    labda.y = labda.ycor()
    labda.x = labda.x + labda.dx
    labda.y = labda.y + labda.dy
    labda.setx(labda.x)
    labda.sety(labda.y)
    
    if labda.ycor() > 290:
        labda.sety(290)
        labda.dy *= -1
        
    elif labda.ycor() < -290:
        labda.sety(-290)
        labda.dy *= -1
        
    elif labda.xcor() > 400:
        labda.setx(0)
        labda.sety(0)
        labda.dx *= -1
        pont_bal +=1
        score.clear()
        score.write(f'bal:{pont_bal}   jobb: {pont_jobb}', align='center', font = ('Courier', 24, 'normal') )
        
        
    elif labda.xcor() < -400:
        labda.setx(0)
        labda.sety(0)
        labda.dx *= -1
        pont_jobb +=1
        score.clear()
        score.write(f'bal:{pont_bal}   jobb: {pont_jobb}', align='center', font = ('Courier', 24, 'normal') )
        
    if labda.xcor() < -340 and labda.ycor() < b.ycor() + 50 and labda.ycor() > b.ycor() - 50:
        labda.dx *= -1 
        
    
    elif labda.xcor() > 340 and labda.ycor() < j.ycor() + 50 and labda.ycor() > j.ycor() - 50:
        labda.dx *= -1
        
    
    
