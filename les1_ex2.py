# Занятие №1 задание №2
# Пользователь вводит время в секундах.


print('Здравствуйте, программа переводит время из секунд в формат чч:мм:сс.')
time_input = int(input('Введите любое число. Это будет время в секундах (пример: 354)'))

# Переведите время в часы, минуты, секунды

user_hours = time_input // 360
time_input = time_input % 360
user_minutes = time_input // 60
user_seconds = time_input % 60

# и выведите в формате чч:мм:сс. Используйте форматирование строк.

print(f'Результат: {user_hours}:{user_minutes}:{user_seconds}')



