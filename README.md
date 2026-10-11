# template-python-monolit

Минимальный шаблон FastAPI + Poetry + PostgreSQL + SQLAlchemy + Alembic.
Реализован один сценарий: создание пользователя с именем и IP-адресом.

## Запуск

Требуются Python 3.13, Poetry и Docker Compose.

```bash
poetry install
docker compose up -d postgres
poetry run alembic upgrade head
poetry run uvicorn src.main:app --reload
```

Приложение доступно на `http://127.0.0.1:8000`, документация API — на
`http://127.0.0.1:8000/docs`. Локальные параметры БД заданы в
`.env.example`; для своих значений скопируйте их в `.env`.

## Создание пользователя

```bash
curl -X POST http://127.0.0.1:8000/api/users \
  -H 'Content-Type: application/json' \
  -d '{"name":"Alice","ip":"127.0.0.1"}'
```

Успешный ответ: HTTP 201 с `id`, `name`, `ip` и `created_at`.
Некорректные имя и IP получают HTTP 422. Эндпоинт не реализует регистрацию
с паролем или авторизацию — для этого потребуются отдельные сценарии.
