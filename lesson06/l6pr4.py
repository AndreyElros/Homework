#Задание 4
class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} : {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины {self.name} : {self.speed}')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше ограничения скорости для городской машины'
        else:
            return f'Скорость автомобиля {self.name} в пределах нормы для городской машины'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} : {self.speed}')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} выше ограничения скорости для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'


fer = SportCar(150, 'Красный', 'Ferrari', False)
bmw = TownCar(30, 'Черный', 'BMW', False)
toy = WorkCar(70, 'Белый', 'Toyota', True)
chev = PoliceCar(120, 'Синий',  'Chevrolet', True)
print(toy.turn_left())
print(f'Когда {bmw.turn_right()}, тогда {fer.stop()}')
print(f'{toy.go()} со скоростью {toy.show_speed()}')
print(f'{toy.name} имеет {toy.color} цвет')
print(f'{fer.name} является полицейской машиной? {fer.is_police}')
print(f'{toy.name}  является полицейской машиной? {toy.is_police}')
print(fer.show_speed())
print(bmw.show_speed())
print(chev.police())
print(chev.show_speed())