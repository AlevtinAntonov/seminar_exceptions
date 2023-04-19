# 3. Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
# и возвращающий новый массив, каждый элемент которого равен разности элементов двух
# входящих массивов в той же ячейке. Если длины массивов не равны, необходимо как-то
# оповестить пользователя.

import array as arr


class ErrorLengthOfArraysNotEqual(Exception):
    pass


def array_difference(array_1, array_2):
    try:
        if len(array_1) == len(array_2):
            result = []
            for i in range(len(array_1)):
                result.append(array_1[i] - array_2[i])
            return print(result)
        else:
            raise ErrorLengthOfArraysNotEqual
    except ErrorLengthOfArraysNotEqual:
        print(f"Массивы разной длины: длина 1-го массива - {len(array_1)}, длина 2-го массива - {len(array_2)} !!!!")


numbers_1 = arr.array('i', [10, 20, 30])
numbers_2 = arr.array('i', [1, 2, 3])

array_difference(numbers_1, numbers_2)
