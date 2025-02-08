
def answer1():
    yrvar.set("English")


import tkinter as tk
yrwin=tk.Tk()
yrwin.geometry("700x300")
yrvar=tk.StringVar()
yrbtn1=tk.Button(yrwin,textvariable=yrvar,command=answer1)
yrvar.set("what language used allover the world")
yrbtn1.pack()
yrwin.title("myname")




yrlable=tk.Label(yrwin,text="hello world",font=("Times",10),bg="black",fg="yellow")
yrlable.pack()

yrbtn=tk.Button(yrwin,text="hello", bg="green", font=("Times",20),fg="white")
yrbtn.pack()

yrwin.mainloop()
