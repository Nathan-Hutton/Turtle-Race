from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-245, 60 - (turtle_index * 30))
    turtles.append(new_turtle)


user_bet = screen.textinput("Turtle race", "Which turtle will win?")

race_is_on = True
while race_is_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 225:
            race_is_on = False
            winner = turtle.pencolor()
            break
if winner == user_bet:
    print(f"You win! {winner} won")
else:
    print(f"You lose! {winner} won")

screen.exitonclick()



