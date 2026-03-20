import pandas as pd


def trim_df(df, columns):
    for col in columns:
        df[col] = df[col].str.strip()
    return df


def null_fill_df(df, defaults):
    for col, value in defaults.items():
        df[col] = df[col].fillna(value)
    return df


def rename_df(df, columns_map):
    return df.rename(columns=columns_map)


def apply_schema(df, schema):
    result = df[list(schema.keys())].copy()

    for col, dtype in schema.items():
        result[col] = result[col].astype(dtype)

    return result
