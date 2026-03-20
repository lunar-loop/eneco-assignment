import json
import pandas as pd


def silver_countries_v2(src_enums, src_objs):
    src_df = src_objs["src"].read(src_enums["src"].NAME.value)
    rows = []

    for json_data in src_df["json_data"]:
        rows.append(json.loads(json_data))

    return pd.DataFrame(rows)
