import turtle
import time
import random
import sys

delay = 0.1
canvas_size = 600

score = 0
high_score = 0

# Fenetre
window = turtle.Screen()
window.title("Snake")
window.bgcolor("black")
window.setup(width=canvas_size, height=canvas_size)
window.tracer(0)

# Tête Snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("grey")
head.penup()
head.goto(0,0)
head.direction = "stop"

# FOOD
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, (canvas_size /2) - 40)
pen.write("Score: 0   High Score: 0", align="center", font=("Courier", 24, "normal"))

# Fonctions
def pause():
    head.direction = "stop"
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def reset():
    time.sleep(1)
    head.direction = "stop"
    head.goto(0, 0)
    for segment in segments:
        segment.goto(canvas_size+800, canvas_size+800)
    segments.clear()
    global delay
    global score
    global pen
    global high_score
    delay = 0.1
    score = 0
    pen.clear()
    pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

def exit():
    raise SystemExit


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# KEYBOARD BIND
window.listen()
window.onkeypress(go_up, "z")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "q")
window.onkeypress(go_right, "d")
window.onkeypress(reset, "a")
window.onkeypress(exit, "x")
window.onkeypress(pause, "p")

# Game Loop
while True:
    window.update()

    #if head.xcor() > ((canvas_size / 2) - 10) or head.xcor() < -((canvas_size / 2) - 10) or head.ycor() > ((canvas_size / 2) - 10) or head.ycor() < -((canvas_size / 2) - 10)
    if head.xcor() > ((canvas_size / 2) - 10):
        head.goto(head.xcor() - canvas_size, head.ycor())
    if head.xcor() < -((canvas_size / 2) - 10):
        head.goto(head.xcor() + canvas_size, head.ycor())
    if head.ycor() > ((canvas_size / 2) - 10):
        head.goto(head.xcor(), head.ycor() - canvas_size)
    if head.ycor() < -((canvas_size / 2) - 10):
        head.goto(head.xcor(), head.ycor() + canvas_size)

    if head.distance(food) < 20:
        x = 20 * random.randint(-((canvas_size / 40) - 10), ((canvas_size / 40) - 10))
        y = 20 * random.randint(-((canvas_size / 40) - 10), ((canvas_size / 40) - 10))
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            reset()

    time.sleep(delay)

window.mainloop()
