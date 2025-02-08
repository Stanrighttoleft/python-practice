numbers=[10,25,-5,15,30]
all_positive=True
for num in numbers:
    if num <=0:
        all_positive=False
        break
if all_positive:
    print("all elements are positive")
else:
    print("Not all are positive")
