# Занятие №1 задание №5
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

print('Добро пожаловать в программу "домашний бухгалтер", которая рассчитает и подскажет с каким финансовым результатом работает фирма.')
# Запросите у пользователя значения выручки и издержек фирмы.
print('Для этого укажите:')
user_income = float(input('Выручку: '))
user_spending = float(input('Издержки: '))

balance = user_income-user_spending

if balance > 0:
    print('Поздравляем! Выручка больше издержек: ', balance)
elif balance < 0:
    print('К сожалению фирма несет убытки, т.к. издержки больше выручки: ', balance, ':(')
else:
    print('Вы сработали в 0, что весьма неудивительно по реалям предпринимателства на территории РФ ;)')

