my_string = input("ведите строку из слов, разделите слова пробелами:").split()

for i, word in enumerate(my_string,1):
    print(f"{i}. {word[:10]}")