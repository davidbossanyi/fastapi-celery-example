from functools import lru_cache
from pathlib import Path

import tomli

from api.config.storage import AzureStorageConfig


@lru_cache
def get_azure_storage_config() -> AzureStorageConfig:
    return AzureStorageConfig()


@lru_cache
def get_version() -> str:
    with open(Path(__file__).parent.parent / "pyproject.toml", "rb") as f:
        project = tomli.load(f)
    return project["tool"]["poetry"]["version"]
