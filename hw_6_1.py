'''1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.'''

import heapq
from memory_profiler import profile

@profile
def random_list():
    import random
    par_1 = int(input(f'Введите нижнюю границу диапазона: '))
    par_2 = int(input(f'Введите верхнюю границу диапазона: '))
    par_3 = int(input(f'Введите кол-во чисел в списке: '))
    list = []
    for i in range(par_3):
        list.append(random.randint(par_1, par_2))
    return list

from memory_profiler import profile

@profile
def main():
    range_ = random_list()
    min_ = heapq.nsmallest(2, range_)
    print(f' Из списка: *range_ два наименьших элемента равны {min_}.')



# Вариант 2.

@profile
def main_1():
    a = random_list()
    # print(*a)
    print(*sorted(a)[:2])


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main_1()
