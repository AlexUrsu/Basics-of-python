# Занятие 5 упражнение 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

#numbes = [x for x in range(random(100))]


import random
# создаем набор случайных чисел
baza = [random.randint(0, 100) for x in range(random.randint(0, 30))]

f = open('random_numbers.txt', 'w+', encoding='utf8')
baza = list(map(str, baza))  # переводим числа в строки
text = ' '.join(baza)        # объединяем в одну строку
f.write(text) #записиываем числа в файл
f.seek(0)     # переводим на начало для чтения
new_info = f.readline().split()
result = 0
for i in new_info:
    result += int(i)
print(new_info) #оставил для наглядности
print('Сумма чисел:', result)
f.close()









