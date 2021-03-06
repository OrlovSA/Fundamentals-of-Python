# 3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение ( __add__() ), вычитание ( __sub__()) ,
# умножение ( __mul__()) , деление ( __truediv__()) . Данные методы должны применяться т олько
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
# до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида * ****\n*****\n*****. .., где количество ячеек между \ n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n** .
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n***** .


class Cell:
    def __init__(self, cells=0):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        result = self.cells - other.cells
        if result > 0:
            return Cell(result)
        else:
            print('Клетка умерла')
            return Cell()

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(round(self.cells / other.cells))

    def __str__(self):
        return f"У клетки {str(self.cells)} Ячеяк"

    def make_order(self, nums):
        result = ''
        x = 0
        for num, i in enumerate('*' * self.cells, 1):
            if num - x != nums:
                result += i
            else:
                x = num
                result += i + '\n'
        else:
            return result


print("Сложение.")
cell_1 = Cell(10)
cell_2 = Cell(20)
cell_3 = cell_1 + cell_2
print(cell_3)
print("Вычитание.")
cell_4 = cell_1 - cell_3
print(cell_4)
cell_5 = cell_2 - cell_1
print(cell_5)
print("Умножение.")
cell_6 = cell_2 * cell_1
print(cell_6)
print("Деление.")
cell_7 = cell_2 / cell_1
print(cell_7)

print(cell_6.make_order(5))