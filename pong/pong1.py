import turtle

wn = turtle.Screen()

wn.title("Pong by Blue")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

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