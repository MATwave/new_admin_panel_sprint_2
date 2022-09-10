#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"


echo "uwsgi --strict --ini uwsgi.ini"
uwsgi --strict --ini uwsgi.ini




