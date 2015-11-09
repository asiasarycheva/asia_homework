import os, re, pickle


patternint = '[0-9]+'
patternengint = '[a-z, A-Z, 0-9]+'

glacierlst = []
countrylst = []
arealst = []

answer = 1

while answer == 1:

    glacier = str(input('введите название ледника на русском '))

    while re.match(patternengint, glacier):
               print('по-русски и без цифр! ')
               glacier = str(input('введите название ледника на русском '))              
    else:
               glacierlst = glacierlst + [glacier]

    country = str(input('введите страну ледника на русском '))
    
    while re.match(patternengint, country):
        print('по-русски и без цифр! ')
    else:
        countrylst = countrylst + [country]

    area = str(input('введите площадь ледника на русском '))
    if re.match(patternint, area):
        arealst = arealst + [area]
    else:
            print('только цифры! ')
    
    answer = int(input ('ввести новый ледник (1) или вывести результат (2) ?' ))

else:
    
    f = open('data.pickle', 'wb')

    pickle.dump(glacierlst, f)
    pickle.dump(countrylst, f)
    pickle.dump(arealst, f)

    f.close()


    f = open('data.pickle', 'rb')
    
    glacierlst = pickle.load(f)
    countrylst = pickle.load(f)
    arealst = pickle.load(f)

    f.close()

    n = len(countrylst)
    for i in range (n):
        finallst = [glacierlst[i] + ' ' + countrylst[i] + ' ' + arealst[i]]
        sortedfinallst = sorted(finallst)
    
        print(sortedfinallst)
        
