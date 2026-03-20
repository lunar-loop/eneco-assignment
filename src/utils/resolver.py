import importlib

from config.config import CONFIG, DATABASE_TYPE_CLASS_MAPPING

from src.io.api import Api
from src.io.azure import Azure
from src.io.csv import Csv
from src.io.postgres import Postgres
from src.io.sqlite import Sqlite


def get_catalog_enum(catalog_object_name):
    module = importlib.import_module(f"catalog.{catalog_object_name}")
    enum_name = "".join(word.capitalize() for word in catalog_object_name.split("_"))
    return getattr(module, enum_name)


def resolve_io(database):
    cls = globals().get(DATABASE_TYPE_CLASS_MAPPING[database])
    return cls(CONFIG["local"][database])
