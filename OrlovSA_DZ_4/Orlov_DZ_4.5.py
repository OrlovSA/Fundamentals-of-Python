# 5) Реализовать формирование списка, используя функцию r ange() и возможности генератора. В
# список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка.
# # Подсказка: использовать функцию reduce() .

from functools import reduce

print(reduce(lambda a, b: a * b, [i for i in range(100, 1000, 2)]))
