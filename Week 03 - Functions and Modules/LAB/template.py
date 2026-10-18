"""
RECORD CHECK  -  my version
===========================

Name  : Mathieu Foissang
Lane  :  AI 
Date  : 09/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Rows loaded   : {value:>10.2f}")
    print(f"  Rows expected : {limit:>10.2f}")
    print(f"  Difference    : {difference:>+10.2f}")
    print(f"  Percent       : {percent:>9.2f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 34)


over_limit_count = 0

while True:
    label = input("Dataset name (or quit): ")

    if label.lower() == "quit":
        break

    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"Over-limit records: {over_limit_count}")

