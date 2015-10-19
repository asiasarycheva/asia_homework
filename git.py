import sys

git clone https://github.com/asiasarycheva/asia_homework.git #первый раз клонируем репозиторий в папке появились файлы

git add file.py #добавили файл в локальный репозиторий
#есть изменение
git commit -a -m "добавили файл file.py" #сохраняем репозиторий с комментом в локальном 
git push origin master #отправит ветку master нашего репозитория на сервер origin
