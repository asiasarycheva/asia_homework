__author__ = 'asiaptichka'
#unicode=utf-8

import os


def find(d, end):
    os.chdir(d)
    for filename in os.listdir('.'):
       if filename.endswith(end):
           for i, line in enumerate(open(filename)):
               yield filename,i, line

#Функция-генератор grep

def grep (generator, w):
    for name, i, s in generator:
        if w in s:
            yield name, i, s

#Запрос строки для поиска

#Выводятся наименование файла; № строки и сама строка(где есть введеная строка для поиска)


end = input('искать в файлах ')
d = input('искать в папке  ')
w = input('искать слово ')

for name, i, s in grep(generator=find(d, end), w=w):
    print(name, i, s)





#Помните поиск слова "python"?

#1. Создайте функцию-генератор find, которая будет заходить в директорию и рекурсивно бежать по всем файлам и папкам, то есть:

#Смотрит содержимое папки.
#Читает содержимое каждого файла с заданным расширением (например, txt) - по очереди.
#Выдает через yield имя файла, номер строки и строку.
#2. Создать функцию-генератор grep, которая будет получать на вход генератор и фильтровать его по вхождению строки, то есть:

#На входе генератор и искомая подстрока.
#По циклу - если в текущей строке найдена подстрока, то по yield выводит имя файла, номер строки и строку.
#3. Сделайте программу, ищущую с помощью этих 2-ух генераторов строки в файлах с расширением .py, в которых встречается, например, определенный тип исключений "TypeError" или, например, инструкция "def".

#*4. Таким образом можно работать с входными параметрами программы:

#import argparse

#parser = argparse.ArgumentParser(description='Process some integers.')

#parser.add_argument('integers', metavar='N', type=int, nargs='+',
#help='an integer for the accumulator')

#parser.add_argument('--sum', dest='accumulate', action='store_const',
#const=sum, default=max,
#help='sum the integers (default: find the max)')

#args = parser.parse_args()
#print(args.accumulate(args.integers))

#В этом примере программу можно будет запустить, например, так:
#python prog.py 1 2 3 4

#или так:
#python prog.py 1 2 3 4 —sum