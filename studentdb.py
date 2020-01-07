import cv2
from Tkinter import *
import sqlite3
root=Tk()

root.title("enter details")

root.configure(bg='white')
def insertOrUpdate(Id,name,gender,sem,branch):
    conn=sqlite3.connect("FaceBase.db")
    cmd="CREATE TABLE IF NOT EXISTS People (ID INT PRIMARY KEY NOT NULL, Name TEXT NOT NULL, Gender TEXT, Sem INT, Branch TEXT)"
    conn.execute(cmd)
    cmd="CREATE TABLE IF NOT EXISTS IP (ID INT PRIMARY KEY UNIQUE, Name STRING, Time TEXT, Attendance CHAR DEFAULT A, NLP INT DEFAULT (0), TL INT DEFAULT (0), NLPP DOUBLE DEFAULT (0), Remark STRING)"
    conn.execute(cmd)
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(name)+",Gender="+str(gender)+",Sem="+str(sem)+",Branch="+str(branch)+" WHERE ID="+str(Id)
        conn.execute(cmd)
    else:
        cmd="INSERT INTO People(ID,Name,Gender,Sem,Branch) Values("+str(Id)+","+str(name)+","+str(gender)+","+str(sem)+","+str(branch)+")"
        conn.execute(cmd)
    cmd="INSERT INTO IP(ID,Name) Values("+str(Id)+","+str(name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()

    cam = cv2.VideoCapture(0)
    detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    sampleNum=0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            sampleNum=sampleNum+1
            cv2.imwrite("dataSet/User."+Id +'.' +str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
        elif sampleNum>20:
            break
    cam.release()
    cv2.destroyAllWindows()
def enter_the_value():
    Id=e1.get()
    name=e2.get()
    gender=e3.get()
    sem=e4.get()
    branch=e5.get()
    insertOrUpdate(Id,name,gender,sem,branch)

Label(root,text="Enter Student detail", font=("helvatica",40),bg="#808A87", fg="#0a0800").grid(rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Label(root, text="Enter The ID Number: ",fg="#000000",bg="#FAFAFA",font=("times new roman",20)).grid(row=3,padx=5,pady=5,sticky=E)
e1=Entry(root)
e1.grid(row=3,rowspan=2,column=1)
Label(root, text="Enter The Name: ",fg="#000000",bg="#FAFAFA",font=("times new roman",20)).grid(row=4,padx=5,pady=5,sticky=E)
e2=Entry(root)
e2.grid(row=4,rowspan=2,column=1)
Label(root, text="Enter Your Gender: ",fg="#000000",bg="#FAFAFA",font=("times new roman",20)).grid(row=5,padx=5,pady=5,sticky=E)
e3=Entry(root)
e3.grid(row=5,rowspan=2,column=1)
Label(root, text="Enter The Sem: ",fg="#000000",bg="#FAFAFA",font=("times new roman",20)).grid(row=6,padx=5,pady=5,sticky=E)
e4=Entry(root)
e4.grid(row=6,rowspan=2,column=1)
Label(root, text="Enter Your Branch: ",fg="#000000",bg="#FAFAFA",font=("times new roman",20)).grid(row=7,padx=5,pady=5,sticky=E)
e5=Entry(root)
e5.grid(row=7,rowspan=2,column=1)
Button(root,text="CLEAR",bg="#3F51B7",font=("times new roman",25), command=root.quit).grid(row=9,columnspan=2,stick=E+W+N+S, pady=4)
Button(root,text="ENTER",bg="#3F51B7",font=("times new roman",25), command=enter_the_value).grid(row=10,columnspan=2,stick=W+E+N+S, pady=4)
root.mainloop()




