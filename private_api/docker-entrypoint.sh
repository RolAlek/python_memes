!#/bin/bash

chmod +x /fastapi_app/docker-entrypoint.sh

# cd app
echo "Applying Alembic migrations..."
if alembic upgrade head; then
    echo "Starting Celery worker..."
    celery -A app.services.celery.tasks:app worker --loglevel=info &
    celery -A app.services.celery.tasks:app flower --loglevel=info &

    echo "Starting Gunicorn-server..."
    gunicorn app.main:app \
        --workers 4 \
        --worker-class uvicorn.workers.UvicornWorker \
        --bind=0.0.0.0:8001 \
        --access-logfile - \
        --error-logfile - \
        --log-level debug \
        --capture-output
else
    echo "Error: Alembic migrations failed. Aborting start-up."
    exit 1
fi