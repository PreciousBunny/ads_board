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

1. Установить локально на свой компьютер Python версией не ниже 3.10.x!
2. Клонировать файлы проекта с GitHub репозитория.
3. Создать виртуальное окружение:
- `python3 -m venv venv`
4. Активировать виртуальное окружение:
- `venv/Scripts/activate (Windows)`
- `source venv/bin/activate (Linux, MacOS)`
5. Установить зависимости:
- `pip install -r requirements.txt`
6. Создать файл .env c переменными окружения.
7. Добавить в файл настройки, как в .env.sample и заполнить их.
8. Поднять контейнеры:
- `docker-compose up -d`
9. Создать и накатить миграции:
 - `python skymarket/manage.py makemigrations`
 - `python skymarket/manage.py migrate`
10. Заполнить базу данных:
- `python skymarket/manage.py loaddata skymarket\fixtures\users.json`
- `python skymarket/manage.py loaddata skymarket\fixtures\ad.json`
- `python skymarket/manage.py loaddata skymarket\fixtures\comments.json`
11. Запустить сервер:
- `python skymarket/manage.py runserver`