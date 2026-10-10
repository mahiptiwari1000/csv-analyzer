from csv_analyzer.reader import read_csv

rows = read_csv("events.csv")

print(len(rows))
print(rows[0])