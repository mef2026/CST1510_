"""
RECORD CHECK  -  my version
===========================

Name  : Mathieu Foissang
Lane  :  AI / 
Date  : 17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(value, limit):
    if limit <= 0:
        raise ValueError("The expected number of rows must be positive.")
    difference = value - limit
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status

 
def print_report(label, value, limit, difference, percent, status):
    print(f"\nDataset: {label}")
    print(f"  Rows loaded:   {value:>9.2f}")
    print(f"  Rows expected: {limit:>9.2f}")
    print(f"  Difference:    {difference:>+9.2f}")
    print(f"  Percentage:    {percent:>8.2f}%")
    print(f"  Status:        {status}")
 
 
def load_records(path):
    records = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            label, value, limit = line.strip().split(",")
            records.append({"label": label,
                            "value": float(value),
                            "limit": float(limit)})
    return records
 

