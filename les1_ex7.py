# Занятие №1 задание №7

#(Дополнительно). Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.

# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

print('Добро пожавловать в программу "Ваш личный тренер"!')
print('Программа учитывает прогресс и подскаждет когда спортцен достигнитет жеаемой цели"!')

start_result = float(input('Укажите какой у Вас начальный результат: '))
end_result =float(input('Укажите конечную цель: '))
progress = 1.1
counter = 1
print('Результат (при условии, что прогресс составляет 10%):')
print(f'{counter}-й день: {start_result}')
while start_result < end_result:
    start_result = start_result * progress
    counter += 1
    print(f'{counter}-й день: {round(start_result, 2)}')

print(f'Ответ: на {counter}-ый день спортсмен достиг результата — не менее {end_result} км.')