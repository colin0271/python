my_list = [9,8,7,6,7,5,4,3,2,1]
new_number = int(input("введите новый элемент рейтинга в виде числа"))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
    else:
        break
my_list.insert(i, new_number)
print(my_list)
