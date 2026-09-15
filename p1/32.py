angle = float(input())

total_minutes = int(angle * 2)

hours = total_minutes // 60
minutes = total_minutes % 60

print(hours, minutes)