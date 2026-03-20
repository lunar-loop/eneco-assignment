from src.utils.resolver import *
from src.utils import validator


def run_validation(catalog_object_name):
    obj_enum = get_catalog_enum(catalog_object_name)
    obj = resolve_io(obj_enum.TYPE.value)
    df = obj.read(obj_enum.NAME.value)
    quality_checks = obj_enum.QUALITY_CHECKS.value
    if quality_checks:
        for qc, args in quality_checks.items():
            if qc == "uniqueness":
                validator.check_uniqueness(df, args, obj_enum.PRIMARY_KEY.value)
            elif qc == "completeness":
                ref_enum = get_catalog_enum(args[1])
                ref_obj = resolve_io(ref_enum.TYPE.value)
                ref_df = ref_obj.read(ref_enum.NAME.value)
                validator.check_completeness(df, ref_df, args)
            else:
                getattr(validator, f"check_{qc}")(df, args)
