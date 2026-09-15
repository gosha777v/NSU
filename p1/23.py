total = int(input())

hours = total // 3600 % 24
minutes = total // 60 % 60
seconds = total % 60

print(hours, "часов", minutes, "минут", seconds, "секунд")