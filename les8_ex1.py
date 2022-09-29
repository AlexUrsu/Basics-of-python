# Занятие 8, упраженеие 1
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#  В рамках класса реализовать два метода.

class Data(object):
    cdata = ''

    def __init__(self, stdata):
        Data.cdata = stdata

    #  Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    @classmethod
    def get_indata(cls):
        return list(map(int, cls.cdata.split('-')))

    #  Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

    @staticmethod
    def leap_year(user_year):
        if user_year % 400 == 0 or user_year % 4 == 0 and user_year % 100 != 0:
            return True
        else:
            return False

    @staticmethod
    def valid_data(userdata):
        if type(userdata) == str:
            userdata = Data(userdata).get_indata()
        if userdata[1] <= 0 or userdata[1] > 12:
            return 'Месяц указан ошибочно.'
        if userdata[2] < 0 or userdata[2] > 5000:
            return  'Возомжно год указан ошибочно (в программе стоит ограничение на отрицательные числа и чиcла превышающие 5000). '
        if userdata[0] <= 0 or userdata[0] > 31:
            return 'День указан ошибочно.'
        elif userdata[0] > 30 and userdata[1] == 4 or userdata[1] == 6 or userdata[1] == 9 or userdata[1] == 11:
            return 'День указан ошибочно. '
        elif userdata[0] > 28 and userdata[1] == 2 and Data.leap_year(userdata[2]) == False:
            return 'День указан ошибочно.'
        elif userdata[0] > 29 and userdata[1] == 2 and Data.leap_year(userdata[2]) == True:
            return 'День указан ошибочно.'
        else:
            return 'Данные введены корректно.'


#  Проверить работу полученной структуры на реальных данных.
data1 = Data('12-12-2022')
print('Проверяем первый метод и убеждаеся, что он переводит дату в числа:', data1.get_indata())

print('Проверяем на корректность введеныне данные, через второй статический метод')
print('12-13-2022', Data.valid_data('12-13-2022'))
print('12-0-2022', Data.valid_data('12-0-2022'))
print('12-12-20220', Data.valid_data('12-12-20220'))
print('31-11-2022', Data.valid_data('31-11-2022'), 'Проверяется дата с учетом месяца')
print('31-1-2022', Data.valid_data('31-1-2022'), 'Проверяется дата с учетом месяца')
print('29-2-2022', Data.valid_data('29-2-2022'), 'Проверяется дата февраля с учетом високосного года')
print('28-2-2022', Data.valid_data('28-2-2022'), 'Проверяется дата февраля с учетом високосного года')
print('29-2-2024', Data.valid_data('29-2-2024'), 'Проверяется дата февраля с учетом високосного года')