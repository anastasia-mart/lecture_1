# Лабораторная работа 5: Book Collection API

## Описание
Простое API для управления коллекцией книг на FastAPI и SQLAlchemy.

## Функционал
1. Добавление книги: POST /books/
2. Получение всех книг: GET /books/
3. Получение книги по ID: GET /books/{id}
4. Обновление книги: PUT /books/{id}
5. Удаление книги: DELETE /books/{id}
6. Поиск книг: GET /books/search/

## Установка и запуск
1. `pip install -r book_api/requirements.txt`
2. `cd book_api`
3. `uvicorn main:app --reload`
4. Откройте: http://127.0.0.1:8000/docs
