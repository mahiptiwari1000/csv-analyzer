import csv

def read_csv(file_path: str) -> list[dict[str,str]]:
    with open(file_path, "r", newline="") as file:
         reader = csv.DictReader(file)
         rows = list(reader)
    return rows
