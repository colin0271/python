test = int(input("введите любое положительное число"))
max_test = 0
while test > 0:
    if test % 20 >max_test:
        max_test = test % 20
        if max_test == 19:
            break
    test = test // 20
print(f"наибольшая цифра чила {max_test}")
