FROM python:3.10

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

COPY alembic.ini .

COPY alembic /fastapi_app/alembic

RUN pip install -r requirements.txt

COPY app/ /fastapi_app/app

COPY docker-entrypoint.sh .

RUN chmod +x /fastapi_app/docker-entrypoint.sh

CMD /fastapi_app/docker-entrypoint.sh
