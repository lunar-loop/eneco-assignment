from enum import Enum


class SourceRevenues(Enum):
    NAME = "revenues.txt"
    TYPE = "file"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = None
    PRIMARY_KEY = None
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = None
    UPDATE_FREQUENCY = None
    SCHEMA = None
    QUALITY_CHECKS = None
    DIRECT_UPSTREAM_SOURCES = None
    TAGS = None
