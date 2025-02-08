# read from a file:

print("Example 1: \n") # require lots of computer memory if file is too large
file = open("readme.txt", "r")  # file is called file handler. file is a variable

content = file.read()
print("XXX"+content+"YYY")
print(type(content))
file.close()



# so how to read the whole file using readline() function:
print("\nExample 2: \n")

file = open("readme.txt", "r")
content = ""
line = file.readline()
print(">"+line+"<", "Line length:", str(len(line)))
while line:
    content += line
    line = file.readline()
    print(">"+line+"<", "Line length:", str(len(line)))
    
print(content)
file.close()


print("\nExample 3 - to avoid this complexity then we use readlines(): \n")

file = open("readme.txt", "r")  # file is called file handler
content = file.readlines()
print(type(content))
print(content)
for i in content:
    print(i)

# 0. open(), read()
# 1. open(), readline()
# 2. open(), readlines()
# 3. with open(), then read line by line using file hanmdler
# 4. open(), write()

