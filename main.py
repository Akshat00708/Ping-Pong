"""
Name: Ping Pong
Creator: Akshat Srivastava
Multiplayer: -/
Is Customizable: -/
Scoring: X
FPS: LOW/MEDIUM/HIGH
Module: Turtle
Created: 13|9|2021
Free: -/
"""

import turtle 

window = turtle.Screen()  
window.title("Ping Pong Game by @akshat_srivastava") 
window.bgcolor("#152238")  
window.setup(width=800, height=600)
window.tracer(0)

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()  
paddle_a.speed(0)  
paddle_a.shape("square") 
paddle_a.color("white") 
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
paddle_a.penup()  
paddle_a.goto(-350, 0) 

paddle_b = turtle.Turtle()  
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white") 
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup()  
paddle_b.goto(350, 0) 

ball = turtle.Turtle()  
ball.speed(0)  
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) 
ball.dx = 0.2  
ball.dy = -0.2

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A :0 Player B:0 ", align="center", font=("Consolas", 24, "normal"))

line = turtle.Turtle()  
line.speed(0) 
line.shape("square")
line.color("#fff") 
line.shapesize(stretch_wid=800, stretch_len=0.1) 
line.penup()  
line.goto(0, 0) 


def paddle_a_up(): 
    y = paddle_a.ycor()    
    y += 20  
    paddle_a.sety(y)  


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)  


def paddle_b_up():  
    y = paddle_b.ycor()    
    y += 20 
    paddle_b.sety(y)  


def paddle_b_down():  
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y) 


window.listen()  
window.onkeypress(paddle_a_up, "w")  
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")  
window.onkeypress(paddle_b_down, "Down") 

while True: 
    window.update() 
    ycor = ball.ycor()
    xcor = ball.xcor()
    ball.setx(xcor + ball.dx)
    ball.sety(ycor + ball.dy)

    if ycor > 290:
        ball.sety(290)
        ball.dy *= -1 

    elif ycor < -290:
        ball.sety(-290)
        ball.dy *= -1 

    elif xcor > 390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    
    elif xcor < -390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1 

    elif ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1

# End
