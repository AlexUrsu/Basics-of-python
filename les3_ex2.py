# Занятие 3 уражнение 2
#Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.

# Функция должна принимать параметры как именованные аргументы.

def user_baza(user_name='не указано ', user_surname='не указано ', year_of_birth='не указано ', city='Москва ', email='нет почты ', phone='нет телефона'):
    st = user_name+user_surname+year_of_birth+city+email+phone
    # print(type(st)) # проверка типа данных - то, что это строка
    #print(st) #Осуществить вывод данных о пользователе одной строкой.
    return st

name = 'Alexander '
surname = 'Ursu '
year = '1981 '
current_city = 'Ivanovo '
mail = 'avursu@mail.ru '
telephone = '8-961-115-17-44'

print(user_baza(user_name=name, user_surname=surname, year_of_birth=year, city=current_city, email=mail, phone=telephone))
print(user_baza(name, surname))









