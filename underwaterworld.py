# UnderWater World Knock out Game 
#Collect as many Star fishes as you can
#Beware of Sharks 

import turtle
import os
import random
import time

# Background SCreen
wn = turtle.Screen()
wn.title("Underwater World")
wn.bgcolor("skyblue")
wn.bgpic("disney.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("boy_left.gif")
wn.register_shape("boy_right.gif")
wn.register_shape("shark1.gif")
wn.register_shape("star1.gif")

# Score
score = 0

# Lives
lives = 3

# Player
player = turtle.Turtle()
player.speed(0)
player.shape("boy_left.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Star fishes
stars = []

for _ in range(20):
    star_fish = turtle.Turtle()
    star_fish.speed(0)
    star_fish.shape("star1.gif")
    
    star_fish.color("green")
    star_fish.penup()
    star_fish.goto(-100, 250)
    star_fish.speed = random.randint(1, 2)
    
    stars.append(star_fish)

# Sharkies
sharks = []

for _ in range(20):
    shark = turtle.Turtle()
    shark.speed(0)
    shark.shape("shark1.gif")
    shark.color("red")
    shark.penup()
    shark.goto(100, 250)
    shark.speed = random.randint(1, 2)

    sharks.append(shark)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Lives: 3", align="center", font=("Courier", 24, "normal"))

# Functions
def go_left():
    player.direction = "left"
    player.shape("boy_left.gif")
    
def go_right():
    player.direction = "right"
    player.shape("boy_right.gif")

    
# Keyboard bindings
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()
    
    # Move the player
    if player.direction == "left":
        player.setx(player.xcor() - 1)
    
    if player.direction == "right":
        player.setx(player.xcor() + 1)
        
    # Check for border collisions
    if player.xcor() < -390:
        player.setx(-390)
        
    elif player.xcor() > 390:
        player.setx(390)
        
    for star_fish in stars:
        # Move the star fish
        star_fish.sety(star_fish.ycor() - star_fish.speed)
    
        # Check if star fishes are off the screen
        if star_fish.ycor() < -300:
            star_fish.goto(random.randint(-300, 300), random.randint(400, 800))

        # Check for collisions
        if player.distance(star_fish) < 40:
            # Score increases
            score += 10
        
            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
        
            # Move the star fish back to the top
            star_fish.goto(random.randint(-300, 300), random.randint(400, 800))



    for shark in sharks:    
        # Move the bad things
        shark.sety(shark.ycor() - shark.speed)
    
        if shark.ycor() < -300:
            shark.goto(random.randint(-300, 300), random.randint(400, 800))
    
        
        if player.distance(shark) < 40:
            # Score increases
            score -= 10
            lives -= 1
        
            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
            
            time.sleep(1)
            # Move the shark back to the top
            for shark in sharks:
                shark.goto(random.randint(-300, 300), random.randint(400, 800))
        
        
    # Check if lives  over
    if lives == 0:
        pen.clear()
        pen.write("Game Over! Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        wn.update()
        time.sleep(5)
        score = 0
        lives = 3
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
        
        
        
        
        
        
        
