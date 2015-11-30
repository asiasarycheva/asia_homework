__author__ = 'asiaptichka'
#unicode=utf-8

import sys, pickle



#создаём файл для записи
f = open('data.pickle', 'wb')
s = open('data_dict.pickle', 'wb')
d = open('data_distance.pickle', 'wb')
#создаём рабочий лист
lst = []
dict = {}
distlst = {}
pickle.dump(lst, f)
pickle.dump(dict, s)
pickle.dump(distlst, d)
f.close()
s.close()
d.close()


# Делаем отдельные функции:
# ввод команды, проверка теперь включена (чтобы не разводить функции)
def input_command():

    glacier = str(input('введите ледник '))
    while not glacier.isalpha():
        print('буквы!')
        glacier = str(input('введите ледник '))
    else:
        pass
        country = str(input('введите страну '))
        while not country.isalpha():
            print('буквы!')
            country = str(input('введите страну '))
        else:
            pass
            area = str(input('введите площадь '))
            while not area.isdigit():
                print('цифры!')
                area = str(input('введите площадь '))
            else:
                global lst
                n = len(lst)
                lst = lst + [(n+1, glacier, country, area)]
                print(lst)
                print('каковы координаты ледника?')
                x = input('по оси Х ')
                y = input('по оси Y ')
                global dict
                dict2 = {n+1: (x, y)}
                dict.update(dict2)
                print(dict)


# запись в пикл
def input_pickle():

    try:
        f = open('data.pickle', 'ab')
    except FileNotFoundError:
        f = open('data.pickle', 'wb')
    else:
        print('имеется прошлая база ледников. дозапишем!')
        f = open('data.pickle', 'ab')
    finally:
        f = open('data.pickle', 'wb')
        pickle.dump(lst, f)
        f.close()
        pass

# вычленение из пикла
def output_pickle():
    f = open('data.pickle', 'rb')
    a = pickle.load(f)
    f.close()
    print(a)
    return a

# сортировка
def sort_area():
    a = output_pickle()
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
def sort_country():
    a = output_pickle()
    finallst = []
    p = str(input('введите страну'))
    n = len(a)
    for i in range(n):
        b = a[i][1]
        if str(b) == p:
            finallst = finallst + [a[i]]
    print(finallst)


# сортировка-3
def sort_glacier():
    a = output_pickle()
    finallst = []
    p = str(input('введите название ледника'))
    n = len(a)
    for i in range(n):
        b = a[i][0]
        if b.find(p) is True:
            finallst = finallst + [a[i]]
        else:
            pass
    print(finallst)

def stop():
    print('конец')
    return sys.exit()

def edit_data():
    f = open('data.pickle', 'rb')
    a = [pickle.load(f)]
    f.close()
    print('какой номер ледника изменить?')
    print(a)
    c = int(input('я хочу удалить номер '))
    print('введите строчку взамен')
    lst = []
    input_command()
    f = open('data.pickle', 'wb')
    a2 = a[:c-1] + lst + a[c+1:]
    pickle.dump(a2, f)

def move_glacier():
    f = open('data.pickle', 'rb')
    a = pickle.load(f)
    f.close()
    print('какой ледник подвинуть? ')
    print(a)
    c = int(input('я хочу передвинуть номер '))
    print(c)
    print('он был на позиции')
    print(dict[c])
    x2 = int(input('по оси х он теперь на '))
    y2 = int(input('по оси y он теперь на '))

    d = open('data_distance.pickle', 'wb')

    q1 = int(dict[c][0])
    w1 = int(dict[c][1])

    distance = (((q1 - x2)**2) + (w1 - y2)**2)**0.5

    try:

        distanceold = int(distlst[a[c-1[1]]])

    except TypeError:

        distanceold = 0

    else:
        print('ледник уже передвигался')

    finally:

        new_distanse = distanceold + distance
        distlst2 = {a[c-1]: new_distanse}
        distlst.update(distlst2)
        print(distlst)
        pickle.dump(distlst, d)
        d.close()




func = {
'1':input_command,
'2':input_pickle,
'3':output_pickle,
'4':sort_area,
'5':sort_glacier,
'6':sort_country,
'7':edit_data,
'8':move_glacier,
'9':stop

}

print('\n 1 - ввести данные '
      '\n 2 - записать в файл '
      '\n 3 - вывести записанные данные '
      '\n 4 - выбрать ледники с площадью больше.. '
      '\n 5 - выбрать ледники с названием... '
      '\n 6 - выбрать ледники страны...'
      '\n 7 - выйти из программы')

a = input('введите команду')

while a in func:
    func[a]()
    a = input('введите команду')
else:
    print('неверно')
    pass


# 1. ищем хотя бы 2 места в своей программе, где удобно воспользоваться try - except (задаем полную конструкцию try-except-else-finaly)

# 2. обрабатываем исключения, защищаясь от ошибок

# 3. при этом программу делим на модули:

# папка cars/
# main.py - сама программа. В main.py предусмотреть возможность его импортирования
# db.py - чтение и запись данных
# debug.py - вывод на экран
