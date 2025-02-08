print("\nExample  - strip white spaces: \n")

with open("accounts.txt", "r") as file:
    content = file.readlines() # generate a list
    print(content)
    for line in content:
        strippedline = line.rstrip()
        print(strippedline)
    

print(type(content))
