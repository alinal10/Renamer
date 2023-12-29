from datetime import datetime
from pathlib import Path

files = Path("/Users/alinalin/Desktop/Files")

for file in files.iterdir():
    print(f"original filename: {file}")
    # set key variables for parent path and file extensions
    directory = file.parent
    extension = file.suffix
    # unpack by splitting old name on the '-' character
    old_name = file.stem
    region, report_type, old_date = old_name.split('-')



