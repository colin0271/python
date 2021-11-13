test = int(input("введите время в секундах:"))
if test < 60:
    print(f"00.00:{test}")
elif test < 3600:
    print(f"00:{test // 60}:{test % 60}")
else:
    print(f"{test // 3600}:{(test % 3600) // 60}:{test % 60}")
