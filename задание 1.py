#Реализовать функцию, принимающую два числа
#(позиционные аргументы) и выполняющую их деление.
#xисла запрашивать у пользователя, предусмотреть обработку ситуации
#деления на ноль.

def nomber(var_1, var_2):
    res = var_1 / var_2
    print(f"res : {res}")
try:
    nomber(99,0)
except ZeroDivisionError:
    print("0")
#fsfsfsfsfsf


