import turtle

# Define the initial variables
level = 2
axiom = 'F-F-F-F'
rules = {
    'F': 'F-f+FF-F-FF-Ff-FF+f-FF+F+FF+Ff+FFF',
    'f': 'ffffff',
    '+': '+',
    '-': '-'
}

# Function to generate the next generation based on rules
def generate_pattern(old_pattern):
    new_pattern = ''
    for character in old_pattern:
        new_pattern += rules.get(character, character)  # Default to the character itself if not in rules
    return new_pattern

# Generate the pattern up to the desired level
pattern = axiom
for _ in range(level):
    pattern = generate_pattern(pattern)

# Calculate the length of each segment
segment_length = 20 / (2 ** level)

# Turtle graphics setup
window = turtle.Screen()
window.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")

# Function to interpret and draw the L-system pattern
def draw_l_system(pen, pattern, length, angle):
    stack = []
    for character in pattern:
        if character == 'F':
            pen.forward(length)
        if character == 'f':
            pen.penup()
            pen.forward(length)
            pen.pendown()
        elif character == '+':
            pen.right(angle)
        elif character == '-':
            pen.left(angle)
        elif character == '[':
            stack.append((pen.position(), pen.heading()))
        elif character == ']':
            position, heading = stack.pop()
            pen.up()
            pen.setposition(position)
            pen.setheading(heading)
            pen.down()

# Draw the pattern
pen.up()
pen.goto(-200, 0)  # Adjust starting position as needed
pen.down()
draw_l_system(pen, pattern, segment_length, 90)

# Finish drawing
pen.hideturtle()
window.mainloop()
