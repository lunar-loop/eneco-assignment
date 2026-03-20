import pandas as pd

from requests.exceptions import HTTPError


def bronze_countries_v2(src_enums, src_objs):
    ref_df = src_objs["src_ref"].read(src_enums["src_ref"].NAME.value)
    json_rows = []

    for country_code in ref_df["iso_country_code"]:
        try:
            json_data = src_objs["src_api"].read(
                src_enums["src_api"].NAME.value, f"/{country_code}"
            )
            json_rows.append(json_data)
        except HTTPError as ex:
            if ex.response is not None and ex.response.status_code == 404:
                print(
                    f"Skipping {country_code}: API returned 404. Country data not found."
                )
                continue
            raise

    return pd.DataFrame({"json_data": json_rows})
