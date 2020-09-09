# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.


def read_file():
    try:
        with open("text5.4.1.txt") as f:
            for i in f:
                yield i.split()
    except IOError:
        print("Произошла ошибка")


def write_file(text):
    try:
        with open("text5.4.2.txt", 'a', encoding="utf-8") as f:
            f.write(text + '\n')
    except IOError:
        print("Произошла ошибка")


rus = ['Один', 'Два', 'Три', 'Четыре']
for num, i in enumerate(read_file()):
    print(i)
    i[0] = rus[num]
    write_file(' '.join(i))
    print(' '.join(i))