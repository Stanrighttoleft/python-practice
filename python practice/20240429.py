def addnumbers(a,b):

    c=a+b
    return c


if addnumbers(3,4)==7:
    print("it is 7")
else:
    print("not 7")

#write a program to subtract 2 numbers

def subtract(a,b):
    z=a-b
    return z

result=subtract(2,3)
print(result)

#write a function called greeting a person...pass the person namem and greeting string
#to the person and return of example "Hi peter, How are you"

'''
def greeting():
    name= input('Nice to meet you, what is your name?\n')
    return name


name=greeting()
print("Nice to meet you "+name)

#teacher answer for greeting
def greetingfun(name, msg):
    return "hi "+name+msg

print(greetingfun("Jawdat","how is your day!"))


'''

#please not- functions must be very dynamic- make them as variable as possible
#the more dynamic the better the function is more useful

# write a function to take the sum of item in a list! (sum, max, min, average)

def listfunction(list1):
    r=sum(list1)
    s=min(list1)
    t=max(list1)
    u=sum(list1)/len(list1)
    return r,s,t,u
list1=[36,14,25,35]

print(listfunction(list1))

# teacher's answer

def listfunction2(list2):
    S=sum(list2)
    A=sum(list2)/len(list2)
    X=max(list2)
    I=min(list2)
    #return "total is "+str(S)+", Agv is "+str(A)+" Max is "+str(X)+" Min is "+str(I)
    return S,A,X,I

list2=(4,6,8,6,12,55)

#this technic is python unpacking
Total, Average, Max, Min=listfunction2(list2)

print('total is ' +str(Total))
print('Average is '+str(Average))
print('Max is '+str(Max))
print('Min is '+str(Min))

# write a function to count number of words in a string

def stringcount(a):
    pure=a.replace(" ","")
    count=len(pure)
    return count

sample="I am the atomatic!"
print(stringcount(sample))

Contrary to popular belief, English has more than five or ten vowel sounds.
The actual number is disputed because of disagreements over when two sounds
are sufficiently distinct to be classified as separate sounds.
I’ve heard some people say 15, some 17, some over 20.
'''

