# Описание структуры 

1. `docker_compose` — настройка Nginx, Docker и Django.
2. `django_api` — реализация API для выдачи информации о фильме.


## Первичный запуск
- необходимо произвести первичные миграции
> - python manage.py migrate 
- создать суперюзера
> - python manage.py createsuperuser 
- и собрать статику
> - python manage.py collectstatic 
# Для первичного наполнения данными 
> - cd sqlite_to_postgres
> - python load_data.py 

