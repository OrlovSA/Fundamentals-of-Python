# 6) *Реализовать структуру данных « Товары ». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


def input_check(text):
    while True:
        try:
            result = int(input(text))
            if result <= 0:
                print("Число меньше или ровно 0")
            else:
                return result
        except ValueError:
            print("Введено не верное значение")


products = {
    'Название': [],
    'Цена': [],
    'Количество': [],
    'Ед': []
}
name = []
cost = []
quantity = []
measurements = []

structures = []
user_quantity = input_check("введите количество продуктов: ")
i = 1
while i-1 < user_quantity:
    structure = []
    name.append(input(f"введите название тавара №{i}: "))
    cost.append(input(f"введите стоймость тавара - {name[i-1]}: "))
    quantity.append(input(f"введите количество тавара - {name[i-1]}: "))
    measurements.append(input(f"введите еденици измерения тавара - {name[i-1]}: "))
    products.update({'Название': name[i-1], 'Цена': cost[i-1], 'Количество': quantity[i-1], 'Ед': measurements[i-1]})
    structure.append(i)
    structure.append(products.copy())
    structures.append(tuple(structure))
    i += 1

print(structures)

products.update({
    'Название': name,
    'Цена': cost,
    'Количество': quantity,
    'Ед': measurements
})
print(products)