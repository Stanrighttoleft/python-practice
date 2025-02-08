list1=["apple", "orange", "aa@aa",123]

string="i like python so much"

s1=string.upper()
print(s1)

s2=s1.lower()
print(s2)
print(string.capitalize())


string="     i like python so much      "

print("----->"+string.lstrip()+"<-----")

print("----->"+string.rstrip()+"<-----")

print("----->"+string.strip()+"<-----")

string="we like python so much"

string2=string.replace("we","i")

print(string2)

print(string.replace("we","do you")+"?")

list2=string.split(" ")
print(list2)

string3=" ".join(list2)
print(string3)

#please convert :string="we like python so much" into set

string="we like python so much"
string4=string.split(" ")
set2=string4

print(set(set2))

list3=string.split()
print(list3)

set3=set(list3)
print(set3)

print(string






