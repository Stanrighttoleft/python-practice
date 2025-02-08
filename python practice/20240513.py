
'''

#read from a file:
print("example 1: \n")#require lots of memory
file=open("readme.txt","r")
#file is called file handler. file is variable

content=file.read()
print("XXX"+content+"YYY")
print(type(content))
file.close()

'''
'''
print("\nexample 2: \n")

file=open("readme.txt","r")
content=""
line=file.readline()
print(">"+line+"<===")
while line:
    
    content +=line
    line=file.readline()
    print("=>"+line+"<===", "line length:")
print(content)
file.close()

'''
''''
#example 3
file=open("readme.txt","r")#file is called file handler
content=file.readlines()
print(type(content))
print(content)
for i in content:
    print(i)

'''
'''
with open("readme.txt", "r") as file:
    content=file.readline()
print(type(content))

for i in content:
    print(i)

'''
'''
with open("readme.txt","r") as file:
    content=file.readlines()
print(type(content))
print(content)

'''
#this is good one
'''
with open("readme.txt",'r')as file:
    for line in file:
        name=line.rstrip() #right trim
        print("--->:"+name+"<----")
'''
      