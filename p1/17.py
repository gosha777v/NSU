weight = float(input())
height = float(input())

weight_kg = weight * 0.45359237
height_m = height * 0.0254

bmi = weight_kg / height_m ** 2

print(f"{bmi:.2f}")