from datetime import datetime 
import math
import random
import csv
import time as tm

def createAcc():
    print("----------------------------------------------")
    acc_db=open('account.csv','a',newline='')
    writ=csv.writer(acc_db,delimiter=",")
    print("\nYou choose '1. Create NEW Profile'")
    print("::::::::::::::::::::::::::::::::::")
    new_account_id = math.floor(random.random()*1000000)
    new_account_name = str(input("> Enter new account NAME: "))
    new_account_address = str(input("> Enter new account ADDRESS: "))
    new_account_phone = str(input("> Enter new account PHONE: "))
    new_account_pass = str(input("> Enter new account PASSWORD: "))
    new_account_balance = str(input("> Enter BALANCE for new account: "))
    acclist=[new_account_id,new_account_name,new_account_address,new_account_phone,new_account_pass,new_account_balance,now.date()]
    print(f"account {new_account_id} on {now.date()}")
    writ.writerow(acclist)
    print("----------------------------------------------")




def DeleteAcc():
    print("----------------------------------------------")
    print("\nYou choose '2. Delete Profile'")
    with open("account.csv",'r') as f:
        rea=csv.reader(f)
        row=[]
        acc_del=input('write the account Id to delete:')
        for i in rea:
            if i[0]!=acc_del:
                row.append(i)
    with open("account.csv",'w',newline="") as j:
        writer=csv.writer(j)
        writer.writerows(row)
    print("Account Deleted...")
    print("----------------------------------------------")


                    
# 958401 938401


def SearchAcc():
    print("----------------------------------------------")
    print("\nYou choose '3. Search Profile'")
    with open("account.csv",'r') as f:
        rea=csv.reader(f)
        acc_search=input('write the account Id to Search:')
        for i in rea:
            if i[0]==acc_search:
                print(i[1])
                print(f"account_id:{i[0]} \naccount_name:{i[1]} \naccount_address:{i[2]} \naccount_phone:{i[3]} \naccount_pass:{i[4]} \naccount_balance:{i[5]} \naccount_Created_0n:{i[6]}")
    print("----------------------------------------------")







# show_Admin_log()