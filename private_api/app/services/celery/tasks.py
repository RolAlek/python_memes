from io import BytesIO

from app.services.celery.worker import app
from app.services.s3_service import minio_manager


@app.task
def upload_to_s3(
    bucket: str,
    filename: str,
    content: bytes,
    content_type: str,
) -> str:
    return minio_manager.post(
        bucket=bucket,
        filename=filename,
        content=BytesIO(content),
        content_len=len(content),
        content_type=content_type,
    )


@app.task
def delete_in_s3(bucket: str, filename: str) -> None:
    minio_manager.delete(bucket, filename)
