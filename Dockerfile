# Используем более свежую версию Python
FROM python:3.11-slim-bookworm

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем директорию для приложения
RUN mkdir /app

# Устанавливаем рабочую директорию
# WORKDIR /app

# Копируем requirements.txt
COPY requirements.txt /app

# Устанавливаем зависимости
RUN pip3 install -r /app/requirements.txt --no-cache-dir

# Копируем все файлы приложения
# COPY . /app/
COPY ekranstroy/ /app

# Сделать директорию /app рабочей директорией.
WORKDIR /app

# Команда для запуска Gunicorn + Daphne
# CMD ["sh", "-c", "daphne -b 0.0.0.0 -p 8000 ekranstroy.asgi:application"]
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "ekranstroy.asgi:application"]
