
import csv
from pathlib import Path

def read_csv(file_path: Path | str, encoding: str = "utf-8"):
    file_path = Path(file_path)

    with open(file=file_path, encoding=encoding) as f:
        csv_file = csv.reader(f)
        for x in csv_file:
            print(x)
