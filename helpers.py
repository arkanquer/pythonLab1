from pathlib import Path
from datetime import datetime as dt
import sys
import csv

CODE_LIST = {".cpp", ".hpp", ".c", ".h", ".py", ".pyw", ".cs", ".js", ".java"}
WHITE_LIST = CODE_LIST | {".html", ".json", ".txt", ".ipynb"}

headers = ["year", "mon", "ext", "cnt", "size", "lines"]

folders = ["/Users/yaroslavbyrak/PycharmProjects",
           "/Users/yaroslavbyrak/CLionProjects",]

def kind(extension):
    if extension in CODE_LIST:
        return "C"
    if extension in WHITE_LIST:
        return "W"
    return "O"

def lines_counter(path):
    notempty_lines = 0
    with open(path, encoding="utf-8", errors="ignore") as f:
        for s in f:
            if not s.isspace() and s is not None and s != "":
                notempty_lines += 1
    return notempty_lines

def kind(extension):
    if extension in CODE_LIST:
        return "C"
    if extension in WHITE_LIST:
        return "W"
    return "O"

def _created_at_Linux(path):
    source_path = Path(path)
    ctime = source_path.stat().st_ctime
    cdate = dt.fromtimestamp(ctime)
    return cdate.year, cdate.month

def _created_at_Windows(path):
    source_path = Path(path)
    ctime = source_path.stat().st_birthtime
    cdate = dt.fromtimestamp(ctime)
    return cdate.year, cdate.month

if sys.platform.startswith('win'):
    created_at = _created_at_Windows
else:
    created_at = _created_at_Linux
