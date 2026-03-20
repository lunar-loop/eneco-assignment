from enum import Enum


class SilverRunways(Enum):
    NAME = "silver_runways"
    TYPE = "sqlite"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = None
    PRIMARY_KEY = ["id"]
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = "overwrite"
    UPDATE_FREQUENCY = "daily"
    CLEANSING_RULES = {
        "trim": ["surface"],
        "rename": {"airport_ident": "airport_identifier"},
    }
    SCHEMA = {
        "id": "string",
        "airport_ref": "string",
        "airport_identifier": "string",
        "length_ft": "Int64",
        "width_ft": "Int64",
        "surface": "string",
        "lighted": "string",
        "closed": "string",
    }
    QUALITY_CHECKS = {"uniqueness": [None], "null": [("airport_ref", 95)]}
    DIRECT_UPSTREAM_SOURCES = "bronze_runways"
    TAGS = None
