# 5) Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.
import random


def read_file():
    try:
        with open("text5.5.txt") as f:
            return f.read()
    except IOError:
        print("Произошла ошибка")


def write_file(text):
    try:
        with open("text5.5.txt", 'a') as f:
            f.write(text + ' ')
    except IOError:
        print("Произошла ошибка")


for i in range(100):
    write_file(str(random.randrange(1, 1000)))
print("Числа созданы, файл заполнен")

result = []
num_str = ''
for i in read_file():
    if i.isdigit():
        num_str += i
    else:
        result.append(int(num_str))
        num_str = ''

print(sum(result))

