from .config import MainConfig
from .config import TestConfig


class DatabaseConfig:
    main_config = MainConfig()  # type: ignore
    test_config = TestConfig()  # type: ignore
