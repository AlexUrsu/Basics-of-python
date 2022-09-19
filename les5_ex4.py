# Занятие 5 упражнение 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

english_dictionary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять'}
f = open('numbers.txt', 'r', encoding='utf-8')
base = [lst[:-1].lower().split() for lst in f]
f.close()

nf = open('rus_numbers.txt', 'w', encoding='utf-8')
for i in base:
    i[0] = english_dictionary[i[0]].capitalize()
    nf.write(' '.join(i)+'\n')
nf.close()





