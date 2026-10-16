import turtle

xc = float(input("xc = "))
yc = float(input("yc = "))
r = float(input("r = "))
x = float(input("x = "))
y = float(input("y = "))

if r <= 0:
    print("Радиус должен быть положительным")
else:
    distance_squared = (x - xc) ** 2 + (y - yc) ** 2
    difference = distance_squared - r ** 2
    if difference < 0:
        difference = -difference

    if difference < 0.000000001:
        message = "Точка лежит на окружности"
    elif distance_squared < r ** 2:
        message = "Точка внутри окружности"
    else:
        message = "Точка вне окружности"
    print(message)

    left = xc - r
    right = xc + r
    bottom = yc - r
    top = yc + r
    if x < left:
        left = x
    if x > right:
        right = x
    if y < bottom:
        bottom = y
    if y > top:
        top = y
    size = right - left
    if top - bottom > size:
        size = top - bottom
    margin = size / 5
    turtle.setup(750, 750)
    turtle.setworldcoordinates(left - margin, bottom - margin,
                               left + size + margin, bottom + size + margin)
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
