#continue and break
#continue and break only works with for and while loops
#skipping odd number and exiting the loop once a even number of 8  is detected

num=[1,5,3,7,5,21,7,8,9,10,11,12]

for n in num:
    if n %2!=0:
        print("sorry this is odd number- I will go back to loop",n )
        continue
    else:
        print("I found an even number, I will print and exit",n)
        break
num1=[1,5,7,21,18,9,5,6,7,8,20, 23,100]
m=0
while True:
    if num[m]%2 !=0:
        print("odd number back to loop",m)
        m+=1
        continue
    else:
        print("even number, print and exit",m)
        break

