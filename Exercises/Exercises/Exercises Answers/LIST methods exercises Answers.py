# EX 1: Append 'apple' to the fruits list
fruits1 = ['banana', 'orange']
fruits1.append('apple')
print("1. Appended 'apple':", fruits1)

# EX 2: Insert 'cherry' at index 1 in the fruits list
fruits2 = ['banana', 'orange']
fruits2.insert(1, 'cherry')
print("2. Inserted 'cherry':", fruits2)

# EX 3: Remove 'banana' from the fruits list
fruits3 = ['banana', 'orange']
fruits3.remove('banana')
print("3. Removed 'banana':", fruits3)

# EX 4: Pop the last element from the fruits list
fruits4 = ['banana', 'orange']
removed_fruit = fruits4.pop()
print("4. Popped element:", removed_fruit)
print("   Resulting list:", fruits4)

# EX 5: Sort the numbers list in ascending order
numbers5 = [3, 1, 5, 2, 4]
numbers5.sort()
print("5. Sorted list:", numbers5)

# EX 6: Reverse the numbers list
numbers6 = [3, 1, 5, 2, 4]
numbers6.reverse()
print("6. Reversed list:", numbers6)

# EX 7: Count the occurrences of 2 in the numbers list
numbers7 = [1, 2, 3, 2, 4, 2]
count_occurrences = numbers7.count(2)
print("7. Count of 2:", count_occurrences)

# EX 8: Extend the first list with elements from the second list
list8_1 = [1, 2, 3]
list8_2 = [4, 5, 6]
list8_1.extend(list8_2)
print("8. Extended list:", list8_1)

# EX 9: Find the index of 'orange' in the fruits list
fruits9 = ['banana', 'orange', 'apple']
index_orange = fruits9.index('orange')
print("9. Index of 'orange':", index_orange)

# EX 10: Clear all elements from the fruits list
fruits10 = ['banana', 'orange', 'apple']
fruits10.clear()
print("10. Cleared list:", fruits10)

