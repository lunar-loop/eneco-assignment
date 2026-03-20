def check_count(df, columns):
    for item in columns:
        if isinstance(item, tuple):
            col, threshold = item
        else:
            col = item
            threshold = 0

        count = df[col].notna().sum() if col else len(df)
        print(
            f"{(col + ': not_null_') if col else 'basic_'}row_count={count}, threshold={threshold}, passed={count > threshold}"
        )


def check_uniqueness(df, checks, primary_keys):
    for item in checks:
        if isinstance(item, tuple):
            columns_to_check, threshold = item
        else:
            columns_to_check = item
            threshold = 100

        if columns_to_check is None:
            columns_to_check = primary_keys

        if isinstance(columns_to_check, str):
            columns_to_check = [columns_to_check]

        total_rows = len(df)
        unique_rows = df[columns_to_check].drop_duplicates().shape[0]
        uniqueness_pct = (unique_rows / total_rows) * 100 if total_rows > 0 else 0

        print(
            f"{columns_to_check}: uniqueness={uniqueness_pct:.2f}%, "
            f"threshold={threshold}%, passed={uniqueness_pct >= threshold}"
        )


def check_completeness(df, ref_df, args):
    column_to_check = args[0]
    reference_column = args[2]
    threshold = args[3] if len(args) > 3 else 100

    reference_values = set(ref_df[reference_column].dropna().unique())
    present_values = set(df[column_to_check].dropna().unique())
    matched_values = reference_values.intersection(present_values)
    completeness_pct = (
        (len(matched_values) / len(reference_values)) * 100 if reference_values else 0
    )

    print(
        f"{column_to_check}: completeness={completeness_pct:.2f}%, "
        f"threshold={threshold}%, passed={completeness_pct >= threshold}"
    )


def check_null(df, checks):
    for item in checks:
        if isinstance(item, tuple):
            column_to_check, threshold = item
        else:
            column_to_check = item
            threshold = 100

        total_rows = len(df)
        not_null_rows = df[column_to_check].notna().sum()
        not_null_pct = (not_null_rows / total_rows) * 100 if total_rows > 0 else 0

        print(
            f"{column_to_check}: not_null={not_null_pct:.2f}%, "
            f"threshold={threshold}%, passed={not_null_pct >= threshold}"
        )


def check_range(df, ranges):
    for column, (min_value, max_value) in ranges.items():
        series = df[column]

        if min_value is None and max_value is None:
            passed = True
        elif min_value is None:
            passed = series.le(max_value).all()
        elif max_value is None:
            passed = series.ge(min_value).all()
        else:
            passed = series.between(min_value, max_value, inclusive="both").all()

        print(f"{column}: range=({min_value}, {max_value}), passed={passed}")
