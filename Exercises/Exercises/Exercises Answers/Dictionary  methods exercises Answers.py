# Exercise 1: Create an empty dictionary
empty_dict = {}
print("1. Empty Dictionary:", empty_dict)

# Exercise 2: Create a dictionary with key-value pairs
my_dict = {"apple": 5, "banana": 3, "cherry": 8}
print("2. Dictionary with key-value pairs:", my_dict)

# Exercise 3: Access the value of a specific key
value_of_apple = my_dict["apple"]
print("3. Value of 'apple':", value_of_apple)

# Exercise 4: Add a new key-value pair to the dictionary
my_dict["orange"] = 6
print("4. Dictionary after adding new key-value pair:", my_dict)

# Exercise 5: Remove a key-value pair from the dictionary
removed_item = my_dict.pop("banana")
print("5. Removed key-value pair:", removed_item)
print("   Dictionary after removal:", my_dict)

# Exercise 6: Check if a key exists in the dictionary
is_key_exist = "banana" in my_dict
print("6. Does 'banana' exist in the dictionary?", is_key_exist)

# Exercise 7: Get all keys in the dictionary
keys = my_dict.keys()
print("7. Keys in the dictionary:", keys)

# Exercise 8: Get all values in the dictionary
values = my_dict.values()
print("8. Values in the dictionary:", values)

# Exercise 9: Update the dictionary with another dictionary
other_dict = {"grape": 4, "kiwi": 2}
my_dict.update(other_dict)
print("9. Updated dictionary:", my_dict)

# Exercise 10: Clear all items from the dictionary
my_dict.clear()
print("10. Cleared dictionary:", my_dict)

