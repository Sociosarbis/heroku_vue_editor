FROM node:10.16-alpine as build-client
WORKDIR /usr/src/app
COPY client/package.json client/package-lock.json ./
RUN npm install
COPY client .
RUN npm run build

FROM nginx:1.16-alpine as build-server
WORKDIR /usr/src/app
RUN apk update && apk add --no-cache python3 && \
  python3 -m ensurepip && \
  rm -r /usr/lib/python*/ensurepip && \
  if [ ! -e /usr/bin/pip ] ; then ln -s pip3 /usr/bin/pip ; fi && \
  if [ ! -e /usr/bin/python ] ; then ln -sf /usr/bin/python3 /usr/bin/python ; fi && \
  if [ -e /root/.cache ] ; then rm -r /root/.cache ; fi
RUN apk update && apk add curl postgresql-dev gcc python3-dev musl-dev libffi-dev
COPY --from=build-client /usr/src/app/dist /usr/share/nginx/html
COPY --from=build-client /usr/src/app/nginx.conf /etc/nginx/conf.d/default.conf
COPY server/requirements.txt ./
RUN pip install -r requirements.txt && alembic init alembic
ENV PYTHONPATH=. \
  FLASK_APP=app \
  DB_HOST=host.docker.internal
COPY server/template.env.py alembic/env.py
COPY server .
EXPOSE 80
CMD gunicorn -c "python:config.gunicorn" app:app --daemon && \
  sed -i -e "s/\$PORT/${PORT}/g" /etc/nginx/conf.d/default.conf && \
  nginx -g "daemon off;"