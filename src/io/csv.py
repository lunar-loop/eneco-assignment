from pathlib import Path

import pandas as pd


class Csv:

    def __init__(self, params):
        self.file_dir = params["file_path"]

    def read(self, file_name):
        full_file_path = f"{self.file_dir}/{file_name}"
        if not Path(full_file_path).exists():
            raise FileNotFoundError(f"File not found")
        if not file_name.endswith(".csv"):
            return full_file_path
        return pd.read_csv(full_file_path)
