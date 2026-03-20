from enum import Enum


class SilverCountries(Enum):
    NAME = "silver_countries"
    TYPE = "sqlite"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = None
    PRIMARY_KEY = ["iso_country_code"]
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = "overwrite"
    UPDATE_FREQUENCY = "daily"
    CLEANSING_RULES = {
        "null_fill": {"keywords": "NA"},
        "rename": {"code": "iso_country_code", "name": "country_name"},
    }
    SCHEMA = {
        "id": "string",
        "iso_country_code": "string",
        "country_name": "string",
        "continent": "string",
        "wikipedia_link": "string",
        "keywords": "string",
    }
    QUALITY_CHECKS = {"count": [None], "null": ["iso_country_code", ("continent", 80)]}
    DIRECT_UPSTREAM_SOURCES = "source_countries"
    TAGS = None
