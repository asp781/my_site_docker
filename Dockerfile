# Создать образ на основе базового слоя python (там будет ОС и интерпретатор Python).
# 3.7 — используемая версия Python.
# slim — обозначение того, что образ имеет только необходимые компоненты для запуска,
# он не будет занимать много места при развёртывании.
FROM python:3.11-slim

# Запустить команду создания директории внутри контейнера
RUN mkdir /app

# Скопировать с локального компьютера файл зависимостей
# в директорию /app.
COPY requirements.txt /app

# Выполнить установку зависимостей внутри контейнера.
RUN pip3 install -r /app/requirements.txt --no-cache-dir

# Скопировать содержимое директории /api_yamdb c локального компьютера
# в директорию /app.
COPY ekranstroy/ /app

# Сделать директорию /app рабочей директорией.
WORKDIR /app

# Выполнить запуск сервера разработки при старте контейнера.
# CMD ["python3", "manage.py", "runserver", "0:8000"]
CMD ["gunicorn", "ekranstroy.wsgi:application", "--bind", "0:8000" ]

# docker build -t ekranstroy .
# docker run --name my_site -it -p 8000:8000 ekranstroy

# docker exec -it my_site_docker-web-1 bash

# docker build -t asp781/ekranstroy:v10.01.2024 .
# docker login -u asp781
# docker push asp781/ekranstroy:v10.01.2024
