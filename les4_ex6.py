# Урок 4  уражнение 6
# Реализовать два небольших скрипта:
# •	итератор, генерирующий целые числа, начиная с указанного;
# •	итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа,# начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle

# я не совсем понял, нужно-ли было это задание через скрипты делать? если да - я закомментировал код на эти 2 случая
#from sys import argv
#script_1, user_input1 = argv

#script_2 = argv
#user_input2 = script_2[1:]

user_input1 = 5
user_input2 = [5, 6, 8]

n_list = []
for i in count(user_input1):
    n_list.append(i)
    if user_input1+10 == i:
        break
print(n_list)

s = 0
n_list = []
for i in cycle(user_input2):
    n_list.append(i)
    s += 1
    if s == len(user_input2)*4:
        break
print(n_list)




