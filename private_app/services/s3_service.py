from minio import Minio

from private_app.core.config import settings


class MinioManager:
    def __init__(
        self,
        endpoint: str,
        access_key: str,
        secret_key: str,
        secure: bool = False,
    ) -> None:
        self.client = Minio(
            endpoint=endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure,
        )

    def post(self,
        bucket: str,
        filename: str,
        content: bytes,
        content_len: int,
        content_type: str
    ) -> str:
        if not self.client.bucket_exists(bucket):
            self.client.make_bucket(bucket)
        self.client.put_object(
            bucket,
            filename,
            content,
            content_len,
            content_type
        )
        return self.client.presigned_get_object(bucket, filename)

    def delete(self, bucket: str, filename: str) -> None:
        self.client.remove_object(bucket, filename)


minio_manager = MinioManager(
    endpoint=settings.minio.endpoint,
    access_key=settings.minio.access_key,
    secret_key=settings.minio.secret_key,
)
