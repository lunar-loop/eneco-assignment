from enum import Enum


class OutputAirportStatistics(Enum):
    NAME = "output_airport_statistics.csv"
    TYPE = "azure_eneco"
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
    DIRECT_UPSTREAM_SOURCES = "gold_airport_statistics"
    TAGS = None
