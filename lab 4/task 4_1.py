import csv

def read_csv_file(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = list(csv.reader(file))
    return reader

def total_rows(data):
    return len(data)

def count_empty_rows(data):
    return sum(1 for row in data if all(cell.strip() == '' for cell in row))

def count_words(data):
    return sum(len(' '.join(row).split()) for row in data)

if __name__ == "__main__":
    filename = 'task4.txt'
    data = read_csv_file(filename)
    print("Total number of rows:", total_rows(data))
    print("Number of empty rows:", count_empty_rows(data))
    print("Total number of words:", count_words(data))