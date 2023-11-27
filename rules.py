import turtle as t

t.speed(0)
t.pencolor('red')
t.hideturtle()


def snail(radius: int):
    for i in range(120):
        t.circle(radius=radius)
        radius += 2

    return t.mainloop()

# snail(radius=2)


def snail_2(angle: int, radius: int):
    for i in range(120):
        t.circle(radius=radius)
        t.right(angle=angle)
        radius += 2

    return t.mainloop()

snail_2(angle=0, radius=5)

