import csv

def read_csv_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = [','.join(row) for row in reader]
    return rows

def total_rows(rows):
    return len(rows)

def count_empty_rows(rows):
    return sum(1 for row in rows if not row.strip())

def count_words(rows):
    return sum(len(row.strip().split()) for row in rows if row.strip())

def analyze_csv_file(filename):
    rows = read_csv_file(filename)
    total = total_rows(rows)
    empty = count_empty_rows(rows)
    words = count_words(rows)
    print(f"rows={total}, empty={empty}, words={words}")

if __name__ == "__main__":
    analyze_csv_file('task4.txt')