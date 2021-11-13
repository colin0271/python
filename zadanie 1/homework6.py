distance = float(input("дистанция в первый день: "))
goal = float(input("цель:"))
days = 1
while distance < goal:
    distance *=1.1
    days +=1
print(f"требуемое количество дней - {days}")