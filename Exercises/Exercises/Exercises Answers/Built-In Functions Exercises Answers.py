# EX 1: input() function to take user input
name = input("Enter your name: ")
print("1. User input:", name)

# EX 2: min() function to find the minimum value
numbers = [3, 1, 5, 2, 4]
min_value = min(numbers)
print("2. Minimum value:", min_value)

# EX 3: max() function to find the maximum value
max_value = max(numbers)
print("3. Maximum value:", max_value)

# EX 4: sum() function to calculate the sum of elements
total_sum = sum(numbers)
print("4. Sum of elements:", total_sum)

# EX 5: int() function to convert a string to an integer
str_number = "10"
int_number = int(str_number)
print("5. Integer value:", int_number)

# EX 6: float() function to convert a string to a float
str_float = "3.14"
float_value = float(str_float)
print("6. Float value:", float_value)

# EX 7: str() function to convert a number to a string
num = 123
str_num = str(num)
print("7. String representation of number:", str_num)

# EX 8: list() function to convert a tuple to a list
tuple_values = (1, 2, 3)
list_values = list(tuple_values)
print("8. List from tuple:", list_values)

# EX 9: set() function to create a set from a list
list_duplicates = [1, 2, 3, 1, 2, 3]
unique_set = set(list_duplicates)
print("9. Unique set from list:", unique_set)

# EX 10: tuple() function to convert a list to a tuple
list_items = [4, 5, 6]
tuple_items = tuple(list_items)
print("10. Tuple from list:", tuple_items)

# EX 11: len() function to get the length of a string
string_length = len("hello")
print("11. Length of string:", string_length)

# EX 12: len() function to get the length of a list
list_length = len([1, 2, 3, 4, 5])
print("12. Length of list:", list_length)

# EX 13: len() function to get the length of a tuple
tuple_length = len((1, 2, 3, 4, 5))
print("13. Length of tuple:", tuple_length)

# EX 14: len() function to get the length of a set
set_length = len({1, 2, 3, 4, 5})
print("14. Length of set:", set_length)

# EX 15: abs() function to get the absolute value
absolute_value = abs(-10)
print("15. Absolute value:", absolute_value)

# EX 16: sorted() function to sort a list
unsorted_list = [3, 1, 5, 2, 4]
sorted_list = sorted(unsorted_list)
print("16. Sorted list:", sorted_list)

# EX 17: reversed() function to reverse a list
reversed_list = list(reversed(unsorted_list))
print("17. Reversed list:", reversed_list)

# EX 18: any() function to check if any element is true
bool_values = [False, True, False]
any_result = any(bool_values)
print("18. Result of any():", any_result)

# EX 19: all() function to check if all elements are true
all_result = all(bool_values)
print("19. Result of all():", all_result)

# EX 20: zip() function to combine lists into tuples
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
zipped_values = list(zip(letters, numbers))
print("20. Zipped tuples:", zipped_values)

