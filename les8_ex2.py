# Занятие 8, упраженеие 2
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyDivError(Exception):
    pass


def div(dividend, divisor):
    try:
        dividend = int(dividend)
        divisor = int(divisor)
        if divisor == 0:
            raise MyDivError
    except ValueError:
        print('Не получилось перевести данные в число')
    except MyDivError:
        print('MyDivError: Делить на ноль нельзя!')
        return 0
    else:
        return dividend/divisor


# x, y = input('Введите через пробел два числа: певое - делимое, второе - делитель: ').split()

print(div(20, 3))
print(div(5, 0))
print(div(10, 2))









