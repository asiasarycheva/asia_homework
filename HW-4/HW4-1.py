#unicode=utf-8

import os, re, pickle

lst = []


# Делаем отдельные функции:


# ввод команды
def input_command(b):
    if b == 1:
        a = input('введите ледник ')

    if b == 2:
        a = input('введите страну ')

    if b == 3:
        a = input('введите площадь ')

    return a


# проверка на соответствие цифрам
def check_func_let(a):
    engint = '[0-9]+'
    while re.match(engint, a):
        return print('буквы!')
    else:
        return True


# проверка на соответствие буквам
def check_func_int(a):
    let = '[a-z, A-Z, а-я, А-Я]+'
    while re.findall(let, a):
        return print('цифры!')
    else:
        return True


# запись в пикл
def input_pickle(a):
    f = open('data.pickle', 'wb')
    pickle.dump(a, f)
    f.close()
    pass


# вычленение из пикла
def output_pickle(a):
    f = open('data.pickle', 'rb')
    a = pickle.load(f)
    f.close()
    return a


# сортировка
def sort_area(a):
    output_pickle(a)
    finallst = []
    p = int(input('введите минимальную площадь'))
    n = len(a)
    for i in range(n):
        b = a[i][2]
        if int(b) > p:
            finallst = finallst + [a[i]]
        else:
            pass
        print(finallst)


# сортировка-2
def sort_country(a):
    output_pickle(a)
    finallst = []
    p = str(input('введите страну'))
    n = len(a)
    for i in range(n):
        b = a[i][1]
        if str(b) == p:
            finallst = finallst + [a[i]]
        print(finallst)


# сортировка-3
def sort_glacier(a):
    output_pickle(a)
    finallst = []
    p = str(input('введите название ледника'))
    n = len(a)
    for i in range(n):
        b = a[i][0]
        if b.find(p) == p:
            finallst = finallst + [a[i]]
        print(finallst)


# сам код
answer = input('Выберете команду:'
               '\n ввести ещё данные - 1'
               '\n поиск по площади - 2'
               '\n поиск по стране - 3'
               '\n поиск по названию ледника - 4')

while int(answer) == 1:

    glacier = str(input_command(1))
    while check_func_let(glacier) != True:
        glacier = str(input_command(1))

    country = str(input_command(2))
    while check_func_let(country) != True:
        country = str(input_command(2))

    area = str(input_command(3))
    while check_func_int(area) != True:
        area = str(input_command(3))

    lst = lst + [[glacier] + [country] + [area]]
    input_pickle(lst)

    print(lst)


    answer = input('Выберете команду:'
                   '\n ввести ещё данные - 1'
                   '\n поиск по площади - 2'
                   '\n поиск по стране - 3'
                   '\n поиск по названию ледника - 4')

while int(answer) == 2:
    sort_area(lst)

    answer = int(input('Выберете команду:'
                       '\n ввести ещё данные - 1'
                       '\n поиск по площади - 2'
                       '\n поиск по стране - 3'
                       '\n поиск по названию ледника - 4'))

while int(answer) == 3:
    sort_country(lst)

    answer = input('Выберете команду:'
                   '\n ввести ещё данные - 1'
                   '\n поиск по площади - 2'
                   '\n поиск по стране - 3'
                   '\n поиск по названию ледника - 4')

while int(answer) == 4:
    sort_glacier(lst)

    answer = input('Выберете команду:'
                   '\n ввести ещё данные - 1'
                   '\n поиск по площади - 2'
                   '\n поиск по стране - 3'
                   '\n поиск по названию ледника - 4')

#1. Берем задачу из дз №3. Выделяем следующие процессы в функции:
#- ввод команды - отдельная функция
#- сообщение в случае ошибки ввода команды - отдельная функция
#- Ввести и Вывести - 2 отдельные функции
#- поиски по условию - 3 отдельные функции соответственно
#- сохранение в pickle и загрузка из pickle - 2 отдельные функции

