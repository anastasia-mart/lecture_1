# Лабораторная работа №6: Dockerize Python приложение

## Запуск
```bash
docker build . -t healthcheck-app:latest
docker run -d -p 8080:8080 healthcheck-app:latest
curl http://localhost:8080/healthcheck
