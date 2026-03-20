from enum import Enum


class SourceAirports(Enum):
    NAME = "airports.csv"
    TYPE = "file"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = None
    PRIMARY_KEY = ["ident"]
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = None
    UPDATE_FREQUENCY = None
    SCHEMA = None
    QUALITY_CHECKS = None
    DIRECT_UPSTREAM_SOURCES = None
    TAGS = None
