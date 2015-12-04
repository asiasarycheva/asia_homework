__author__ = 'asiaptichka'
#unicode=utf-8

class Tank():
    #автоматически создаём атрибуты класса с помощью конструктора
    def __init__(self):
        self.model = str(input('введите модель танка '))
        self.chassis = bool(input('нажми 1 если есть шасси танка '))
        self.track = bool(input('нажми 1 если есть гусеница танка '))
        self.velocity = int(input('введите скорость танка '))

    def status(self):
        print(self.model, self.chassis, self.track, self.velocity)

    def __str__(self):
        return ' '.join([self.model, str(self.chassis), str(self.track), str(self.velocity)])

    def __repr__(self):
        return self.__str__()

class Car():
    def __init__(self):
        self.model = str(input('введите модель машины '))
        self.wheels = bool(input('нажми 1 если есть колёса у машины '))
        self.velocity = int(input('введите скорость машины '))

    def status(self):
        print(self.model, self.wheels, self.velocity)

    def __str__(self):
        return ' '.join([self.model, str(self.wheels), str(self.velocity)])

    def __repr__(self):
        return self.__str__()


class Cart():
    def __init__(self):
        self.wheels = int(input('введите число колёс телеги '))
        self.velocity = int(input('введите скорость телеги '))

    def status(self):
        print(self.wheels, self.velocity)

    def __str__(self):
        return ' '.join([str(self.wheels), str(self.velocity)])

    def __repr__(self):
        return self.__str__()


a = input('сколько введём танков? ')
n = int(a)
tank_dict = {i: Tank() for i in range(n)}
print('номер|модель|шасси?|гусеница?|скорость'
      '\n', tank_dict)



a = input('сколько введём машин? ')
n = int(a)
car_dict = {i: Car() for i in range(n)}
print('номер|модель|колёса|скорость|'
      '\n', car_dict)

a = input('сколько введём телег? ')
n = int(a)
cart_dict = {i: Cart() for i in range(n)}
print('номер|колёса|скорость|'
      '\n', tank_dict)


def change_tank():
    m = int(input('меняем номер...'))
    k = int(input('меняем '
              '\n модель - 1'
              '\n шасси? - 2'
              '\n гусеница - 3?'
              '\n скорость - 4' ))
    if k == 1:
        tank_dict[m][1] = str(input('новая модель? '))
    if k == 2:
        tank_dict[m][2] = str(bool(input('есть ли шасси? ')))
    if k == 3:
        tank_dict[m][3] = str(bool(input('есть ли гусеница? ')))
    if k == 4:
        tank_dict[m][4] = str(int(input('скорость ? ')))



def change_car():
    m = int(input('меняем номер...'))
    k = int(input('меняем '
              '\n модель - 1'
              '\n колёса - 2'
              '\n скорость - 3?'))
    if k == 1:
        tank_dict[m][1] = str(input('новая модель? '))
    if k == 2:
        tank_dict[m][2] = bool(input('колёса? '))
    if k == 3:
        tank_dict[m][3] = int(input('скорость? '))



def change_cart():
    m = int(input('меняем номер...'))
    k = int(input('меняем '
              '\n модель - 1'
              '\n колёса - 2'
              '\n скорость - 3?'))

    if k == 1:
        tank_dict[m][1] = int(input('число колёс? '))
    if k == 2:
        tank_dict[m][2] = int(input('скорость? '))

func = {
    1: change_tank,
    2: change_car,
    3: change_cart
}
a = int(input('что будем менять?'
          '\n танк - 1'
          '\n машину - 2'
          '\n телегу - 3'))

func[a]()

print('номер|модель|шасси?|гусеница?|скорость',
      '\n', tank_dict,
      '\n номер|модель|колёса|скорость',
      '\n', car_dict,
      '\n номер|колёса|скорость|',
      '\n', cart_dict)



#1. создаем 3 отдельных класса со следующими атрибутами:
#- Танк (модель=строка, шасси=False/True, скорость=число, гусеницы=False/True)
#- Машина (модель, колеса, скорость)
#- Телега (колеса, скорость)
#2. У каждого класса метод status, выводящий состояние объекта на данный момент.
#3. Создаем и собираем сколько-то новых объектов этих классов в список cars.
#4. Делаем несколько действий с этими объектами (Например, назначили машине "Audi" скорость 90, у танка 'Т34' сняли шасси).
#5. В конце программы выводим состояния всех объектов из cars.