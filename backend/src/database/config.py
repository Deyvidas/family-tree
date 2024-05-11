from __future__ import annotations

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
from pydantic_settings import YamlConfigSettingsSource
from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


class Config(BaseSettings):
    engine_config: EngineConfig
    session_config: SessionConfig

    model_config = SettingsConfigDict(yaml_file='config.yaml')

    @classmethod
    def settings_customise_sources(cls, settings: type[BaseSettings], **kwarg):
        return (YamlConfigSettingsSource(settings),)

    @property
    def engine(self) -> Engine:
        return create_engine(
            url=self.engine_config.db_url,
            echo=self.engine_config.echo,
        )

    @property
    def session(self) -> sessionmaker[Session]:
        return sessionmaker(
            bind=self.engine,
            autoflush=self.session_config.autoflush,
            expire_on_commit=self.session_config.expire_on_commit,
        )


class EngineConfig(BaseModel):
    db_url: str
    echo: bool


class SessionConfig(BaseModel):
    autoflush: bool
    expire_on_commit: bool


config = Config()  # type: ignore
