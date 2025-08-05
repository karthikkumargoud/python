def find_max_min(tup):
    return max(tup), min(tup)
numbers = (1, 2, 3, 4, 5)
max_num, min_num = find_max_min(numbers)
print("Maximum:", max_num)  
print("Minimum:", min_num)
