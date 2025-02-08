'''
num=1

while num<=5:
    print(num)
    num+=1
'''

#nornall we use debugin to validate the correct logic and in case when we have wrong outputs we call these run time errors

#calculate the sum of number from 1 to 10 using a while loop and for loop
'''
money=1
sum=0
while money<=10:

    sum=money+sum
    money+=1
print(sum)

total=0
for x in range(1,11):
    total=total+x
print(total)
'''
# ask the user to enter a positive number using a while loop. must break when enter negative number
#avoid infinite loops

'''
num=int(input("please input a number greater than 0, to exit num<0"))
print(num)

while num>0:
    num=int(input("please input a number greater than 0, to exit num<0"))
    if num>0:
        print(num)
        continue
    else:
        break
    
while True:
    num=int(input("please input a number greater than 0, to exit num<0"))
    if num>0:
        print(num)
        continue
    else:
        break
'''

#count down from 10 to 1 using a while loop

count=10
while count>0:
    print(count)
    count-=1
        