import pandas as pd


def gold_airport_statistics(src_enums, src_objs):
    # Select columns and apply filters for null join keys
    airports = src_objs["airports"].read(
        src_enums["airports"].NAME.value,
        ["airport_identifier", "airport_name", "iso_country_code"],
    )
    airports = airports[airports["iso_country_code"].notna()]

    countries = src_objs["countries"].read(
        src_enums["countries"].NAME.value, ["iso_country_code", "country_name"]
    )
    countries = countries[
        ~countries["country_name"].str.contains("Unknown", case=False, na=False)
    ]
    countries = countries[countries["iso_country_code"].notna()]

    runways = src_objs["runways"].read(
        src_enums["runways"].NAME.value,
        ["airport_identifier", "length_ft", "width_ft", "surface", "lighted", "closed"],
    )

    airports_x_runways = airports.merge(runways, on="airport_identifier", how="left")
    # Keep only rows with a known runway length before selecting the longest runway
    # per country, countries with no valid runway length data are left out here and
    # will still appear later after the left join to countries, with null runway fields
    valid_runways = airports_x_runways.dropna(subset=["length_ft"])
    if not valid_runways.empty:
        longest_idx = valid_runways.groupby("iso_country_code")["length_ft"].idxmax()
        airports_x_runways = valid_runways.loc[longest_idx]
    else:
        airports_x_runways = valid_runways

    airports_x_runways = airports_x_runways.rename(
        columns={
            col: f"longest_runway_{col}"
            for col in airports_x_runways.columns
            if col != "iso_country_code"
        }
    )

    airport_counts = (
        airports.groupby("iso_country_code").size().reset_index(name="airport_count")
    )

    result = countries.merge(airport_counts, on="iso_country_code", how="left")
    result = result.merge(airports_x_runways, on="iso_country_code", how="left")
    # In case there is no airport in a country make the count as 0
    result["airport_count"] = result["airport_count"].fillna(0).astype(int)

    return result
