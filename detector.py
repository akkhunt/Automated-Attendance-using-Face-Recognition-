import numpy as np
import cv2
import cv2 as cv
import os
from datetime import *
import sys
import time
import pickle
import sqlite3
import os
import sys
from Tkinter import *
import Tkinter
from PIL import Image, ImageTk
import winsound
root=Tk()

root.title("enter details")

root.configure(bg="white")

root.focus_set()
def getsheet(Id):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM IP WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    sheet=None
    for row in cursor:
        sheet=row
    conn.close()
    return sheet


def getProfile(Id):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

def IP(prof,Id,name,time,attendance,l,tl,per,r):
    print prof,Id,name,time,attendance,l,tl,r
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM IP WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        conn.execute("UPDATE IP SET TL="+str(tl)+"")
        conn.execute("UPDATE IP SET Name="+str(name)+",Time="+str(time)+",Attendance="+str(attendance)+",NLP="+str(l)+",TL="+str(tl)+",NLPP="+str(per)+",Remark="+str(r)+" WHERE ID="+str(Id))
    else:
        params = (Id,name,time,attendance,l,tl,per,r)
        conn.execute("INSERT INTO IP Values(?, ?, ?, ?, ?, ?, ?,?)", params)
    conn.commit()
    conn.close()
    winsound.PlaySound('sound.mp3',winsound.SND_FILENAME)
    
def faculty(prof):
    cd=[0]*100
    uid=prof
    detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    recognizer = cv2.createLBPHFaceRecognizer()
    recognizer.load('trainner/trainner.yml')
    path='dataSet'
    font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            lp=getsheet(Id)
            profile=getProfile(Id)
            if(profile!=None):
                cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1]),(x,y+h+30),font, 255)
                cv2.cv.PutText(cv2.cv.fromarray(img),str(conf),(x,y+h+60),font, 255)
                if (uid=="IP") and (cd[Id]!=Id):
                    cd[Id]=Id
                    name=str(profile[1])
                    names='"%s"'%name
                    times='"%s"'%(time.strftime("%c"))
                    attendance='"P"'
                    L=lp[4]
                    l=(int)(L+1)
                    tl=float(e3.get())
                    q=tl/100
                    per=(float(l/q))
                    if (per<75.0) and (per!=0):
                        r='"Defaulter"'
                    else:
                        r='"--"'
                    IP(uid,Id,names,times,attendance,l,tl,per,r)
                    break
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

def enter_the_value():
    uid=e2.get()
    password=e4.get()
    if password=="12345":
        faculty(uid)

Label(root,text="FACULTY LOGIN", fg='white', bg='#424242' ,font=("helvetica",40),width=23).grid(rowspan=2,columnspan=3,sticky=E+W+N+S,padx=5,pady=5)

Label(root, text="Enter Subject : ",font=("helvetica ",30),fg='#000000',bg="#FAFAFA").grid(row=2,sticky=E,column=0)

Label(root, text="Enter the lecture number: ",font=("helvetica ",30),fg='#000000',bg="#FAFAFA").grid(row=3,sticky=E,column=0)

Label(root, text="Enter password: ",font=("helvetica ",30),fg='#212121',bg="#FAFAFA").grid(row=4,sticky=E,column=0)

e2=Entry(root)
e3=Entry(root)
e4=Entry(root)

e2.grid(row=2,column=1,columnspan=2,sticky=W)
e3.grid(row=3,column=1,columnspan=2,sticky=W)
e4.grid(row=4,column=1,columnspan=2,sticky=W)
Button(root,text="CLEAR",font=("times new roman",30), fg="white",bg="#3F51B7",command=root.quit).grid(row=5,column=0, pady= 10,padx=10,sticky=E+W+N+S)
Button(root,text="ENTER",font=("times new roman",30), fg="white",bg="#3F51B7",command=enter_the_value).grid(row=5,column=1,pady=10,padx=10,sticky=E+W+N+S)
root.mainloop()





