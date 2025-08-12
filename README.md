# 📝 Django Blog with Docker

[![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?logo=docker)](https://www.docker.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap)](https://getbootstrap.com/)

Современный блог на Django с поддержкой Docker, PostgreSQL и REST API.

## 🛠 Технологический стек
#### Backend
- Django 5.2
- Django REST Framework
- Gunicorn
- PostgreSQL 16
- Psycopg2
- Social Auth

#### Frontend
- Bootstrap 5
- HTML5/CSS3
- Django Templates

## ✨ Особенности
- 🐳 Полная Docker-контейнеризация
- 🗄️ PostgreSQL как основная СУБД
- 🔐 Аутентификация через соцсети (GitHub/Google)
- 📱 Адаптивный дизайн (Bootstrap 5)
- 🌐 REST API (DRF)
- ✉️ SMTP-рассылка (Yandex)
- 🏷️ Система тегов (django-taggit)

## 🚀 Быстрый старт

### Требования
- Docker 24.0+
- Docker Compose 2.0+
- Python 3.11

### Установка
```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog
cp .env.example .env  # заполните настройки
docker-compose up --build -d
```

### Первоначальная настройка

```bash
# Применить миграции
docker-compose exec web python manage.py migrate

# Создать администратора
docker-compose exec web python manage.py createsuperuser

# Загрузить тестовые данные
docker-compose exec web python manage.py loaddata mysite_data.json
```

### Структура проекта
```bash
├── accounts/          # Аутентификация и пользователи
├── blog/              # Основное приложение блога
├── blog_api/          # REST API endpoints
├── mysite/            # Конфигурация проекта
├── templates/         # HTML шаблоны
├── media/             # Загружаемые файлы
├── .env               # Конфигурационные переменные
├── Dockerfile         # Конфигурация Docker
└── docker-compose.yml # Оркестрация сервисов
```
## Локальный запуск

```python
# Установка зависимостей
pip install -r requirements.txt

# Настройка .env файла
echo "SECRET_KEY=your-secret-key" > .env
echo "DEBUG=True" >> .env
echo "DB_URL=postgres://user:pass@localhost:5432/blogdb" >> .env

# Запуск миграций
python manage.py migrate

# Запуск сервера
python manage.py runserver
```
