flask clear-migration-versions
flask seed
alembic revision --autogenerate -m"migrate" && alembic upgrade head