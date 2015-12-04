__author__ = 'asiaptichka'
#unicode=utf-8

class Animal:

    def __init__(self, k, p, v):
        self.kids = k
        self.product = p
        self.voice = v

    def kids(self):
        print('количество прибывших', self.kids)
        n_kids = input('')
        return n_kids
    def product(self):
        print('количество произведённых ', self.product)
        n_product = input('')
        return n_product

    def voice(self):
        return print(self.voice)

class Duck(Animal):

    def status(self):
        a = str(Animal.kids(self))
        b = str(Animal.product(self))
        c = 'кря-кря'
        print('В нашем полку прибыло\n', a, 'утят \n',
              b, ' яиц \n', c, '!')
        return [a, b, c]



class Cow(Animal):

    def status(self):
        a = str(Animal.kids(self))
        b = str(Animal.product(self))
        c = 'му-му'
        print('В нашем полку прибыло\n', a, 'телят \n', b, ' молока \n', c, '!')
        return [a, b, c]

class Dog(Animal):

    def status(self):
        a = str(Animal.kids(self))
        b = str(Animal.product(self))
        c = str(Animal.voice(self))
        print('В нашем полку прибыло\n', a, 'щенят \n',
              'поймано ', b, ' вредных лис \n', c, '!')
        return [a, b, c]

class Farm:
    def __init__(self):
        self.quantity_duck = int(input('введите количество уток'))
        self.quantity_cow = int(input('введите количество коров'))
        self.quantity_dog = int(input('введите количество собак'))


Farm = Farm()

kid_report = {'duckling': 0, 'calf': 0, 'puppy': 0}
product_report = {'eggs': 0, 'milk': 0, 'fox': 0}

duck_report = {}

try:
    Duck = Duck('утята', 'яйца', 'кря-кря')
    for i in range(Farm.quantity_duck):
        duck_report2 = {
            i: Duck.status()}
        duck_report.update(duck_report2)
        lst = Duck.status()
        a = kid_report['duckling']
        b = product_report['eggs']
        kid_report['duckling'] = a + int(lst[0])
        product_report['eggs'] = b + int(lst[1])
except TypeError:
    pass

cow_report = {}
try:
    Cow = Cow('телята', 'молоко', 'му-му')
    for i in range(Farm.quantity_cow):
        cow_report2 = {i: Cow.status()}
        cow_report.update(cow_report2)
        lst = Cow.status()
        a = kid_report['calf']
        b = product_report['milk']
        kid_report['calf'] = a + int(lst[0])
        product_report['milk'] = b + int(lst[1])

except TypeError:
    pass

dog_report = {}
try:
    Dog = Dog('щенята', 'пойманные лисы', 'гав-гав')
    for i in range(Farm.quantity_dog):
        dog_report2 = {i: Dog.status()}
        dog_report.update(dog_report2)
        lst = Dog.status()
        a = kid_report['puppy']
        b = product_report['fox']
        kid_report['puppy'] = a + int(lst[0])
        product_report['fox'] = b + int(lst[1])

except TypeError:
    pass

print(duck_report)
print(kid_report)
print(product_report)





#Создаем программу-модуль "Жизнь на ферме" с набором классов:

#- Утка
#- Корова
#- Собака

#1. У этих классов есть следующие функциональности (нужные в работе методы нужно придумать):

#- бежать
#- голос
#- продукт - молоко (или яйцо...)
#Все эти классы отнаследованы от базового "Животное".

#2. Также нужен класс Ферма.
#Программа инициализирует ферму с заданным числом каждого животного.

#3. Далее запускается метод класса Ферма "прошелМесяц".
#Там циклом проходим по всем животным, запуская их собственный метод "прошелМесяц" (какое животное сколько раз делает продукт, как успешно, где использовать random, какие случайные факторы внести в жизнь фермы, решайте сами).

#4. Далее запускается метод класса Ферма "своднаяИнформация", который расскажет нам об изменениях на ферме.