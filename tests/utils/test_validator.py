import pandas as pd

from src.utils.validator import (
    check_completeness,
    check_count,
    check_null,
    check_range,
    check_uniqueness,
)


def test_check_count_prints_pass_result_for_total_row_count(capsys):
    df = pd.DataFrame({"airport_identifier": ["A", "B", "C"]})

    check_count(df, [(None, 2)])

    captured = capsys.readouterr()
    assert "basic_row_count=3, threshold=2, passed=True" in captured.out


def test_check_uniqueness_uses_primary_key_when_check_is_none(capsys):
    df = pd.DataFrame(
        {
            "airport_identifier": ["A", "B", "B"],
            "airport_name": ["One", "Two", "Two"],
        }
    )

    check_uniqueness(df, [None], ["airport_identifier"])

    captured = capsys.readouterr()
    assert (
        "['airport_identifier']: uniqueness=66.67%, threshold=100%, passed=False"
        in captured.out
    )


def test_check_completeness_prints_reference_coverage_percentage(capsys):
    df = pd.DataFrame({"iso_country_code": ["NL", "DE", "NL", None]})
    ref_df = pd.DataFrame({"iso_country_code": ["NL", "DE", "BE", "FR"]})

    check_completeness(
        df, ref_df, ("iso_country_code", "silver_countries", "iso_country_code", 60)
    )

    captured = capsys.readouterr()
    assert (
        "iso_country_code: completeness=50.00%, threshold=60%, passed=False"
        in captured.out
    )


def test_check_null_prints_not_null_percentage(capsys):
    df = pd.DataFrame({"country_name": ["Netherlands", None, "France"]})

    check_null(df, [("country_name", 60)])

    captured = capsys.readouterr()
    assert "country_name: not_null=66.67%, threshold=60%, passed=True" in captured.out


def test_check_range_prints_pass_result_for_values_within_bounds(capsys):
    df = pd.DataFrame({"latitude_deg": [10.5, -20.0, 0.0]})

    check_range(df, {"latitude_deg": (-90, 90)})

    captured = capsys.readouterr()
    assert "latitude_deg: range=(-90, 90), passed=True" in captured.out
