import turtle

wn = turtle.Screen()

wn.title("Pong by Blue")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a= 0
score_b= 0


#padle A
padle_a= turtle.Turtle()
padle_a.speed(0)
padle_a.shape("square")
padle_a.color("white")
padle_a.shapesize(stretch_wid=5, stretch_len=1)
padle_a.penup()
padle_a.goto(-350, 0)

#padle B
padle_b= turtle.Turtle()
padle_b.speed(0)
padle_b.shape("square")
padle_b.color("white")
padle_b.shapesize(stretch_wid=5, stretch_len=1)
padle_b.penup()
padle_b.goto(350, 0)

#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx=0.1
ball.dy=0.1
#pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A :0 Player B :0", align="center", font=("Courier", 24, "normal" ))

#function
def padle_a_up():
  y = padle_a.ycor()
  y += 20
  padle_a.sety(y)
 
def padle_a_down():
  y = padle_a.ycor()
  y -= 20
  padle_a.sety(y)

def padle_b_up():
  y = padle_b.ycor()
  y += 20
  padle_b.sety(y)
 
def padle_b_down():
  y = padle_b.ycor()
  y -= 20
  padle_b.sety(y)
 

  #keybord binding 

wn.listen()
wn.onkeypress(padle_a_up,"w")
wn.onkeypress(padle_a_down,"q")

wn.onkeypress(padle_b_up,"o")
wn.onkeypress(padle_b_down,"p")
  

#main game loop
while True:
  wn.update()

#move the ball
  ball.setx(ball.xcor() +ball.dx)
  ball.sety(ball.ycor() +ball.dy)
#corder cheking
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    score_a += 1
    pen.clear()
    pen.write("Player A :{} Player B :{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal" ))

  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    score_b += 1
    pen.clear()
    pen.write("Player A :{} Player B :{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal" ))

# padle and ball colision
  if (ball.xcor() > 340 and ball.xcor()< 350) and (ball.ycor() < padle_b.ycor() + 40 and ball.ycor() > padle_b.ycor() -40 ):
    ball.setx(340)
    ball.dx *= -1 
  if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor() < padle_a.ycor() + 40 and ball.ycor() > padle_a.ycor() -40 ):
    ball.setx(-340)
    ball.dx *= -1 