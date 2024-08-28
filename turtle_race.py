from turtle import Turtle, Screen


turtle_colors = ["blue", "red", "purple", "green", "black", 'orange']
screen = Screen()
screen.setup(500, 400)
projected_winner = screen.textinput("Enter your bet.", "Which color turtle will win the race?").lower()
print(projected_winner)


# tim = Turtle()
y = -60
for num in range(6):
    tim = Turtle("turtle")
    tim.color(turtle_colors[num])
    tim.penup()
    tim.goto(x=-230,y=y)
    y += 30







screen.exitonclick()