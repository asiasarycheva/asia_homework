import os

for filename in os.listdir('.'): #ищем в папке, в которой сохранён код,все файлы
    if filename.find ('python') != -1: #используем оператор find для поиска слова в названии файла. истине соответствует значение не "-1"

        print (filename) 



