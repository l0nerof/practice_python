import csv
from io import StringIO
from urllib.request import urlopen


class CsvReader:
    def read_data(self, source):
        if source.startswith(("http://", "https://")):
            with urlopen(source) as response:
                content = response.read().decode("utf-8-sig")
        else:
            with open(source, "r", encoding="utf-8-sig", newline="") as file:
                content = file.read()

        reader = csv.DictReader(StringIO(content))
        return list(reader)
