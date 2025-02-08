# Exercise 1
# Print the squares of numbers from 1 to 10
'''

for num in range(1, 5):
    print(num ** 2)

# Exercise 2
# Print the sum of all even numbers in a list
numbers = [2, 5, 8, 12, 15, 20, 25]
sum_even = 0
for num in numbers:
    # devide the num by 2 and chekc if remainder is zero
    if num % 2 == 0:
        sum_even += num
print("Sum of even numbers:", sum_even)

# Exercise 3

string = "HellO, World!"
count_vowels = 0
for char in string.lower():
    if char in 'aeiou':
        count_vowels += 1
print("Number of vowels:", count_vowels)
'''
# Exercise 4
# Find the maximum number in a given list

numbers = [12, 45, 67, 23, 56, 89, 34]

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("Maximum number:", max_num)
'''
# Exercise 5
# Print names starting with the letter 'S'
names = ["Sam", "Sarah", "John", "Sophia", "Samantha", "Tom"]
for name in names:
    if name.startswith("S"):
        print(name)

# Exercise 6
# Calculate the factorial of a given number
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)

# Exercise 7
# Print the keys and values of a dictionary
student_scores = {"John": 80, "Alice": 90, "Bob": 75}
for name, score in student_scores.items():
    print("Name:", name, "- Score:", score)

# Exercise 8
# Check if all elements in a list are positive numbers
numbers = [10, 25, -5, 15, 30]
all_positive = True
for num in numbers:
    if num <= 0:
        all_positive = False
        break
if all_positive:
    print("All elements are positive")
else:
    print("Not all elements are positive")

# Exercise 9
# Print the index and value of each element in a list
numbers = [10, 20, 30, 40, 50]
for index, value in enumerate(numbers):
    print("Index:", index, "- Value:", value)

# Exercise 10
# Generate a multiplication table for a given number
number = 5
for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)
'''