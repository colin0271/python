goods = []
features = {"название": "", "цена": "", "колличество": "", "единица измерения": ""}
analytics = {"название": [], "цена": [], "колличество": [], "единица измерения": []}
num = 0
while True:
    if input("Для выхода из программы нажмите Q , для продолжения Enter: ").upper() == "Q":
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f"ввдите значение свойства "f": ")
        f_copy[f] = int (pro) if f in "цена количесвта" and pro.isdigit() else pro
        analytics[f].append(f_copy[f])
    goods.append(num,f_copy[f])
    print(f"\n структура товаров\n{goods} ")
    print(f"\n текущая аналитика по товарам: \n {"*" * 30}")
    for key , value in analytics.items():
        print(f"{key:>30}: {value}")
    print("*" * 30)