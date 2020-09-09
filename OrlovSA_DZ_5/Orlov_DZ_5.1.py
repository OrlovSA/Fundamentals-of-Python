# 1) Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.


def write_file(text):
    try:
        with open("text5.1.txt", "a", encoding="utf-8") as f:
            f.write(text + '\n')
    except IOError:
        print("Произошла ошибка")


while True:
    result = input("Введите строку: ")
    if not result:
        print('Ввод закончен.')
        break
    else:
        write_file(result)