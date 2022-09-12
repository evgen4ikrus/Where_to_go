# Where_to_go
Куда сходить в Москве?! Сайт с интересными местами отдыха в Москве.

Проект доступен по [ссылке](https://shesterikov3.pythonanywhere.com/).
## Установка и запуск
* Скачайте код
* Установите зависимости:
```
pip install -r requirements.txt
```
* Примените миграции:
```
python manage.py migrate
```
* Создайте файл .env в корнейвой папке проекта, определите в файле переменные окружения. Пример содержимого файла .env:
```
SECRET_KEY=h7wfbk14otyo6qs-1l3^)i9h@(qo&fcfg=e6i@k*(nvg9^fg2f
DEBUG=True
ALLOWED_HOSTS=127.0.0.1
```
Примечание: SECRET_KEY - обязательно, у остальных заданы параметры по умолчанию (DEBUG = True, ALLOWED_HOSTS = ['127.0.0.1'])
* Запустите локальный сервер:
```
python manage.py runserver
```
* Перейдите по ссылке в командной строке
