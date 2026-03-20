from enum import Enum


class SilverCountriesV2(Enum):
    NAME = "silver_countries_v2"
    TYPE = "sqlite"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = True
    PRIMARY_KEY = ["iso_country_code"]
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = "overwrite"
    UPDATE_FREQUENCY = "daily"
    CLEANSING_RULES = {
        "trim": ["code", "name"],
        "rename": {"code": "iso_country_code", "name": "country_name"},
    }
    SCHEMA = {
        "iso_country_code": "string",
        "country_name": "string",
        "continent": "string",
    }
    QUALITY_CHECKS = {
        "null": ["iso_country_code", ("country_name", 95)],
        "completeness": (
            "iso_country_code",
            "silver_countries",
            "iso_country_code",
            99.9,
        ),
    }
    DIRECT_UPSTREAM_SOURCES = "bronze_countries_v2"
    TAGS = None
