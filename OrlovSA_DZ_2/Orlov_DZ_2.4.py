#  4) Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
# только первые 10 букв в слове.


def input_check(text):
    while True:
        result = input(text).split()
        if len(result) <= 1:
            print("Введите больше 1 слова")
        else:
            return result


words = input_check('Введите слова через пробел: ')
for numb, word in enumerate(words, 1):
    print(numb, word[:10])

