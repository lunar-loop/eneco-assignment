from enum import Enum


class BronzeRunways(Enum):
    NAME = "bronze_runways"
    TYPE = "sqlite"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = None
    PRIMARY_KEY = ["id"]
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = "overwrite"
    UPDATE_FREQUENCY = "daily"
    SCHEMA = None
    QUALITY_CHECKS = {"count": [None]}
    DIRECT_UPSTREAM_SOURCES = "source_runways"
    TAGS = None
