'''Lab Exercises: 

Exercise 1: Variable Assignments 

Assign an integer variable num1 with a value of 20, a float variable num2 with a value of 3.5, and a string variable text with the value "Python". 

'''
num1=20
num2=3.5
string="python"

'''
Exercise 2: String Manipulation 

Create a string variable sentence with the value "Python is fun!". 

Use slicing to extract the substring "is". 

Use the replace() function to replace "fun" with "amazing".
'''
string="python is fun!"
print(string[7:9])
string1=string.replace("fun", "amazing")
print(string1)

'''

Exercise 3: Type Conversions 

Convert the string "15" to an integer and assign it to a variable num_int. 

Convert the integer 25 to a float and assign it to a variable num_float.
'''
string="15"
num_int=int(string)
print(type(num_int))

num=25
num_float=float(num)
print(num_float)


'''

Exercise 4: Built-in Functions 

Find the absolute value of -7 and assign it to a variable abs_result. 

Given a list [10, 25, 17, 4, 29], find the maximum and minimum values and assign them to variables max_val and min_val respectively. 

Calculate the sum of all elements in the list [3, 6, 9, 12] and assign it to a variable sum_result.
'''

abs_result=abs(-7)
print(abs(abs_result))
list1=[10, 25, 17, 4, 29]
print(max(list1))

print(min(list1))

list2=[3,6,9,12]

sum_result=sum(list2)
print(sum_result)


'''

Exercise 5: List Manipulation 

Create an empty list called numbers. 

Append the numbers 5, 10, and 15 to the list. 

Remove the number 10 from the list.

'''

numbers=[]
numbers.append(5)
numbers.append(10)
numbers.append(15)
print(numbers)

numbers.remove(10)
print(numbers)


'''

Exercise 6: String Formatting 

Create variables name and age with your name and age respectively. 

Use string formatting to create a sentence "My name is [name] and I am [age] years old."
'''
name="olive"
age=10

string1="my name is {} and i am {} years old."
print(string1.format(name,age))

'''

Exercise 7: Data Type Identification 

Identify the data type of the variables num1, num2, and text.

'''
text="cool"
print(type(num1))
print(type(num2))
print(type(text))

'''

Exercise 8: Boolean Operations 

Create boolean variables is_sunny and is_raining with appropriate values. 

Perform boolean operations to check if it's sunny and not raining.
'''

is_sunny=True
is_raining=False

print(bool(is_sunny))
print(bool(is_raining))

'''

Exercise 9: Input and Output 

Prompt the user to enter their age and assign it to a variable user_age. 

Print the user's age.
'''
user_age=input("your age?:")
print("your age is: "+user_age)

'''

Exercise 100 List Slicing 

Create a list my_list containing numbers from 1 to 10. 

Use slicing to extract the sublist [3, 4, 5] from my_list.


'''

my_list=[1,2,3,4,5,6,7,8,9,10]
print(list[3:4:5])
