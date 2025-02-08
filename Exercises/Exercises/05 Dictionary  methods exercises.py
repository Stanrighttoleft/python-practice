# EX 1: Create an empty dictionary

mylist={}
# EX 2: Create a dictionary with key-value pairs
mylist={"1":"toyota", "2":"ford", "3":"VW"}

# EX 3: Access the value of a specific key
my_dict = {"apple": 5, "banana": 3, "cherry": 8}
print(my_dict["apple"])

# EX 4: Add a new key-value pair to the dictionary
my_dict["pineapple"]=10
print(my_dict)

# EX 5: Remove a key-value pair from the dictionary
my_dict.pop("pineapple")
print(my_dict)
# EX 6: Check if a key exists in the dictionary
y=my_dict["apple"]
print(y)

# EX 7: Get all keys in the dictionary
x=my_dict.keys()
print(x)

# EX 8: Get all values in the dictionary
z=my_dict.values()
print(z)

# EX 9: Update the dictionary with another dictionary
dict2= {"grape": 4, "kiwi": 2}
my_dict.update(dict2)
print(my_dict)


# EX 10: Clear all items from the dictionary
my_dict.clear()
print(my_dict)
