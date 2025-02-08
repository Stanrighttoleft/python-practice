'''
•	Ask the user to input the marks for the five subjects in a list/array.
•	The program must ensure that the marks are between 0 and 100
•	Display the list/array of marks entered.
•	Find the sum of all the marks in the list (all five subjects) and display the output as: The sum of your marks is: [sum]
•	Find the average of all the marks in the list (all five subjects) and display the output as: The average of your marks is: [average mark]

'''
#Create a function to make user only be able to input integer between 0-100, otherwise error message will be provide.
def mark(i):
   while True:

   
    try:
        print("please enter mark"+str(i)+" below")
        mark = int(input("type number between 0-100: "))
        
        if 0>mark or mark>100:
            raise ValueError
        else:
            return mark
    except ValueError:
        print("Invalid Integer, please enter number between 0-100 ")
           

print("please enter your 5 marks below")

#call the mark function to read each function
lenmark=5
i=1
#create array/list with five marks
markslist = []

while i<=lenmark:
   marks=mark(i)
   markslist.append(marks)
   i+=1

#print the array/list
print(markslist)

#calculate the sum and average
sumOfMarks = sum(markslist)
averageOfMarks = sum(markslist)/5

#display results
print("The sum of your marks is: "+str(sumOfMarks))
print("The average of your marks is: "+str(averageOfMarks))



     