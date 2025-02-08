
'''
x=range(1,5)

print(x[0])
print(x[1])
print(x[2])
print(x[3])
'''

'''
string="hello python"
s="x" 
#pervious s is ignored becasue "for statment" used the s internally
#and assigned the letters from the string in sequence
for s in string:
    print(s, string.index(s))
'''

'''
list1=[1,"A","c",2,5,"123","google",1.23]

for i in list1:
    print(i)

tuple1=(1,"A","c",2,5,"123","google",1.23)
print("+++++++++++++++++")
for i in tuple1:
    print(i)

x=range(1,20,2)

for i in x:
    print(i)

numbers=[2,5,8,12,15,20,25]
sum_even=0
for num in numbers:
    if num % 2==0:
        sum_even +=num
print("sum of even numbers:", sum_even)

string="Hello World"
count_vowels=0
for char in string.lower():
    if char in 'aeiou':
        count_vowels +=1

print("number of vowels:",count_vowels)

numbers=[12,45,67,23,56,89,34]
print(max(numbers))
max_num=numbers[0]
for num in numbers:
    if num>max_num:
        max_num=num
print("maximun number:",max_num)

names=["sam","sarah","john","sophia","samantha","tom"]
for name in names:
    if name.startswith("s"):
        print(name)

num=5
factorial=1
for i in range(1, num+1):
    factorial *=i
print("factorial of", num, "is", factorial)
'''



student_scores={"john":80, "alice":90, "bob":75}

for name, score in student_scores.items():
    print("name:", name,"- score:", score )

for score in student_scores.values():
    print(score)



numbers=[10,25,-5,15,30]
all_positive=True
for num in numbers:
    if num <=0:
        all_positive=False
        break
if all_positive:
    print("all elements are positive")
else:
    print("Not all are positive")


number=5
for i in range(1,11):
    result=number*i
    print(number, "x",i,"=",result)