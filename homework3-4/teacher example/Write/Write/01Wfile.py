# write to a file

# if I  open a file to wite an dth efile does not exists it will be created.
'''
with open("example3.txt", "w") as file:
    file.write("This is a single line of text.")


lines = ["This is the first line.",
         "This is the second line.",
         "This is the third line."]

with open("example4.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
'''
with open("example2.txt", "a") as file:
    file.write("This line will be appended to the end of the file example4.txt.")

