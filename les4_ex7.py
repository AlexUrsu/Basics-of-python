# Урок 4  уражнение 7
# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

n = 4
def fact(num):
    res = 1
    for i in range(num):
        res += res * i
        yield res

for el in fact(n):
    print(el)

#########################################################################################
# Если честно, не совсем понятно зачем так усложнять, если можно решить задачу вот так?
f = 4
res = 1
for x in range(f):
    res += res*x
    print(res)

