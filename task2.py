from pathlib import Path
import helpers

YEAR = 2024
MONTH = 9

d = {}

for i in helpers.folders:
    root = Path(i)
    s = root.glob("**/*")
    for el in s:
        if not (el.is_file() and el.suffix is not None and el.suffix != "" and el.suffix in helpers.WHITE_LIST):
            continue

        year, month = helpers.created_at(el)
        if year < YEAR or (year == YEAR and month < MONTH):
            continue

        line_count = 0
        size = el.stat().st_size
        if helpers.kind(el.suffix) == "C":
            line_count = helpers.lines_counter(el)

        if (year, month) not in d:
            d[(year, month)] = [1, size, line_count]
        else:
            d[(year, month)][0] += 1
            d[(year, month)][1] += size
            d[(year, month)][2] += line_count

d_items = list(d.items())
d_items.sort()

for key_time, file_info in d_items:
    year = key_time[0]
    month = key_time[1]
    file_count = file_info[0]
    size = file_info[1]
    line_count = file_info[2]
    avg_size = size // file_count
    avg_line_count = line_count // file_count
    print(
        f"{year:10} {month:8} {file_count:10} {size:15} {line_count:15} {avg_size:10} {avg_line_count:10}"
    )