import random
from turtle import Turtle, Screen

colours = ["RoyalBlue", "Tomato", "Violet", "Indigo", "DarkCyan", "DarkTurquoise", "SkyBlue", "LightSlateGray"]

t = Turtle()
t.shape("turtle")
screen = Screen()


def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)


def draw_dashed_line():
    for _ in range(15):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()


def draw_figures():
    for _ in range(3, 11):
        t.color(random.choice(colours))
        for i in range(0, _):
            t.forward(100)
            t.right(360 / _)


def random_walk():
    t.pensize(15)
    t.speed("fast")
    screen.colormode(255)
    for i in range(50):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        t.color((r, g, b))
        directions = [0, 90, 180, 270]
        t.setheading(random.choice(directions))
        t.forward(30)


random_walk()
screen.exitonclick()
