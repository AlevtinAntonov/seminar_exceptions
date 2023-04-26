from custom_error_classes import *
from split_input_string import split_input_string
from looking_for_male import looking_for_male
from looking_for_date import looking_for_date
from looking_for_phone import looking_for_phone

while True:
    input_string = input('Введите следующие данные в произвольном порядке, разделенные пробелом:\n'
                         'фамилия имя отчество - не меняя порядок ФИО\n'
                         'дата_рождения - строка формата dd.mm.yyyy\n'
                         'номер_телефона - целое беззнаковое число без форматирования\n'
                         'пол - символ латиницей f или m : \n').split()

    try:
        if len(input_string) < 6:
            raise NumberOfInputDataWrongError(f'ОШИБКА! Количество данных = {len(input_string)} -> меньше требуемых 6\n'
                                              'Попробуйте ввести ещё раз\n')
        elif len(input_string) > 6:
            raise NumberOfInputDataWrongError(f'ОШИБКА! Количество данных = {len(input_string)} -> больше требуемых 6\n'
                                              'Попробуйте ввести ещё раз\n')

        looking_for_male(input_string)
        looking_for_date(input_string)
        looking_for_date(input_string)
        looking_for_phone(input_string)

    except NumberOfInputDataWrongError as e:
        print(e)
    except MaleNotEnteredError as e:
        print(e)
    except DateInputError as e:
        print(e)
    except PhoneNumberInputError as e:
        print(e)

    else:
        split_input_string(input_string)
        break
