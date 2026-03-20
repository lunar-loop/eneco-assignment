from io import StringIO
import pandas as pd

from azure.storage.blob import BlobClient


class Azure:

    def __init__(self, conn_details):
        self.conn_details = conn_details

    def write(self, df, file_name):
        csv_data = StringIO()
        df.to_csv(csv_data, index=False)

        blob_url = (
            f"https://{self.conn_details['account']}.blob.core.windows.net/"
            f"{self.conn_details['container']}/{self.conn_details['path']}/{file_name}"
            f"?{self.conn_details['signature']}"
        )

        blob_client = BlobClient.from_blob_url(blob_url)
        blob_client.upload_blob(csv_data.getvalue(), overwrite=True)
