# EX 1: input() function to take user input
print("enter something:")
x=input()
print("you type this:"+x)
# EX 2: min() function to find the minimum value
numbers = [3, 1, 5, 2, 4]
y=min(numbers)
print(y)

 

# EX 3: max() function to find the maximum value
numbers = [3, 1, 5, 2, 4]
z=max(numbers)
print(z)

# EX 4: sum() function to calculate the sum of elements
numbers = [3, 1, 5, 2, 4]
a=sum(numbers)
print(a)

# EX 5: int() function to convert a string to an integer
str_number = "10"
b=int(str_number)
print(type(b))
 

# EX 6: float() function to convert a string to a float
str_float = "3.14"
c=float(str_float)
print(type(str_float))
 

# EX 7: str() function to convert a number to a string
num = 123
d=str(num)
print(type(num))
 

# EX 8: list() function to convert a tuple to a list
tuple_values = (1, 2, 3)
e=list(tuple_values)
print(e)

# EX 9: set() function to create a set from a list
list_duplicates = [1, 2, 3, 1, 2, 3]
f=set(list_duplicates)
print(f)
 

# EX 10: tuple() function to convert a list to a tuple
list_items = [4, 5, 6]
g=tuple(list_items)
print(g)
 

# EX 11: len() function to get the length of a string
string_length = len("hello")
print(string_length)
 

# EX 12: len() function to get the length of a list
numbers1 = [3, 1, 5, 2, 4]
h=len(numbers1)
print(h)

# EX 13: len() function to get the length of a tuple
numbers2 = (3, 1, 5, 2, 4)
i=len(numbers2)
print(i)


# EX 14: len() function to get the length of a set
numbers3 = {3, 1, 5, 2, 4}
j=len(numbers3)
print(j)

# EX 15: abs() function to get the absolute value
num1 = -20
k=abs(num1)
print(k)

# EX 16: sorted() function to sort a list
unsorted_list = [3, 1, 5, 2, 4]
l=sorted(unsorted_list)
print(l)


# EX 17: reversed() function to reverse a list
unsorted_list1 = [3, 1, 5, 2, 4]
m=reversed(unsorted_list1)
print(m)


# EX 18: any() function to check if any element is true
bool_values = [False, True, False]
n=any(bool_values)
print(n)


# EX 19: all() function to check if all elements are true
bool_values = [False, True, False]
o=all(bool_values)
print(o)
 

# EX 20: zip() function to combine lists into tuples
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
p=zip(letters, numbers)
print(p)