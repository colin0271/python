#Для списка реализовать обмен значений соседних элементов.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
#При нечётном количестве элементов последний сохранить на своём месте.
#Для заполнения списка элементов нужно использовать функцию input().

massive = []
a = int(input("введите количество элементов:"))
for d in range(a):
    massive.append(d)
    print(massive)
k = 0
array = []
while k<len(massive)-1:
    array.append(massive[k+1])
    array.append(massive[k])
    k+=2
if len(array)<len(massive):
    b=len(massive)-1
    array.append(massive[b])
print(array)


