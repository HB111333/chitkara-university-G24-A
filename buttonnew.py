from tkinter import *
from PIL import ImageTk, Image
import mysql.connector as A
con=A.connect(host='localhost', user='root', password='root', database='upsc')
if con.is_connected():
    print('connected')
else:
    print('not connected')

root =Tk()
root.geometry("555x333")
def reg():
    c=con.cursor()
    c.execute(' select * from registration')
    data=c.fetchall()
    count=len(data)
    regno=(count+1)
    n=input('enter your name                     :')
    fn=input('enter your father name             :')
    mn=input('enter your mother name             :')
    ex='chitkara entrance'
    y=input('enter applied year                  :')
    g=input('enter gender                        :')
    d=input('enter date of birth (yyyy-mm-dd)    :')
    na=input('enter nationality                  :')
    ms=input('enter marital status               :')
    com=input('enter community                   :')
    mi=input('minority status                    :')
    add_1=input('enter address line 1            :')
    add_2=input('enter address line 2            :')
    add_3=input('enter address line 3            :')
    dis=input('enter district                    :')
    sta=input('enter your state                  :')
    pin=input(' enter pincode                    :')
    phn=input(' phone number                     :')
    mbn=input('mobile number                     :')
    e_mail=input('email address                  :')
    edu=input('education qulification            :')
    pre=input('preferance                        :')
    data=(regno,n,fn,mn,ex,y,g,d,na,ms,com,mi,add_1,add_2,add_3,dis,sta,pin,phn,mbn,e_mail,edu,pre)
    sql='insert into registration values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    print('>---------------------------------------------------------<')
    print('registration no. is',regno)
    print('>---------------------------------------------------------<')
    c.execute(sql,data)
    con.commit()
    print('>---------------------------------------------------------<')
    
    print('data entered successfully')
def display():
    reg=int(input("enter registration number: "))
    t=(reg,)
    c=con.cursor()
    a='select* from registration where regno=%s'
    c.execute(a,t)
    data=c.fetchall()
    for i in data:
        if i[0]!=reg:
            print("wrong")
        elif i[0]==reg:
            print(">----------------------------------------------------<")
            print("Registration No. is     : ",i[0])
            print("Name                    : ",i[1])
            print("Father Name             : ",i[2])
            print("Mother Name             : ",i[3])
            print("Examination Applied     : ",i[4])
            print("Year                    : ",i[5])
            print("Gender                  : ",i[6])
            print("Date Of Birth           : ",i[7])
            print("Nationality             : ",i[8])
            print("Marital Status          : ",i[9])
            print("Community               : ",i[10])
            print("Minority                : ",i[11])
            print("Address line 1          : ",i[12])
            print("Address line 2          : ",i[13])
            print("Address line 3          : ",i[14])
            print("District                : ",i[15])
            print("State                   : ",i[16])
            print("Pincode                 : ",i[17])
            print("Phone                   : ",i[18])
            print("Mobile Number           : ",i[19])
            print("Email Address           : ",i[20])
            print("Education Qualification : ",i[21])
            print("Preferance              : ",i[22])
            print(">----------------------------------------------------<")
def update():
    r=int(input("enter regno want to update: "))
    t=(r,)
    c=con.cursor()
    a='select* from registration where regno=%s'
    c.execute(a,t)
    data=c.fetchall()
    for i in data:
        if i[0]==r:
            print(" press 1 to update (name,fathername,mothername,gender,comm,dob,mrs)")
            print(" press 2 to update (exam,year,nat,min,edu,pre)")
            print(" press 3 to update (satae,dis,add1,add2,add3,pin)")
            print(" press 4 to update (ph,mb,em)")
            print(" press 5 if all information correctly updated ")
            n=int(input("enter your choice: "))
            if n==1:
                na=input("enter correct name            : ")
                fn=input("enter correct father name     : ")
                mn=input("enter correct mother name     : ")
                ge=input("enter correct gender          : ")
                co=input("enter correct community       : ")
                do=input("enter correct dob             : ")
                mr=input("enter correct marital status  : ")
                c=con.cursor()
                t=(na,fn,mn,ge,co,do,mr,r)
                sql='update registration set name=%s,fathername=%s,mothername=%s,gender=%s,community=%s,dob=%s,maritial_status=%s where regno=%s'
                c.execute(sql,t)
                con.commit()
                print(">----------------------------------------------------<")
                print('data updated successfully')
            elif n==2:
                ex=input("enter correct examination applied  : ")
                y=input("enter correct year of application   : ")
                na=input("enter correct nationality          : ")
                mr=input("enter correct minority             : ")
                ed=input("enter correct qualification        : ")
                pr=input("enter correct preferance type      : ")
                c=con.cursor()
                t=(ex,y,na,mr,ed,pr,r)
                sql='update registration set examination_applied=%s, year=%s, nationality=%s, minority=%s, edu_qul=%s, preferance=%s where regno=%s'
                c.execute(sql,t)
                con.commit()
                print(">----------------------------------------------------<")
                print('data updated successfully')
            
            elif n==3:
                st=input("enter correct state           : ")
                di=input("enter correct state           : ")
                a1=input("enter correct addd 1          : ")
                a2=input("enter correct addd 2          : ")
                a3=input("enter correct addd 3          : ")
                pi=input("enter correct pincode         : ")
                c=con.cursor()
                t=(st,di,a1,a2,a3,pi,r)
                sql='update registration set state=%s,dist=%s,add_1=%s,add_2=%s,add_3=%s,pincode=%s where regno=%s'
                c.execute(sql,t)
                con.commit()
                print(">----------------------------------------------------<")
                print('data updated successfully')
            elif n==4:
                pb=input("enter correct phone no   : ")
                mb=input("enter correct mobile no  : ")
                em=input("enter correct email      : ")
                c=con.cursor()
                t=(pb,mb,em,r)
                sql='update registration set phone_no=%s,mobile_no=%s,email=%s where regno=%s'
                c.execute(sql,t)
                con.commit()
                print(">----------------------------------------------------<")
                print('data updated successfully')
            else:
                print("all data updated successfully please check again after view data ")
                
                exit
def delete():
    reg=int(input("enter registration number: "))
    t=(reg,)
    c=con.cursor()
    a='select* from registration where regno=%s'
    c.execute(a,t)
    data=c.fetchall()
    for i in data:
        if reg==i[0]:
            t=(reg,)
            a='delete from registration where regno=%s '
            c=con.cursor()
            c.execute(a,t)
            con.commit()
            print(">-------------------------------------<")
            print("Data Deleted Successfully ")
        else:
            print("registration No. Wrong")
frame = Frame(root, borderwidth=10, bg="yellow",relief=SUNKEN)
frame.pack(side=LEFT,anchor  ='nw')

b1= Button(frame, fg="red", text="REGISTER DATA",command=reg)
b1.pack(side=LEFT)
b2= Button(frame, fg="red", text="DISPLAY DATA",command=display)
b2.pack(side=LEFT)
b3= Button(frame, fg="red", text="UPDATE DATA",command=update)
b3.pack(side=LEFT)
b4= Button(frame, fg="red", text="DELETE DATA",command=delete)
b4.pack(side=LEFT)
img = Image.open("C:/Users/Honey Bansal/Downloads/12.png")
img = img.resize((250,200))
photo= ImageTk.PhotoImage(img )




h_lable1 = Label(image=photo)
h_lable1.pack()

root.mainloop()

