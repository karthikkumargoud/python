def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers)) 