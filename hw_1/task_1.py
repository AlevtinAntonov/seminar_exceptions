# 1. Реализуйте 3 метода, чтобы в каждом из них получить разные исключения
class ElementNotInteger(Exception):
    pass


class ElementIsNone(Exception):
    """Element Is None"""


class ElementEqualOrSmallerThanZero(Exception):
    """Element is Equal or Smaller then Zero"""


def check_is_instance(a):
    try:
        if not isinstance(a, int):
            raise ElementNotInteger
        print(f'Число a = {a} - целое')

    except ElementNotInteger("Element is not integer"):
        print(f'Число a = {a} - не целое')


def check_is_equal_or_less_zero(a):
    try:
        if a <= 0:
            raise ElementEqualOrSmallerThanZero
        print(f'Число a = {a} - больше нуля')
    except ElementEqualOrSmallerThanZero("Element is Equal or Smaller then 0"):
        print(f'Число a = {a} - равно или меньше 0')


def check_is_not_none(a):
    try:
        if a is None:
            raise ElementIsNone
        print(f'Число a = {a} - существует')
    except ElementIsNone("Element Is None"):
        print(f'Число a = {a} - не существует')


my_list = [5, 1, 5.5, -3, None]

check_is_not_none(my_list[0])
check_is_equal_or_less_zero(my_list[2])
check_is_instance(my_list[1])
check_is_instance(my_list[2])
# check_is_equal_or_less_zero(my_list[3])
# check_is_not_none(my_list[0])
