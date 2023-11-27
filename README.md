# Дипломная работа. Профессия python-разработчик

## Описание проекта
Данный проект представляет собой backend-часть для сайта объявлений.
Frontend-часть уже готова.

Был реализован следующий функционал:
- авторизация и аутентификация пользователей;
- распределение ролей между пользователями (пользователь и админ);
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои);
- под каждым объявлением пользователи могут оставлять отзывы;
- в заголовке сайта можно осуществлять поиск объявлений по названию.

### Стек технологий: 
 - Python 3.1x, 
 - Django,
 - DRF,
 - PostgreSQL,
 - CORS,
 - Swagger,
 - Unittest,
 - Flake8.

<h3>Запуск проекта</h3>

1. Создать виртуальное окружение
`python3 -m venv venv`
2. Активировать виртуальное окружение
- `venv/Scripts/activate (Windows)`
- `source venv/bin/activate (Linux, MacOS)`
3. Установить зависимости
`pip install -r requirements.txt`
4. Создать файл .env c переменными окружения
5. Добавить в файл настройки, как в .env.sample и заполнить их.
6. Поднять контейнеры:
`docker-compose up -d`
7. Создать и накатить миграции:
 - `python skymarket/manage.py makemigrations`
 - `python skymarket/manage.py migrate`
8. Заполнить Базу Данных:
- `python skymarket/manage.py loaddata skymarket\fixtures\users.json`
- `python skymarket/manage.py loaddata skymarket\fixtures\ad.json`
- `python skymarket/manage.py loaddata skymarket\fixtures\comments.json`
9. Запустить сервер
- `python skymarket/manage.py runserver`