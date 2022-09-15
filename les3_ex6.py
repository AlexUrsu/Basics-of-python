# Занятие 3 уражнение 6
# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.


user_input = 'привет медвед'

def int_func(st):
    u, last = st[0].upper(), st[1:]
    return u+last

print(user_input.capitalize())
print(int_func(user_input))
