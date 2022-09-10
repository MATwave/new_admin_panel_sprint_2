# Описание структуры 

1. `docker_compose` — настройка Nginx, Docker и Django.
2. `django_api` — реализация API для выдачи информации о фильме.


## Первичный запуск
- запустим докеры
> - docker compose up -d --build
- перейдем внутрь контейнера с джангой
> - docker exec -it <id контейнера с джангой> bash
- и произведем первичные миграции
> - python manage.py migrate 
- создадим суперюзера
> - python manage.py createsuperuser 
- и соберем статику
> - python manage.py collectstatic 
# Для первичного наполнения данными 
- перейдем в папку
> - cd sqlite_to_postgres
- запустим скрипт
> - python load_data.py 

