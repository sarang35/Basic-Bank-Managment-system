
import function as ac
import time as tm
import adlog as ad
import csv


AdminID=input("write your admin ID: ")
Password=input("write your Password: ")


run = True
while run:
    with open("admin.csv",'r') as ar:
        read=csv.reader(ar)
        for i in read:
            if i[0]==AdminID and i[1]==Password:
                ad.AdminLog(AdminID)
                print("-----------------------------------------------------------")
                print("WELCOME TO OUR PAGE \n")
                resp=input("WHAT DO U WANT TO DO:\n1.Create account \n2.delete account \n3.Search Account \n4.Admin Login log \nenter any button to exit")
                if resp.lower() == "create account" or resp == "1" :
                    ac.createAcc()
                elif resp.lower() == "delete account" or resp == "2" :
                    ac.DeleteAcc()
                elif resp.lower() == "Search Account" or resp == "3" :
                    ac.SearchAcc()
                elif resp.lower() == "Admin Login" or resp == "4" :
                    ad.show_Admin_log(AdminID)
                else:
                    run=False
                break
            else:
                print("wrong password or login ID")
                AdminID,Password=ad.adlogin()

        print("-----------------------------------------------------------")
