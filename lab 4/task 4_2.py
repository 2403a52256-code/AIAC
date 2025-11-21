import csv

def read_csv_file(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    return rows

def count_total_rows(rows):
    return len(rows)

def count_empty_rows(rows):
    empty_count = 0
    for row in rows:
        # Consider a row empty if all fields are empty or whitespace
        if all(cell.strip() == '' for cell in row):
            empty_count += 1
    return empty_count

def count_total_words(rows):
    word_count = 0
    for row in rows:
        for cell in row:
            word_count += len(cell.strip().split())
    return word_count

if __name__ == "__main__":
    filename = 'task4.txt'
    rows = read_csv_file(filename)
    total_rows = count_total_rows(rows)
    empty_rows = count_empty_rows(rows)
    total_words = count_total_words(rows)
    print(f"total_rows={total_rows}, empty_rows={empty_rows}, total_words={total_words}")