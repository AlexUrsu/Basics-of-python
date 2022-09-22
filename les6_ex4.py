# Занятие 6 упражнение 4
# 4. Реализуйте базовый класс Car.
# •	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# •	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# •	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# •	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car(object):

    def __init__(self, speed=0, color='белый', name='Lada', polise=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = polise
        self.__direction = 'прямо'

    def go(self, speed=10):
        self.speed += speed
        return self.__get_status()

    def stop(self):
        self.speed = 0
        return self.__get_status()

    def turn(self, direction):
        self.__direction = direction
        return self.__get_status()

    def show_speed(self):
        return 'Текуцая скорость автомобиля '+str(abs(self.speed))+'км/ч'

    def __get_status(self):
        if self.speed >0:
            return 'Машина в движении, скорость '+str(self.speed)+'км/ч. Движется в направлении '+self.__direction
        elif self.speed <0:
            return 'Машина едет назад! Со скоростью ' + str(abs(self.speed)) + 'км/ч'
        else:
            return 'Машина остановилась'

# •	для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class TownCar(Car):
    def show_speed(self):
        if self.speed > abs(60):
            return 'Внимание! превышение скорости более 60 км/ч!!!'
        else:
            return Car.show_speed(self)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > abs(40):
            return 'Внимание! превышение скорости более 40 км/ч!!!'
        else:
            return super().show_speed()

class SportCar(Car):
    def __init__(self, speed=0, color='белый', name='Lada-Sport', polise=False):
        Car.__init__(self, speed=speed, color=color, polise=polise)
        self.name = name

class PoliceCar(Car):
    def __init__(self, speed=0, color='белый', name='Lada', polise=True):
        Car.__init__(self, speed=speed, color=color, name=name, polise=polise)




car1 = Car()
print('Создаем прототип машины')
print('Разгоняем до 100 км/ч')
print(car1.go(100))
print('Разгоняем до -100 км/ч, выходим окольным путем на остановку машины и проходим проверку остановки')
print(car1.go(-100))
print('Едем назад')
print(car1.go(-10))
print('Останавливаемся через метод')
print(car1.stop())
print('Выполняем поворот руля, но машина стоит поэтому никакого направления движения нет')
print(car1.turn('налево'))
print('Машина поехала по умолчанию со скоростью 10 км/ч с учетом направления заданного ранее')
print(car1.go())
print('Меняем направление движения')
print(car1.turn('прямо'))
print('Отдельным методом показываем текущую скорость')
print(car1.show_speed())

print('Создаем рабочую технику и проверяем на скорость')
car2 = WorkCar()
print(car2.go(100))
print(car2.show_speed())
print(car2.go(-65))
print(car2.show_speed())

print('Создаем городскую машину и проверяем на скорость')
car3 = TownCar()
print(car3.go(100))
print(car3.show_speed())
print(car3.go(-45))
print(car3.show_speed())

print('Создаем спортивную машину Лада-Спорт')
car4 = SportCar()
print(car4.name)

print('Проверяем машина действительно полицейская')
car5 = PoliceCar()
print(car5.is_polise is True)




