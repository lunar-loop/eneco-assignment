import time
from pathlib import Path

from tabulate import tabulate

from src.utils.resolver import resolve_io


def read_sql_file(sql_file):
    path = Path(f"sql/{sql_file}")
    if not path.exists():
        raise FileNotFoundError(f"SQL file not found: {path}")
    sql = path.read_text(encoding="utf-8").strip()
    if not sql:
        raise ValueError(f"SQL file is empty: {path}")
    return sql


def run_analysis(sql_file, database):
    if database not in ["sqlite", "postgres"]:
        print(f"{database} is not supported for running analysis queries yet..")
        return

    sql = read_sql_file(sql_file)
    query_obj = resolve_io(database)

    start = time.perf_counter()
    df = query_obj.run_query(sql)
    duration = time.perf_counter() - start

    if df.shape[1] == 0:
        print(f"Query executed in {duration:.3f} seconds (no rows returned).")
        return

    print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
    print(f"\nTime taken: {duration:.3f} seconds")
