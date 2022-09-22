# Занятие 6 упражнение 2
# Реализовать класс Road (дорога).
# •	определить атрибуты: length (длина), width (ширина);
# •	значения атрибутов должны передаваться при создании экземпляра класса;
# •	атрибуты сделать защищёнными;
# •	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# •	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# •	проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road(object):
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self, metr_mass, depth):
        return f'Результат: {self._width} м*{self._length} м*{metr_mass} кг*{depth} см = {self._length*self._width*metr_mass*depth/1000} т.'

print('Создадим дорогоу по вашим параметрам и рассчитаем сколько нужно асфальта.')
ln, wh = input('1. Укажите через пробел длину и ширину дороги: ').split()
ms = int(input('2. Укажите сколько весит асфальт (в кг) для покрытия /n одного кв. метра дороги асфальтом, толщиной в 1 см: '))
dh = int(input('3. Укажите какова будет толщина покрытия в сантиметрах: '))

small_road = Road(int(ln), int(wh))
print(small_road.mass_calculation(ms, dh))






