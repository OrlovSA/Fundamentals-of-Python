# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__() ), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — с истема некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, user_list):
        self.user_list = user_list
        self.result = f'{user_list[0]}  {user_list[1]}  {user_list[2]}\n' \
                      f'{user_list[3]}  {user_list[4]}  {user_list[5]}\n' \
                      f'{user_list[6]}  {user_list[7]}'

    def __add__(self, other):
        result = []
        for i, x in zip(other.user_list, self.user_list):
            result_1 = []
            for n, w in zip(i, x):
                result_1.append(n+w)
            result.append(result_1)
        return Matrix(result)

    def __str__(self):
        return self.result

matr_1 = Matrix([[65, 27], [33, 6, -23], [3, 5, 8, 3],
                 [51, 23], [35, 3, 325], [6, 2, 6, 5],
                 [71, 32], [-3, 5, -32]])

matr_2 = Matrix([[342, 23], [43, 45, 233], [34, 52, 85, 32],
                 [341, 52], [33, 54, -42], [33, 25, 48, 53],
                 [515, 32], [-6, 35, -62]])

print(matr_1)
print(matr_2)
print(matr_1 + matr_2)
