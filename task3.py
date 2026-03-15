from pathlib import Path
import csv
import helpers

d = {}

for folder in helpers.folders:
    root = Path(folder)
    for el in root.glob("**/*"):
        if not (el.is_file() and el.suffix in helpers.WHITE_LIST):
            continue

        year, month = helpers.created_at(el)
        ext = el.suffix
        size = el.stat().st_size

        lines = 0
        if ext in helpers.CODE_LIST:
            lines = helpers.lines_counter(el)

        key = (year, month, ext)

        if key not in d:
            d[key] = [1, size, lines]
        else:
            d[key][0] += 1
            d[key][1] += size
            d[key][2] += lines

d_items = list(d.items())
d_items.sort()

def create_csv(file_name, headers):
    path = ""
    with open(file_name, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        path = f.name
    return path

def write_row(file_path, row):
    with open(file_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

file_path = create_csv("lab1_1.csv", helpers.headers)

for key, value in d_items:
    row = list(key) + list(value)
    if row[-1] == 0:
        row[-1] = None
    write_row(file_path, row)