def count_lines_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

# Example usage:
filename = 'test.txt'  # Replace with your file name
num_lines = count_lines_in_file(filename)
print(f"Number of lines in '{filename}': {num_lines}")