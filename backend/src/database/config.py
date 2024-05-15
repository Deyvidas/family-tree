from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
from pydantic_settings import YamlConfigSettingsSource
from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


class EngineConfig(BaseModel):
    db_url: str
    echo: bool


class SessionConfig(BaseModel):
    autoflush: bool
    expire_on_commit: bool


class MainConfig(BaseSettings):
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
            connect_args={'options': '-c timezone=utc'},
        )

    @property
    def sessionmaker(self) -> sessionmaker[Session]:
        return sessionmaker(
            bind=self.engine,
            autoflush=self.session_config.autoflush,
            expire_on_commit=self.session_config.expire_on_commit,
        )


class TestConfig(MainConfig):
    """Configuration used for testing the application."""

    model_config = SettingsConfigDict(yaml_file='test.config.yaml')
