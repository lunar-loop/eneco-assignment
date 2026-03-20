import pandas as pd

from src.utils.cleanser import apply_schema, null_fill_df, rename_df, trim_df


def test_trim_df_strips_whitespace_from_selected_columns():
    df = pd.DataFrame(
        {
            "name": ["  Alice  ", "Bob ", " Carol"],
            "city": [" New York ", "London", " Paris "],
        }
    )

    result = trim_df(df, ["name", "city"])

    assert result["name"].tolist() == ["Alice", "Bob", "Carol"]
    assert result["city"].tolist() == ["New York", "London", "Paris"]


def test_null_fill_df_replaces_missing_values_with_defaults():
    df = pd.DataFrame(
        {
            "continent": [None, "EU"],
            "keywords": [None, "mountains"],
        }
    )

    result = null_fill_df(df, {"continent": "NA", "keywords": "unknown"})

    assert result["continent"].tolist() == ["NA", "EU"]
    assert result["keywords"].tolist() == ["unknown", "mountains"]


def test_rename_df_returns_dataframe_with_renamed_columns():
    df = pd.DataFrame({"code": ["NL"], "name": ["Netherlands"]})

    result = rename_df(df, {"code": "iso_country_code", "name": "country_name"})

    assert list(result.columns) == ["iso_country_code", "country_name"]
    assert result.iloc[0].to_dict() == {
        "iso_country_code": "NL",
        "country_name": "Netherlands",
    }


def test_apply_schema_selects_columns_and_casts_dtypes():
    df = pd.DataFrame(
        {
            "id": ["1", "2"],
            "count": ["10", "20"],
            "name": ["A", "B"],
            "ignored": ["x", "y"],
        }
    )

    result = apply_schema(
        df,
        {
            "id": "string",
            "count": "Int64",
            "name": "string",
        },
    )

    assert list(result.columns) == ["id", "count", "name"]
    assert str(result["id"].dtype) == "string"
    assert str(result["count"].dtype) == "Int64"
    assert str(result["name"].dtype) == "string"
    assert result.to_dict("records") == [
        {"id": "1", "count": 10, "name": "A"},
        {"id": "2", "count": 20, "name": "B"},
    ]
