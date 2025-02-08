print("\nExample  - strip white spaces: \n")

with open("accounts1.txt", "r") as file:
    content = file.readlines() # generate a list
    print(content)
    for line in content:
        strippedline = line.strip()
        print(strippedline)
    
print(content)
print(type(content))

