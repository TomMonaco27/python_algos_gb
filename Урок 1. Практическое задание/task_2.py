"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

# Вариант 1 Cложность: O(n) - линейная
def min_lst(lst):
    min_el = 0
    for el in lst:  # O(n) - Линейная
        if el < min_el: # O(1) - Константа
            min_el = el
    return min_el

lst = [1,-2,3,-4]

print('Программа "Функция, поиск минимального элемента в списке". Вариант 1. Сложность O(n) - Линейная')
print(f'Min el is :{min_lst(lst)}')

# Вариант 2 Сложность O(n^2) - квадратичная
def min_lst_two(lst):
    for el in list:
        min_el = True
        for el2 in lst:
            if el > el2:
                min_el = False
        if min_el:
            return el

print('Программа "Функция, поиск минимального элемента в списке". Вариант 2. Сложность O(n) - Линейная')
print(f'Min el is :{min_lst(lst)}')

