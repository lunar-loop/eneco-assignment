import requests


class Api:

    def __init__(self, conn_details):
        self.host = conn_details["host"]

    def read(self, url, param):
        response = requests.get(self.host + url + param)
        response.raise_for_status()
        return response.text

    def write(self, file_path, url):
        with open(file_path, "r", encoding="utf-8") as f:
            response = requests.post(self.host + url, data=f.read())
        response.raise_for_status()
        print(response)
