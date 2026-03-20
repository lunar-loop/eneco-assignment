import pandas as pd
from sqlalchemy import create_engine, text


class Postgres:

    def __init__(self, conn_details):
        self.conn_details = conn_details

    def run_query(self, query):
        engine = create_engine(
            (
                f"postgresql+psycopg2://{self.conn_details['user']}:"
                f"{self.conn_details['password']}@"
                f"{self.conn_details['host']}:"
                f"{self.conn_details['port']}/"
                f"{self.conn_details['dbname']}"
            )
        )

        with engine.connect() as conn:
            return pd.read_sql_query(text(query), conn)
