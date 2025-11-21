def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                # Swap
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted list is:", my_list)
