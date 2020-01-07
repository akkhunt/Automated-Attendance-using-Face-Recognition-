from Tkinter import *
import sqlite3
import os
root=Tk()
root.configure(background='white')

def function1():
    
    os.system("python c:/python27/FRSA/studentdb.py")
    
def function2():
    
    os.system("python c:/python27/FRSA/trainner.py")

def function3():

    os.system("python c:/python27/FRSA/detector.py")

root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

Label(root, text="SELECT YOUR OPTION",font=("helvatica",40),fg="white",bg="#808A87",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="STUDENT DATABASE",font=("times new roman",30),bg="#3F51B7",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="TRAIN DATABASE",font=("times new roman",30),bg="#3F51B7",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="ATTENDANCE",font=('times new roman',30),bg="#3F51B7",fg="white",command=function3).grid(row=5,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

root.mainloop()
