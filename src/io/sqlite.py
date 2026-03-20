import sqlite3
import pandas as pd


class Sqlite:

    def __init__(self, params):
        self.db_path = params["data_path"]

    def read(self, table, cols="*"):
        if cols != "*":
            cols = ", ".join(cols)
        query = f"SELECT {cols} FROM {table}"
        return self.run_query(query)

    def run_query(self, query):
        conn = sqlite3.connect(self.db_path)
        try:
            return pd.read_sql_query(query, conn)
        finally:
            conn.close()

    def write(self, df, table_name):
        # Currently schema will also be replaced if data is overwritten
        # Currently only overwrite is supported and schema evolution is not supported
        conn = sqlite3.connect(self.db_path)
        try:
            df.to_sql(table_name, conn, if_exists="replace", index=False)
        finally:
            conn.close()
