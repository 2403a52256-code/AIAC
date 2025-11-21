def linear_search(lst, value):
    for index, elem in enumerate(lst):
        if elem == value:
            return index
    return -1

# Example usage
my_list = [4, 2, 7, 1, 9, 3]
search_value = 7
result_index = linear_search(my_list, search_value)
print(f"Index of {search_value} is {result_index}")
