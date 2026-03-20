from enum import Enum


class GoldAirportStatistics(Enum):
    NAME = "gold_airport_statistics"
    TYPE = "sqlite"
    PRODUCT = "aviation"
    STATUS = "active"
    TRANSFORMATIONS = True
    PRIMARY_KEY = ["iso_country_code"]
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = "overwrite"
    UPDATE_FREQUENCY = "daily"
    SCHEMA = {
        "iso_country_code": "string",
        "country_name": "string",
        "airport_count": "Int64",
        "longest_runway_airport_identifier": "string",
        "longest_runway_airport_name": "string",
        "longest_runway_length_ft": "Int64",
        "longest_runway_width_ft": "Int64",
        "longest_runway_surface": "string",
        "longest_runway_lighted": "string",
        "longest_runway_closed": "string",
    }
    QUALITY_CHECKS = None
    DIRECT_UPSTREAM_SOURCES = {
        "airports": "silver_airports",
        "countries": "silver_countries",
        "runways": "silver_runways",
    }
    TAGS = None
