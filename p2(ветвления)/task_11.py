import turtle

xc = float(input("xc = "))
yc = float(input("yc = "))
r = float(input("r = "))
x = float(input("x = "))
y = float(input("y = "))

if r <= 0:
    print("Радиус должен быть положительным")
else:
    d = (x - xc)**2 + (y - yc)**2

    if abs(d - r**2) < 0.000000001:
        message = "Точка лежит на окружности"
    elif d < r**2:
        message = "Точка внутри окружности"
    else:
        message = "Точка вне окружности"

    print(message)

    left = min(xc - r, x)
    right = max(xc + r, x)
    bottom = min(yc - r, y)
    top = max(yc + r, y)

    size = max(right - left, top - bottom)
    margin = size / 5

    turtle.setup(750, 750)
    turtle.setworldcoordinates(
        left - margin,
        bottom - margin,
        left + size + margin,
        bottom + size + margin
    )

    turtle.title(message)
    turtle.speed(0)

    turtle.penup()
    turtle.goto(xc, yc - r)
    turtle.pendown()
    turtle.circle(r)

    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(7, "red")

    turtle.hideturtle()
    turtle.done()