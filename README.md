# Kefir


Kefir: API для хранения данных пользователей.

## Требования

1. Docker ([установка](https://docs.docker.com/engine/install/))
2. Docker-compose ([установка](https://docs.docker.com/compose/install/))

## Запуск приложения

Для запуска приложения склонируйте репозиторий с проектом:

```bash
git clone git@github.com:stanbychkov1/kefir.git
````
Затем создать .env файл с переменными и заполните все поля значениями, где есть <>:
````
DJANGO_SECRET_KEY='<secret_key>'
DJANGO_DEBUG=false
DOMAIN_NAME=localhost
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=<postgres_username>
POSTGRES_PASSWORD=<postgres_password>
DB_HOST=db
DB_PORT=5432
````
После следует запустить приложение с помощью команды docker-compose, находясь в корневой папке проекта:
```bash
docker-compose up --build
````
Для вашего удобства будут созданы пробные данные с 3 обычными пользователями и один администратором. Логин и пароли можно получить в файле data/users.csv
````
Воспользуетесь Swagger, чтоб увидеть полные возможности API.\
## Основные end-points:
[localhost/admin/](localhost/admin/) - административная часть\
[localhost/swagger/](localhost/swagger/) - документация Swagger\
[localhost/redoc/](localhost/redoc/) - документация Redoc\
[localhost/api/api-auth/login/](localhost/api/api-auth/login/) - аутентификация пользователей\
[localhost/api/api-auth/logout/](localhost/api/api-auth/logout/) - разлогинивание пользователей\
[localhost/api/users/](localhost/api/users/) - доступ к списку пользователей\
[localhost/api/users/id/](localhost/api/users/id/) - доступ к данным пользователя\
