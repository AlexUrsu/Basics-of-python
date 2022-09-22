# Занятие 6 упражнение 3
# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

# Реализовать базовый класс Worker (работник).
class Worker(object):
    # определить атрибуты: name, surname, position (должность), income (доход);
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 100000, 'bonus': 20000}



# создать класс Position (должность) на базе класса Worker;
class Position(Worker):
    def get_full_name(self):
        return self.name+' '+self.surname

    def get_total_income(self):
        return self._income['wage']+self._income['bonus']

class NewPosition(Position):                                      # Вариант назначения атрибутов при создании класса
    def __init__(self, name, surname, position='Программист'):
        self.name = name
        self.surname = surname

person1 = Position()
person1.name = 'Иван'
person1.surname = 'Иванов'
person1.position = 'Программист'

person2 = NewPosition('Петр', 'Петрович')

print(person1.get_full_name(), person1.get_total_income())
print(person2.get_full_name(), person2.get_total_income())









