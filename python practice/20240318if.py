A=4
B=5
if A==B:
    print("a equal to b")
else:
    print("a not equal to b")


list1=[1,2,"A","B"]
char="X"

if char in list1:
    print(char+" found")
else:
    print(char+" not found")

if A==B:
    print("A equal to B")
elif A<B:
    print("A less than B")
elif A>B:
    print("A greater than B")
else:
    print("cant predict")

if A==B:
    print("A equal to B")
else: 
    if A>B:
        print("A not equal B")
    else:
        print("no match")
    
username= input("enter login username:")
if username.lower()=="admin":
    print("login successful")
else:
    print("sorry failed to login- Please try again")

mark=input("enter student mark:")

if float(mark)>49:
    print("student passed the test:"+mark)
else:
    print("failed mark is below the pass quota:"+float(mark))


