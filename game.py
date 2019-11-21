import turtle

wn = turtle.Screen()
wn.title("Pingpong by Stylesowy")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# g1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# g2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Function
def g1_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def g1_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def g2_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def g2_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard bindsing
wn.listen()
wn.onkeypress(g1_up, "w")
wn.onkeypress(g1_down, "s")
wn.onkeypress(g2_up, "Up")
wn.onkeypress(g2_down, "Down")

# pilka
ball = turtle.Turtle()
ball.speed(0)
ball.color("green")
ball.shape("circle")
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1
# Main loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
    # paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1