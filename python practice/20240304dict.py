
'''
dict1={"a":1,"b":4, "c":10}
for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for key,value in dict1.items():
    print("key:",key, "value:", value)

#if in operation
dict1={"a":1,"b":4, "c":10}

if "b" in dict1.keys():
    print("b is a key in dict1")
else:
    print("b is not a key in dict1")

#put key into list
dict1={"a":1,"b":4, "c":10}

dict1list=list(dict1.keys())
print(dict1list)

dict2list=list(dict1.values())
print(dict2list)
print(sum(dict2list))
print(max(dict2list))
print(min(dict2list))

marks={"alex":35,"john":56,"linda":99}
dict3list=list(marks.values())
print(max(dict3list))
print(max(marks, key=marks.get))

students=list(marks.keys())

print(students)
marks1=list(marks.values())
print(marks1)
print(max(marks1))
'''

#keys.get()

dict1={"a":1,"b":4, "c":10}

print("value of key a is:", dict1.get("c"))
print("value of key a is:", dict1.get("d","key not found") )

key="b"
getkey=dict1.get(key)
print(getkey)

