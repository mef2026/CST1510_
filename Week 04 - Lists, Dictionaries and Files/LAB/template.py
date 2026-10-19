
"""
RECORD CHECK - My Version
=========================

Name  : Mathieu Foissang
Lane  : AI / Data Science
Date  : 17/10/2026

Run it: python template.py

"""

with open("dataset_records.txt", "w") as file:
    file.write("survey_2026,1187,1200\n")
    file.write("survey_2026,1250,1200\n")
    file.write("logs_2026,790,1000\n")
    file.write("survey_2026,1200,1200\n")

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

def print_summary(over_count, total_count):
    print(f"\nOver-limit records: {over_count} of {total_count}")
 
 
def print_missing_file(path):
    print(f"Cannot find {path}; starting with an empty list.")
 
 
def main():
    path = "dataset_records.txt"
    try:
        records = load_records(path)
    except FileNotFoundError:
        print_missing_file(path)
        records = []
 
    over_count = 0
    with open("results.txt", "w", encoding="utf-8") as file:
        for record in records:
            difference, percent, status = check_record(
                record["value"], record["limit"]
            )
            print_report(record["label"], record["value"],
                         record["limit"], difference, percent, status)
            file.write(f"{record['label']},{status}\n")
            if status == "OVER LIMIT":
                over_count += 1
    print_summary(over_count, len(records))
 
 
if __name__ == "__main__":
    main()
