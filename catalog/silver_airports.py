from enum import Enum


class SilverAirports(Enum):
    NAME = "silver_airports"
    TYPE = "sqlite"
    PRODUCT = None
    STATUS = "active"
    TRANSFORMATIONS = None
    PRIMARY_KEY = ["airport_identifier"]
    RETENTION_PERIOD = None
    PARTITION_COLUMN = None
    UPDATE_TYPE = "overwrite"
    UPDATE_FREQUENCY = "daily"
    CLEANSING_RULES = {
        "trim": ["iso_country"],
        "rename": {
            "ident": "airport_identifier",
            "iso_country": "iso_country_code",
            "name": "airport_name",
        },
    }
    SCHEMA = {
        "id": "string",
        "airport_identifier": "string",
        "type": "string",
        "airport_name": "string",
        "latitude_deg": "float64",
        "longitude_deg": "float64",
        "elevation_ft": "Int64",
        "continent": "string",
        "iso_country_code": "string",
        "municipality": "string",
    }
    QUALITY_CHECKS = {
        "uniqueness": [None, ("airport_name", 99)],
        "null": [("airport_name", 97), "iso_country_code"],
        "range": {"latitude_deg": (-90, 90), "longitude_deg": (-180, 180)},
    }
    DIRECT_UPSTREAM_SOURCES = "bronze_airports"
    TAGS = None
