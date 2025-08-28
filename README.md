# 📝 Django Blog with Docker

[![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?logo=docker)](https://www.docker.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap)](https://getbootstrap.com/)

A modern Django blog with support for Docker, PostgreSQL and REST API.

## 🛠 Technology stack
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

## ✨ Features
- 🐳 Docker
- 🗄️ PostgreSQL 
- 🔐 OAuth 2.0
- 📱 Adaptive design (Bootstrap 5)
- 🌐 REST API (DRF)
- ✉️ SMTP mailing list (Yandex)
- 🏷️ Tag system (django-taggit)

## 🚀 Quick start

### Requirements
- Docker 24.0+
- Docker Compose 2.0+
- Python 3.11

### Installation
```bash
git clone https://github.com/yourusername/django-blog.git
cd app-name
cp .env.example .env
docker-compose up --build -d
```

### First-step Installation

```bash
# Apply migrations
docker-compose exec web python manage.py migrate

# Create admin
docker-compose exec web python manage.py createsuperuser

# Load data
docker-compose exec web python manage.py loaddata mysite_data.json
```

```
## Local launch

```python

pip install -r requirements.txt

sudo -u postgres psql -c "CREATE DATABASE blog;"
sudo -u postgres psql -c "CREATE USER bloguser WITH PASSWORD 'blogpass';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE blog TO bloguser;"

echo "SECRET_KEY=your-secret-key" > .env
echo "DEBUG=True" >> .env
echo "POSTGRES_DB=postgres://user:pass@localhost:5432/blogdb" >> .env
echo "POSTGRES_USER=admin" >> .env
echo "POSTGRES_USER=admin" >> .env
echo "POSTGRES_PASSWORD=admin" >> .env
echo "DB_HOST=localhost" >> .env
echo "DB_PORT=5432" >> .env

# For OAuth 2.0, fill into .env GITHUB_KEY, GITHUB_SECRET, GOOGLE_KEY, GOOGLE_SECRET 

python manage.py migrate

python manage.py runserver
```
