# Занятие2 упражнение 2
#Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

print('Добро пожаловать в программу "Перевертыш"!')
print('Видимо в ней поселился вредоносный код, который переставляет местами ваши данные :)')
lst_user = input('Введите набор данных: ').split()

if len(lst_user) % 2 == 0:
    for i in range(0, len(lst_user), 2):
        lst_user[i], lst_user[i+1] = lst_user[i+1], lst_user[i]
else:
    for i in range(0, len(lst_user)-1, 2):
        lst_user[i], lst_user[i+1] = lst_user[i+1], lst_user[i]

print('Вот такой набор получился:', lst_user)