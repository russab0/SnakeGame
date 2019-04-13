import turtle
import random
import time

# Score
score = 0

# Delay in seconds
delay = 0.1 

# Screen
screen = turtle.Screen()
screen.title("Snake game")
screen.bgcolor("green")
screen.setup(width = 600, height = 600)
screen.tracer(0) # turns off the screen updates

# Head
head = turtle.Turtle()
head.color("black")
head.shape("square")
head.penup()
head.speed(15)
head.direction = "wait"

# Tail
segments = list()

#Food
food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.penup()
food.speed(0)
foodx = random.randint(-300 + 20//2, 300 - 20//2)
foody = random.randint(-300 + 20//2, 300 - 20//2)
food.goto(foodx, foody)
while head.distance(food) < 20:
    foodx = random.randint(-300 + 20//2, 300 - 20//2)
    foody = random.randint(-300 + 20//2, 300 - 20//2)
    food.goto(foodx, foody)

# Info
info = turtle.Turtle()
info.penup()
info.goto(0, 260)
info.hideturtle()
info.speed(0)
info.color("white")
info.write("Score: " + str(score), 
            align="center",
            font=("Tahoma", 24, "normal"))

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def go_up():
    if head.direction != "down" and head.direction != "stop":
        head.direction = "up"

def go_down():
    if head.direction != "up" and head.direction != "stop":
        head.direction = "down"

def go_right():
    if head.direction != "left" and head.direction != "stop":
        head.direction = "right"

def go_left():
    if head.direction != "right" and head.direction != "stop":
        head.direction = "left"


screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_left, "a")

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return x


while head.direction != "stop":
    # Collision with the food
    if head.distance(food) < 20:
        score += 1
        info.clear()
        info.write("Score: " + str(score), 
            align="center",
            font=("Tahoma", 24, "normal"))

        foodx = random.randint(-300 + 20//2, 300 - 20//2)
        foody = random.randint(-300 + 20//2, 300 - 20//2)
        food.goto(foodx, foody)

        # Adding new segment
        new_segment = turtle.Turtle()
        new_segment.color("grey")
        new_segment.shape("square")
        new_segment.speed(15)
        new_segment.penup()
        segments.append(new_segment)

    # Going from last segment to the first
    for i in range(len(segments) - 1, 0, -1): 
        x = segments[i - 1].xcor() # Getting x coordinate of prev segm
        y = segments[i - 1].ycor() # Getting y coordinate of prev segm
        segments[i].goto(x, y)
    # Setting the 0th segment coords to head's coords
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Checking for collision between head and tail
    for segment in segments:
        if segment.distance(head) < 20:
            head.write("Game Over")
            head.direction = "stop"

    x = head.xcor()
    y = head.ycor()
    if abs(head.xcor()) > 300:
        x = sign(x) * (-300)
        head.goto(x, y)
    if abs(head.ycor()) > 300:
        y = sign(y) * (-300)
        head.goto(x, y)
    

    screen.update()
    time.sleep(delay)



screen.exitonclick()