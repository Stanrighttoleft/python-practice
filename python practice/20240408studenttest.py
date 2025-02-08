#a student with the following smarks:
marks=[56,78,90,23,57]
index=0

while True:
    if marks[index]<50:
        passed=False
        print("Your failed",marks[index])
        break
    else:
        passed=True
        index+=1
 
print("Verdict:")
if passed:
    print("well done")
else:
    print("you fial")

#the student is granted a pass if all marks are above 50% otherwise the student fail
#if any mark is below 50%
#write a python code to sdetermine if the student has passed or fail

marks1 =[56,78,90,53,57,60]
#determine who passed and who failed

