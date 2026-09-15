import math

radius1 = float(input())
radius2 = float(input())

outer_radius = max(radius1, radius2)
inner_radius = min(radius1, radius2)

area = math.pi * (outer_radius ** 2 - inner_radius ** 2)

print(area)