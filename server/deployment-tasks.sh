echo $PWD
cd /usr/src/app
alembic revision --autogenerate -m"migrate" && alembic upgrade head