from enum import Enum


class BronzeAirports(Enum):
    NAME = "bronze_airports"
    TYPE = "sqlite"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = None
    PRIMARY_KEY = ["ident"]
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = "overwrite"
    UPDATE_FREQUENCY = "daily"
    SCHEMA = None
    QUALITY_CHECKS = {"count": [None]}
    DIRECT_UPSTREAM_SOURCES = "source_airports"
    TAGS = None
