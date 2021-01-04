from turtle import Screen, Turtle

FLAG_HOIST = 250
FLAG_FLY = FLAG_HOIST * 1.9
STRIPE_WIDTH = FLAG_HOIST/13
CANTON_HOIST = STRIPE_WIDTH * 7
CANTON_FLY = 2 * FLAG_FLY / 5
STAR_DIAMETER = 4 * STRIPE_WIDTH / 5
VERTICAL_STAR_GAP = -CANTON_HOIST/5
HORIZONTAL_STAR_GAP = CANTON_FLY/6
START_X = -FLAG_FLY/2
START_Y = FLAG_HOIST/2
def draw_fill_rectangle(x, y, width, height, color):
    turtle.color(color)
    turtle.goto(x, y)
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

    turtle.end_fill()
def draw_star(x, y, color, length):
    turtle.color(color)
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()

    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()

    turtle.penup()
def draw_stripes():
    y = START_Y

    for _ in range(6):
        for color in ['red', 'white']:
            draw_fill_rectangle(START_X, y, FLAG_FLY, STRIPE_WIDTH, color)

            y -= STRIPE_WIDTH

    draw_fill_rectangle(START_X, y, FLAG_FLY, STRIPE_WIDTH, 'red')
def draw_square():
    draw_fill_rectangle(START_X, START_Y, CANTON_FLY, CANTON_HOIST, 'navy')
def draw_six_stars_rows():
    y = START_Y + VERTICAL_STAR_GAP/2

    for _ in range(5):
        x = START_X + (HORIZONTAL_STAR_GAP/2 - STAR_DIAMETER/2)
        for _ in range(6):
            draw_star(x, y, 'white', abs(STAR_DIAMETER))
            x += HORIZONTAL_STAR_GAP
        y += VERTICAL_STAR_GAP
def draw_five_stars_rows():
    y = START_Y + VERTICAL_STAR_GAP

    for _ in range(4):
        x = START_X + (HORIZONTAL_STAR_GAP - STAR_DIAMETER/2)
        for _ in range(5):
            draw_star(x, y, 'white', abs(STAR_DIAMETER))
            x += HORIZONTAL_STAR_GAP
        y += VERTICAL_STAR_GAP
turtle = Turtle()
turtle.hideturtle()
turtle.speed('fastest')
turtle.penup()
draw_stripes()
draw_square()
draw_six_stars_rows()
draw_five_stars_rows()