import turtle

def draw_heart(x, y, size):
    heart_turtle.penup()
    heart_turtle.goto(x, y)
    heart_turtle.pendown()
    heart_turtle.color("red", "pink")  # Red border, pink fill
    heart_turtle.begin_fill()

    heart_turtle.left(50)
    heart_turtle.forward(size)
    heart_turtle.circle(size // 2, 200)
    heart_turtle.right(140)
    heart_turtle.circle(size // 2, 200)
    heart_turtle.forward(size)

    heart_turtle.end_fill()

def draw_lips(x, y, size):
    lips_turtle.penup()
    lips_turtle.goto(x, y)
    lips_turtle.pendown()
    lips_turtle.color("red")
    lips_turtle.width(3)

    lips_turtle.left(90)
    lips_turtle.circle(size, 180)

# Set up the window
window = turtle.Screen()
window.title("Kissing Emoji Drawing")
window.bgcolor("white")

# Set up the turtle for the face
emoji_turtle = turtle.Turtle()
emoji_turtle.speed(2)

# Draw the face
emoji_turtle.penup()
emoji_turtle.goto(0, -100)
emoji_turtle.pendown()
emoji_turtle.color("yellow", "yellow")  # Yellow border, yellow fill
emoji_turtle.begin_fill()
emoji_turtle.circle(100)
emoji_turtle.end_fill()

# Draw the eyes
for eye_pos in [(-30, 30), (30, 30)]:
    emoji_turtle.penup()
    emoji_turtle.goto(eye_pos)
    emoji_turtle.pendown()
    emoji_turtle.color("black", "black")  # Black border, black fill
    emoji_turtle.begin_fill()
    emoji_turtle.circle(15)
    emoji_turtle.end_fill()

# Draw the mouth (lips)
draw_lips(0, -40, 60)

# Draw the hearts
draw_heart(-50, -50, 20)
draw_heart(50, -50, 20)

# Hide the turtle
emoji_turtle.hideturtle()


# Draw the lips
draw_lips(0, -40, 60)

# Hide the turtle
emoji_turtle.hideturtle()


