'''
def function1(p1, p2, p3, p4):
    return <value>, or return multiple values
'''

#to call a function:
#assign a variable to it then call it
'''
v2=function1(p1, p2, p3, p4)
'''

#sample coding 1:
#enter unit to 5 students name and their correspoing mark and print:
#1)list of students and their corresponding marks in a table form
#2)print the students marks sum, max, min and number of students in the student list
#3)must be able to identify who is the student with highest mark! print the student with highest mark

# hintss:
#1) create an empty sudents list students=[]
#2) create an empty mark list.
#3)enter students in the students list (using input() function)
#4) enter marks in the marks list (using input() function), ensure the marks are float()
#5)test by printing the students and marks lists

students=[]
marks=[]

def function1():
    a=input('please enter student 1 name:')
    a1=float(input('please enter student 1 mark:'))
    b=input('please enter student 2 name:')
    b1=float(input('please enter student 2 mark:'))
    c=input('please enter student 3 name:')
    c1=float(input('please enter student 3 mark:'))
    d=input('please enter student 4 name:')
    d1=float(input('please enter student 4 mark:'))
    e=input('please enter student 5 name:')
    e1=float(input('please enter student 5 mark:'))

    list1=[]
    list1.append(a)
    list1.append(b)
    list1.append(c)
    list1.append(d)
    list1.append(e)
    list2=[]
    list2.append(a1)
    list2.append(b1)
    list2.append(c1)
    list2.append(d1)
    list2.append(e1)


    return list1, list2


students, marks=function1()
print(students)
print(marks)

len=len(students)
print('there are ',len,' students in total')
print('the totoal marks is', sum(marks))
max=max(marks)
index=marks.index(max)
print('the hightest score is ' +students[index]+': ',max)
min=min(marks)
index1=marks.index(min)
print('the lowest score is '+students[index]+': ',min)

#the teacher answer

'''
print(50*"_")
print(1*"|"+"student Name "+1*"|"+"student mark")
print(50*"_")
names=[]
marks=[]

def studentsmarks():
     noofstudents=int(input("please enter number of students: "))

     for i in range(noofstudents):
     name=input("enter student name:")
     mark=float(input("enter student mark:))
     #construnct the lists of students and marks from the inputs
     names.append(name)
     marks.append(mark)

     print(names)
     print(marks)
     for i in range(names):
      print(names[i], marks[i])

      #highest score:
      maxmark=max(marks)
      print(maxmark)
      maxindex=marks.index(maxmark)
      print(maxindex)
      print(name[maxindex])
      print("highest score is :",maxmark, "which was scored by :", name[maxindex])

     return names, marks

     #print(sum(marks)), max(marks), min(marks))

studentsmarks()



print(marks)

'''