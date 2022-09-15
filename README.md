# Where_to_go
Куда сходить в Москве?! Сайт с интересными местами отдыха в Москве.

Проект доступен по [ссылке](https://shesterikov3.pythonanywhere.com/).

Панель администратора можно протестировать по [ссылке](https://shesterikov3.pythonanywhere.com/admin).
## Установка и запуск
* Скачайте код
* Установите зависимости:
```
pip install -r requirements.txt
```
* Создайте файл .env в корнейвой папке проекта, определите в файле переменные окружения. Пример содержимого файла .env:
```
SECRET_KEY=h7wfbk14otyo6qs-1l3^)i9h@(qo&fcfg=e6i@k*(nvg9^fg2f
DEBUG=True
ALLOWED_HOSTS=127.0.0.1
```
Примечание: SECRET_KEY - обязательно, у остальных заданы параметры по умолчанию (DEBUG = True, ALLOWED_HOSTS = ['127.0.0.1'])
* Примените миграции:
```
python manage.py migrate
```
* Запустите локальный сервер:
```
python manage.py runserver
```
* Перейдите по ссылке в командной строке
## Загрузка новых мест отдыха
Есть два способа загрузки новых мест:
* Через панель администратора - запустите локальный сервер и перейдите по адресу http://127.0.0.1:8000/admin

* С помощью готового json-файла, запустите команду:
```
python manage.py load_place <ссылка_на_json-файл>
```
Json-файл должен иметь вид:
```
{
    "title": "Название места отдыха",
    "imgs": [
        "Ссылка на картинку 1"
        "Ссылка на картинку 2"
        "Ссылка на картинку 3"
        ...
    ],
    "description_short": "Краткое описание",
    "description_long": "Подробное описание с html тегами",
    "coordinates": {
        "lng": "Координаты долготы",
        "lat": "Координаты широты"
    }
}
```
## Цель проекта
Код написан в образовательных целях на курсе для web-разработчиков [dvmn.org](https://dvmn.org/)
