from enum import Enum


class BronzeCountriesV2(Enum):
    NAME = "bronze_countries_v2"
    TYPE = "sqlite"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = True
    PRIMARY_KEY = None
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = "overwrite"
    UPDATE_FREQUENCY = "daily"
    SCHEMA = None
    QUALITY_CHECKS = {"count": [(None, 150)]}
    DIRECT_UPSTREAM_SOURCES = {
        "src_api": "source_countries_v2",
        "src_ref": "silver_countries",
    }
    TAGS = None
