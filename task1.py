from pathlib import Path
import helpers

d = {}
for i in helpers.folders:
    root = Path(i)
    s = root.glob("**/*")
    for el in s:
        if el.is_file() and el.suffix != "" and el.suffix is not None:
            if el.suffix not in d:
                d[el.suffix] = 1
            else:
                d[el.suffix] += 1

suffixes_cnts = list(d.items())
suffixes_cnts_sorted = sorted(suffixes_cnts, key=lambda el: el[1], reverse=True)

for suffix, file_count in suffixes_cnts_sorted:
    print(f"{suffix:15} {file_count:10} {helpers.kind(suffix):10}")