# read from a file using with:
'''
print("Example 1: \n")

with open("readme.txt", "r") as file:
    content = file.read() 
print(content)
print(type(content))



print("\nExample 2: \n")

with open("readme.txt", "r") as file:
    content = file.readline()

print(type(content))

for i in content:
    print(i)



# so how to read the whole file using readline() function:
print("\nExample 2 reviewed: \n")
with open("readme.txt", "r") as file:
    content = ""
    line = file.readline()
    while line:
        content += line
        line = file.readline()
    print(content)

print("\nExample 3 - to avoid this complexity then we use readlines(): \n")

with open("readme.txt", "r") as file:
    content = file.readlines()

print(type(content))
print(content)
for i in content:
    print(i)

'''
print("\nExample 4 \n")

with open("readme.txt", 'r') as file:
    for line in file:
        name = line.rstrip() # right trim
        print("--->"+ name+"<---")
    
''''


# 0. open(), read()
# 1. open(), readline()
# 2. open(), readlines()
# 3. with open(), then read line by line using file hanmdler
# 4. open(), write()
'''