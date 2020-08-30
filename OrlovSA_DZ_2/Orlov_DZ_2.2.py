# 2) Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input() .


def input_check(text):
    while True:
        result = (input(text))
        if len(result) == 0:
            print("строка пустая.")
        else:
            return result


user_list = list(input_check("Введите строку: "))
i = 0
x = 1
print(user_list)
while True:
    try:
        user_list[i], user_list[x] = user_list[x], user_list[i]
        i += 2
        x += 2
    except IndexError:
        break

print(user_list)
