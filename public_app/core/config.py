from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='PUBLIC_APP__',
        extra='allow',
    )
    app_title: str = 'Публичный API-клиент.'
    service_url: str


settings = Config()
