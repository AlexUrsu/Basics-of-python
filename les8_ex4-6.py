# Занятие 8, упраженеие 4-6
# Начните работу над проектом «Склад оргтехники».


#А также класс «Оргтехника», который будет базовым для классов-наследников.
class OfficeEquipment(object):
    # id = 0
    # В базовом классе определите параметры, общие для приведённых типов.
    def __init__(self, brand, name, location):
        self.brand = brand
        self.name = name
        self.location = location

# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
class Printer(OfficeEquipment):
    def __init__(self, brand, name, location, charge=True):
        OfficeEquipment.__init__(self, brand, name, location)
        self.charge = charge

    def my_print(self, text):
        if self.charge == True:
            return 'Печатается текст: '+text
        else:
            return 'Заправьте пожалуйста катридж'

    def __str__(self):
        return (f'Принтер {self.name}, {self.brand}, ({self.location})')

class Scanner(OfficeEquipment):
    def __init__(self, brand, name, location, hiresolution=True):
        OfficeEquipment.__init__(self, brand, name, location)
        self.hiresolution = hiresolution

    def my_scan(self):
        if self.hiresolution == True:
            return 'Сканируется документ в высоком разрешении'
        else:
            return 'Сканируется документ в низком разрешении'

    def __str__(self):
        return (f'Сканер {self.name}, {self.brand}, ({self.location})')


class Xerox(OfficeEquipment):
    def __init__(self, brand, name, location, wear=0):
        OfficeEquipment.__init__(self, brand, name, location)
        self.wear = wear

    def my_copy(self, document, ncopy=1):
        st = ''
        self.wear += ncopy
        for i in range(nсopy):
            st += document+'\n'
        return st
    def __str__(self):
        return (f'Ксерокс {self.name}, {self.brand}, ({self.location})')


# Создайте класс, описывающий склад.

class Store(object):
    def __init__(self, name):
        self.name = name
        self.equipment = []
        self.location = []

# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
    def add_location(self, place):
        if place not in self.location:
            self.location.append(place)
        else:
            print('Такое помещение уже существует')

    def get_locations(self):
        ls = 'Список помещений компании: \n'
        for i in self.location.keys():
            ls += '  '+i+'\n'
        return ls

    def del_location(self, pace_name):
        self.location.remove(pace_name)

    def add_equipment(self, brand, name, location, tip):
        if location not in self.location:
            return ('Нет такого подразделения в компании: '+location)
        if tip == 'Принтер' or tip == 'принтер' or tip == 'пр' or tip == 'p' or tip == 'р' :
            x = Printer(brand, name, location)
        if tip == 'Сканер' or tip == 'сканер' or tip == 'ск' or tip == 's':
            x = Scanner(brand, name, location)
        if tip == 'Ксерокс' or tip == 'ксерокс' or tip == 'кс' or tip == 'x' or tip == 'х':
            x = Xerox(brand, name, location)
        self.equipment.append(x)

    def get_equipment(self):
        ls = 'Список имеющейся орг техники компании:\n'
        for n, i in enumerate(self.equipment):
            ls += ' '+str(n+1)+' '+i.__str__()+'\n'
        return ls

    def move_equipment(self, num, location):
        self.equipment[num-1].location = location

    def del_eqipment(self, num):
        del self.equipment[num-1]

    def __str__(self):
        s = 'Компания: '+self.name+'\n'
        s += self.get_locations()
        s += self.get_equipment()
        return s

# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.


print('Добро пожаловать в программу "Склад оргтехники"')
name = input('Введите название компании: ')
company = Store(name)
# company = Store('IBM')
while True:
    place = input('Введите подразделения компании (если хотите завершить ввод данных нажмите Enter)')
    if place == '':
        break
    else:
        company.add_location(place)

print(company.get_locations())

# company.add_location('Склад')
# company.add_location('Офис 1')
# company.add_location('Офис 2')
# company.add_location('Офис 3')
# company.add_location('Ремонтный отдел')
# company.add_location('Кабинет директора')

while True:
    print('Введите имеющуюся огр технику (если хотите завершить ввод данных нажмите Enter)')
    brand = input('Укажите фирму производитель: ')
    name = input('Укажите название и номер: ')
    location = input('Укажите подразделение, в котором хранится техника: ')
    tp = input('Укажите тип техники (p - принтер, s - сканер, x - ксерокс): ')
    if brand == '' or name == '' or location == '' or tp == ''
        break
    company.add_equipment(brand, name, location, tp)

# company.add_equipment('Canon', 'Printer 5100', 'Склад', 'пр')
# company.add_equipment('Canon', 'Printer 5100', 'Склад', 'пр')
# company.add_equipment('Samsung', 'S 400', 'Офис 1', 's')

print(company)

#company.move_equipment(1, 'Ремонтный отдел')













