import mysql.connector
def check():
    card = int(input("enter card no: "))
    print("check")
    database = mysql.connector.connect(host="localhost", user="root", password="", database="atmpy")
    cursor = database.cursor()
    a1 = "SELECT * from `atmpy`"
    cursor.execute(a1)
    result = cursor.fetchall()
    for x in result:
        if x[3]==card:
            print("Your balance is ",x[4])
            user()

def withdrawl():
    card=int(input("Enter card no:"))
    amount=int(input("Enter the amount:"))
    database=mysql.connector.connect(host="localhost", user="root",password="",database="atmpy")
    cursor=database.cursor()
    s="SELECT *FROM `atmpy`"
    cursor.execute(s)
    result=cursor.fetchall()
    for i in result:
        if i[3]==card:
            TotalBalance=i[4]-amount
            print(f"your total balance is {TotalBalance}")
    database=mysql.connector.connect(host="localhost",user="root",password="",database="atmpy")
    cursor=database.cursor()
    update="UPDATE `atmpy` set Balance='TotalBalance' WHERE Card='card'"
    cursor.execute(update)
    database.commit()
    user()

def deposit():
    card=int(input("Enter card no:"))
    amount=int(input("Enter the amount:"))
    database = mysql.connector.connect(host="localhost", user="root", password="", database="atmpy")
    cursor = database.cursor()
    a1 = "SELECT * from `atmpy`"
    cursor.execute(a1)
    result = cursor.fetchall()
    for x in result:
        if x[3]==card:
            TotalBalance=x[4]+amount
            print(f"Your Total Balance is {TotalBalance}")
    database=mysql.connector.connect(host="localhost",user="root",password="",database="atmpy")
    cursor=database.cursor()
    update="UPDATE `atmpy` set Balance='TotalBalance' WHERE Card='card'"
    cursor.execute(update)
    database.commit()
    print("your amount deposite successfully")
    user()

def changepin():
       acc=input("Enter account no.:")
       card=input("Enter card no.:")
       print("for reset your pin enter only 4-digit ")
       pin=input("Enter your new pin:")
       database=mysql.connector.connect(host="localhost",user="root",password="",database="atmpy")
       cursor=database.cursor()
       update="UPDATE `atmpy` SET pin=%s WHERE card=%s"
       values = (pin , card)
       cursor.execute(update,values)
       database.commit()
       print(cursor.rowcount)
       user()


def user():
    print("""
    1. check balance
    2. Withraw money
    3. Deposit money
    4. change pin
    """)
    a = int(input("enter your choice:"))
    if a==1:
        check()
    elif a==2:
        withdrawl()
    elif a==3:
        deposit()
    elif a==4:
        changepin()
    else:
        print("Invalid entry")
        user()
user()