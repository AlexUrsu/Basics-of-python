# Занятие 5 упражнение 3
# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

f = open('buch.txt', 'r', encoding='utf-8')
base = f.readlines()
f.close()
base = [line.strip('\n').split() for line in base]

cassa = 0.0
for i in base:
    cassa += float(i[1])
cassa = cassa/len(base)

workers = [i[0] for i in base if float(i[1]) < 20000.00]

# print(base)
print('Средняя зарплата сотрудников составила: ', cassa)
print('Список сотрудников в зарплатой меньше 20000:')
for n, person in enumerate(workers):
    print(n+1, person)


