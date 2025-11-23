import csv
import time as tm
from datetime import datetime
now = datetime.now()
folder="admin"


def AdminLog(AdminID):
    tim=tm.localtime()
    time=[tim.tm_hour,tim.tm_min,tim.tm_sec,now.date(),now.strftime("%a"),AdminID]
    with open("AdminLogin.csv",'a',newline="") as j:
        writer=csv.writer(j)
        writer.writerow(time)





def show_Admin_log(AdminID):
    print("----------------------------------------------")
    with open("AdminLogin.csv",'r',newline="") as j:
        rea=csv.reader(j)
        print("ADMIN LOGIN REPORT")
        for i in rea:
            if i[5]==AdminID:
                print(i[0]+":"+i[1]+":"+i[2]+"-"+i[3],"-"+i[4])
    print("----------------------------------------------")

def createAdmin():
    print("----------------------------------------------")
    acc_db=open('admin.csv','a',newline='')
    writ=csv.writer(acc_db,delimiter=",")
    print("\nYou choose '1. Create NEW Profile'")
    print("::::::::::::::::::::::::::::::::::")
    AdminID=input("Write the new Admin ID")
    AdminName = str(input("> Enter Admin NAME: "))
    AdminAddress = str(input("> Enter Admin ADDRESS: "))
    AdminPhone = str(input("> Enter Admin PHONE: "))
    AdminPass = str(input("> Enter Admin PASSWORD: "))
    Adminlist=[AdminID,AdminPass,AdminName,AdminAddress,AdminPhone,now.date()]
    writ.writerow(Adminlist)

# c0001,sarang
# createAdmin()


def adlogin():
    AdminID=input("write your admin ID")
    Password=input("write your Password")
    return AdminID,Password