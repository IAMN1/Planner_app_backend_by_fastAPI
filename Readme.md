# Planner App Backend (FastAPI)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Coverage](https://img.shields.io/badge/Coverage-94%25-brightgreen?style=for-the-badge)

Серверная часть приложения для управления задачами с использованием FastAPI и MongoDB. Проект обеспечивает высокую производительность, асинхронную обработку запросов и включает 94% тестовое покрытие.

## Ключевые особенности

- **Полный CRUD функционал** для управления задачами
- **JWT аутентификация** с защищенными эндпоинтами
- **Валидация данных** через Pydantic схемы
- **Асинхронное взаимодействие** с MongoDB
- **Автогенерация документации** (Swagger/ReDoc)
- **Комплексное тестирование** с использованием pytest
- **Контейнеризация** через Docker

## Технологический стек

### Основные компоненты
- **Python 3.10+**
- **FastAPI** - высокопроизводительный веб-фреймворк
- **MongoDB** - NoSQL база данных
- **Motor** - асинхронный драйвер MongoDB
- **Pydantic** - валидация данных и сериализация
- **JWT** - аутентификация через JSON Web Tokens

### Тестирование
- **Pytest** - фреймворк для тестирования
- **HTTPX** - асинхронный HTTP клиент
- **Coverage.py** - анализ покрытия кода тестами

### Вспомогательные инструменты
- **Poetry** - управление зависимостями
- **Docker** - контейнеризация приложения
- **GitHub Actions** - CI/CD пайплайн
- **pre-commit hooks** - автоматические проверки кода

## Установка и запуск

### Предварительные требования
- Python 3.10+
- MongoDB 5.0+


### Пошаговая инструкция

1. Клонируйте репозиторий:
```bash
git clone https://github.com/IAMN1/Planner_app_backend_by_fastAPI.git
cd Planner_app_backend_by_fastAPI
```
2. Установите зависимости из requirements.txt
```bash
pip install -r requirements.txt
```
3. Настройте окружение
```bash
cp .env.example .env
# Отредактируйте .env при необходимости
```
4. Запустите приложение
```bash
python main.py
```

### Тестирование
1. Запуск тестов с отчетом о покрытии
```bash
pytest
```
2. Генерация отчета о покрытии
```bash
coverage run -m pytest
coverage report
```

### Docker
1. Соберите образ
```bash
docker build -t planner-backend .
```

## 📜 Лицензия
Этот проект распространяется под лицензией [Apache 2.0](LICENSE).  
Copyright © [2025] [IAMN1]
