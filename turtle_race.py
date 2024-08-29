from turtle import Turtle, Screen

import random
from venv import create


def create_turtles(num,  y):
    for turtle in range(num):
        tim = Turtle("turtle")
        the_turtles.append(tim)
        tim.color(turtle_colors[turtle])
        tim.penup()
        tim.goto(x=-230,y=y)
        y += 30



turtle_colors = ["blue", "red", "purple", "green", "black", 'orange']
the_turtles = []
start_y = -60
winner = ""
race_is_on = True

screen = Screen()
screen.setup(500, 400)
projected_winner = screen.textinput("Enter your bet.", "Which color turtle will win the race?").lower()

create_turtles(6, start_y)
while race_is_on:
    for turtle in the_turtles:
        distance = random.randint(1, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 230:
            winner = turtle.color()[0]
            race_is_on = False
            break

if projected_winner == winner:
    print(f"You win, the winning color was: {winner}.")
else:
    print(f"You guessed wrong.  The winning color was {winner}.")










screen.exitonclick()