from enum import Enum


class OutputRevenues(Enum):
    NAME = "/revenues?client=abc123"
    TYPE = "api_eneco"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = None
    PRIMARY_KEY = None
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = "overwrite"
    UPDATE_FREQUENCY = "daily"
    SCHEMA = None
    QUALITY_CHECKS = None
    DIRECT_UPSTREAM_SOURCES = "source_revenues"
    TAGS = None
