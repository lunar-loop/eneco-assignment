from enum import Enum


class SourceRunways(Enum):
    NAME = "runways.csv"
    TYPE = "file"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = None
    PRIMARY_KEY = ["id"]
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = None
    UPDATE_FREQUENCY = None
    SCHEMA = None
    QUALITY_CHECKS = None
    DIRECT_UPSTREAM_SOURCES = None
    TAGS = None
