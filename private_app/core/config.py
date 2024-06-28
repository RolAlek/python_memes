from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class CeleryConfig(BaseModel):
    broker: str
    backend: str


class Minio(BaseModel):
    endpoint: str
    access_key: str
    secret_key: str
    bucket: str

class DBConfig(BaseModel):
    url: PostgresDsn
    echo: bool


class PrivateConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='../.env',
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='PRIVATE_APP__',
        extra='allow',
    )
    app_title: str = 'Приватный API-клиент.'
    db: DBConfig
    minio: Minio
    celery: CeleryConfig


settings = PrivateConfig()
