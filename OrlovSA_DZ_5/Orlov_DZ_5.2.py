# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.


try:
    with open("text5.2.txt") as f:
        for num, i in enumerate(f, 1):
            print(num, len(i.split()))
except IOError:
    print("Произошла ошибка")

