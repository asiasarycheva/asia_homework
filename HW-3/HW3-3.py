__author__ = 'asiaptichka'
import os, re, pickle


#вводим переменные, включающие в себя все цифры, либо все буквы
patternint = '[0-9]+'
patternengint = '[a-z, A-Z, 0-9]+'

#вводим пустые списки для заполняемых данных. при каждом запуске они обнуляются. если файл пикл уже создан, можно использовать функцию load
glacierlst = []
countrylst = []
arealst = []

#переменная для понимания дальнейшего дейстивя (продолжить запись в пикл или же вывести результат)
answer = 1

while answer == 1:

        glacier = str(input('введите название ледника на русском ')) #вводим название ледника на русском.

        while re.match(patternengint, glacier): #если же присутствуют другие символы - программа попросит повторить действие

            print('по-русски и без цифр! ')
            glacier = str(input('введите название ледника на русском '))
        else:
            glacierlst = glacierlst + [glacier] #если всё верно - список пополнится на одну строчку

#то же самое для страны, где располагается ледник

        country = str(input('введите страну ледника на русском '))

        while re.match(patternengint, country):
            print('по-русски и без цифр! ')
            country = str(input('введите страну ледника на русском '))
        else:
          countrylst = countrylst + [country]

#то же самое для площади ледника

        area = str(input('введите площадь ледника на русском '))

        while re.match(patternint, area) == False:
            print('только цифры! ')
            area = str(input('введите площадь ледника на русском '))
        else:
            arealst = arealst + [area]     #проверяем дальнейшие действия - ввести новый ледник или же вывести желаемый результат?


        answer = int(input ('ввести новый ледник (1) или вывести результат (2) ?' ))
#выводим результат - сортировка по имени Ледника

f = open('data.pickle', 'wb')

#то, что записали в список до этого, записываем в открытый файл пикл
pickle.dump(glacierlst, f)
pickle.dump(countrylst, f)
pickle.dump(arealst, f)

f.close()

#открываем для чтения файл пикл
f = open('data.pickle', 'rb')

#загружаем записанные ранее объекты
glacierlst = pickle.load(f)
countrylst = pickle.load(f)
arealst = pickle.load(f)

f.close()

#формируем новый список - разбиваем ледники, страну и площадь на состовляющие и записываем каждый соответствующий друг другу элемент в одну строку
n = len(countrylst)
for i in range (n):

#отбираем ледники лишь с определённой страной

    a = countrylst[i]
    if a == 'Исландия':
        finallst = [glacierlst[i] + ' ' + countrylst[i] + ' ' + arealst[i]]
        print(finallst)