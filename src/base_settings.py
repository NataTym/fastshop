from typing import Optional

from pydantic import (
    BaseModel,
    conint,
    field_validator,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class PostgresSettings(BaseModel):
    user: str = 'user'
    password: str = 'password'
    db: str = 'fastapi_shop'
    host: str = 'db'
    port: str = 5432
    url: str = 'postgresql+asyncpg://user:password@db:5432/fastapi_shop'


class AuthorizationSettings(BaseModel):
    secret_key: str
    algorithm: str = 'HS256'
    access_token_expire_minutes: conint(gt=0) = 30
    crypt_schema: str = 'bcrypt'


class ElasticsearchConfig(BaseModel):
    hosts: str = 'http://elastic:fastshop@elasticsearch:9200'
    timeout: int = 10
    verify_certs: bool = False

    @field_validator('hosts')
    def validate_hosts(cls, value: str) -> list[str]:
        value = value.split(',') if isinstance(value, str) else value
        return value


class RedisSettings(BaseModel):
    host: str = 'redis'
    port: int = 6379


class ProjectSettings(BaseSettings):
    api_key: str
    debug: Optional[bool] = True
    api_logger_format: Optional[str] = '%(levelname)s: %(asctime)s - %(message)s'

    postgres: PostgresSettings = PostgresSettings()
    auth: AuthorizationSettings
    elasticsearch: ElasticsearchConfig = ElasticsearchConfig()
    redis: RedisSettings = RedisSettings()

    date_time_format: str = '%Y-%m-%d %H:%M:%S'

    model_config = SettingsConfigDict(
        env_nested_delimiter='__',
        frozen=True,
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


base_settings = ProjectSettings()
