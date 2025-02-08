#looking students' mark
#range of mark 0-100

num_marks=5
#markrange=range(0,101) #from 0-100  
marks=[]
i=1

while True:
    try:

        mark=float(input(f"enter mark {i}: "))
        if 0<=mark<=100:
            marks.append(mark)
            i+=1

            if len(marks)== num_marks:
                break
        else:
            print("sorry mark is outside the range(0,100)!")
    except:
        print("sorry need input is not valid")
print("student's Marks are: ", marks)
print("student's average marks are: ", sum(marks)/len(marks))
print("student's marks total: ",sum(marks))