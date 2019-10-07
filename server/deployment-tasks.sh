flask clear-migration-versions
alembic revision --autogenerate -m"migrate" && alembic upgrade head