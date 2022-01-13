import turtle
import time
import os
# create a window
window = turtle.Screen()
window.setup(width=1200, height=750)
window.title("team death match")
window.bgcolor(0.3, 0.3, 0.3)
window.tracer(0)

class GameObj(turtle.Turtle):
    def __init__(self, speed, color, shape, stretchLen, stretchWid, goToX, goToY):
        super().__init__()
        self.speed(speed)
        self.color(color)
        self.shape(shape)
        self.shapesize(stretch_len=stretchLen, stretch_wid=stretchWid)
        self.penup()
        self.goto(goToX, goToY)



# player 1
p1 = GameObj(100, "Red", "square", 1, 7, -550, 0)


# player 2
p2 = GameObj(100, "Blue", "square", 1, 7, 550, 0)

# ball
# ball = turtle.Turtle()
# ball.speed(0)
# ball.fillcolor("white")
# ball.pensize(10)
# ball.begin_fill()
# ball.circle(20)
# ball.end_fill()
# ball.goto(0,0)
ball = GameObj(0, "White", "square", 1, 1 , 0, 0)
ball.dx = 0.2
ball.dy = 0.2
# methods
def player1MoveUp():
    y = p1.ycor() + 20
    if (y >= 300):
        y = 300
    p1.sety(y)

def player1MoveDown():
    y = p1.ycor() - 20
    if(y<=-300):
        y = -300
    p1.sety(y)
def player2MoveUp():
    y = p2.ycor() + 20
    if (y >= 300):
        y = 300
    p2.sety(y)

def player2MoveDown():
    y = p2.ycor() - 20
    if(y<=-300):
        y = -300
    p2.sety(y)

def ballMove():
    if (ball.ycor()>=350 or ball.ycor()<=-350):
        ball.dy *= -1
    ball.sety(ball.ycor()+ball.dy)

    if (ball.xcor() >= 600 or ball.xcor() <= -600):
        ball.goto(0,0)
        ball.dx *= -1
        time.sleep(1)
    else:
        ball.setx(ball.xcor() + ball.dx)

def bounce():
    #print(p1.)
    print("this is ball y", ball.ycor())
    print("this is player 2 y", p2.ycor())
    print("this is ball x", ball.xcor())
    print("this is player 2 x", p2.xcor())
    player1Rnage = range(p2.ycor()-20, p2.ycor()+20)
    if (ball.ycor() in player1Rnage and ball.xcor()<=550 and ball.xcor()>=545):
        ball.dx *= -1
# Bind the keyboard keys event
window.listen()
window.onkeypress(player1MoveUp, "w")
window.onkeypress(player1MoveDown, "s")
window.onkeypress(player2MoveUp, "Up")
window.onkeypress(player2MoveDown, "Down")
#keep the screen open
while True:
    ballMove()
    # bounce()
    # Paddle and ball collisions
    if ball.xcor() < -550 and ball.ycor() < p1.ycor() + 50 and ball.ycor() > p1.ycor() - 50:
        ball.dx *= -1
       # os.system("afplay bounce.wav&")

    elif ball.xcor() > 550 and ball.ycor() < p2.ycor() + 50 and ball.ycor() > p2.ycor() - 50:
        ball.dx *= -1
       # os.system("afplay bounce.wav&")
    window.update()



