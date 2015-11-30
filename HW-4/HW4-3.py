__author__ = 'asiaptichka'
#unicode=utf-8

import sys, os, pickle



#создаём файл для записи
f = open('data.pickle', 'wb')
#создаём рабочий лист
lst = []
pickle.dump(lst, f)

f.close()

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
                lst = lst + [(glacier, country, area)]
                return print(lst)




# запись в пикл
def input_pickle():

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
    n = len(a)
    print(n)
    for i in range(n):
        print(i, a[i])
    c = int(input('я хочу удалить номер '))
    print('введите строчку взамен')
    lst = []
    input_command()
    f = open('data.pickle', 'wb')
    a2 = a[:c-1] + lst + a[c+1:]
    pickle.dump(a2, f)




func = {
'1':input_command,
'2':input_pickle,
'3':output_pickle,
'4':sort_area,
'5':sort_glacier,
'6':sort_country,
'7':edit_data,
'8':stop
}

print('\n 1 - ввести данные '
      '\n 2 - записать в файл '
      '\n 3 - вывести записанные данные '
      '\n 4 - выбрать ледники с площадью больше.. '
      '\n 5 - выбрать ледники с названием... '
      '\n 6 - выбрать ледники страны...'
      '\n 7 - редактировать...'
      '\n 8 - выйти из программы')

a = input('введите команду')

while a in func:
    func[a]()
    a = input('введите команду')
else:
    print('неверно')
    pass


#3. Добавляем в программу логику "Редактировать" для изменения уже введенных данных, а также "Удалить". Как с помощью функций сократить программный код в этом случае?

