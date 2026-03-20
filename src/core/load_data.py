import importlib

from src.utils.resolver import *
from src.utils import cleanser


def run_data_load(catalog_object_name):
    # Fetching the data object details
    obj_enum = get_catalog_enum(catalog_object_name)

    # Resolving the source object(s) details
    upstream_sources = obj_enum.DIRECT_UPSTREAM_SOURCES.value
    if isinstance(upstream_sources, dict):
        src_enums = {k: get_catalog_enum(v) for k, v in upstream_sources.items()}
    else:
        src_enums = {"src": get_catalog_enum(upstream_sources)}
    src_objs = {k: resolve_io(v.TYPE.value) for k, v in src_enums.items()}

    # Applying transformations if present
    if obj_enum.TRANSFORMATIONS.value:
        module = importlib.import_module(f"src.transformations.{catalog_object_name}")
        transformer = getattr(module, catalog_object_name)
        result = transformer(src_enums, src_objs)
    else:
        src_enum = next(iter(src_enums.values()))
        src_obj = next(iter(src_objs.values()))
        result = src_obj.read(src_enum.NAME.value)

    # Cleansing for silver layer objects
    if catalog_object_name.startswith("silver_"):
        cleansing_rules = obj_enum.CLEANSING_RULES.value
        if cleansing_rules:
            for cr, args in cleansing_rules.items():
                result = getattr(cleanser, f"{cr}_df")(result, args)

    # Apply schema
    if obj_enum.SCHEMA.value:
        result = cleanser.apply_schema(result, obj_enum.SCHEMA.value)

    # Writing result to the target
    tgt_obj = resolve_io(obj_enum.TYPE.value)
    tgt_obj.write(result, obj_enum.NAME.value)
