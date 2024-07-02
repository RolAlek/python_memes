# python_memes
Приложение для загрузки/просмотров мемов.

## Используемые технологии:
* Python 3.10
* FastAPI - приватный/публичный API.
* Celery(RabbitMQ:Redis) - работа с S3-Minio
* Minio - S3-хранилище.
* PostgreSQL
* Docker

### Установка и запуск
### Для разработки и теста:

1. Клоинируйте git-репозиторий с проектом,
2. Находясь в корневой директории проекта установите и активируйте виртуальное окружение:

    Для пользователей с ОС Unix-семейства:
    ```bash
    python3.10 -m venv <ваше_название>
    source <ваше_название>/bin/activate
    ```
    Если вам не повезло и вы пользователь Windows:
    ```bash
    python3.10 -m venv <ваше_название>
    source <ваше_название>/Scripts/activate
    ```
3. Вносите свои измения, работайте с кодовой базой, предварительно не забудьте обновит пакетный мэнеджер pip и установить зависимости из `requirements.txt`:
    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. Создайте в корне проекта файл с переменными окружения `.env`
    ```
    PUBLIC_APP__SERVICE_URL=http://private:8001/services/

    PRIVATE_APP__DB__URL=postgresql+asyncpg://<user>:<password>@<localhost/db>:5432/<название_бд>
    PRIVATE_APP__DB__ECHO=0
    PRIVATE_APP__MINIO__ENDPOINT=minio:9000
    # Предварительно за пустите сервер с minio и во вкладке Keys создайте ключи безопасности и сохраните их ниже
    PRIVATE_APP__MINIO__ACCESS_KEY=<ваш_access_key>
    PRIVATE_APP__MINIO__SECRET_KEY=<ваш_secret_key>
    PRIVATE_APP__MINIO__BUCKET=memes-bucket
    PRIVATE_APP__CELERY__BROKER=amqp://<ваш_пользователь>:<ваш_пароль>@<host>:<5672>//
    PRIVATE_APP__CELERY__BACKEND=rpc://

    #INIT POSGRESQL:
    POSTGRES_USER=<ваш_пользователь>
    POSTGRES_PASSWORD=<ваш_пароль>
    POSTGRES_DB=<название_БД>
    # INIT MINIO:
    MINIO_ROOT_USER=<ваш_пользователь>
    MINIO_ROOT_PASSWORD=<ваш_пароль>
    # RABBITMQ
    RABBITMQ_DEFAULT_USER=<ваш_пользователь>
    RABBITMQ_DEFAULT_PASS=<ваш_пароль>
    # Инструкция для расширения хранилища для кролика
    RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS=-rabbit disk_free_limit 2147483648
    ```
5. А можно просто установить docker-демона и запустить все контейнеры простым: docker-compose up 🙃 и перейти по http://0.0.0.0:8000/docs#/ - для доступа к документации публичного API или http://0.0.0.0:8001/docs#/ - для доступа к документации приватного API.