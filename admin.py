import mysql.connector


def RegisterAcc():
    Un = input("Enter your name: ")
    Accn = int(input("Enter new account Number:"))
    pin = int(input("creat your pin: "))
    CN = int(input("Enter card number:"))
    opbalance = int(input("Enter opening balance"))

    # i want to store this on database
    database = mysql.connector.connect(host="localhost", user="root", password="", database="atmpy")
    cursor = database.cursor()
    insert = "INSERT INTO `atmpy` (name,acc,card,balance,pin) VALUES (%s,%s,%s,%s,%s)"
    val = (Un, Accn, pin, CN, opbalance)
    cursor.execute(insert, val)
    database.commit()
    print("New account created successfully")
    account()


def AmountWithdrawl():
    Accn = int(input("please Enter Account No:"))
    card_no = int(input("please Enter you card no:"))
    amount = int(input("please Enter how many  amount you want to withdrawl:"))
    database = mysql.connector.connect(host="localhost", user="root", password="", database="atmpy")
    cursorobj = database.cursor()
    s1 = "SELECT *FROM `atmpy`"
    cursorobj.execute(s1)
    result = cursorobj.fetchall()
    for i in result:
        if i[3] == card_no:
            TotalBalance = i[4] - amount

            print(f"you Total balance is {TotalBalance} ")
            print("you withdral your amount successfully")

    # update this amount in database
    update = "UPDATE atmpy Set  Balance =%s WHERE Card =%s"
    val = ("TotalBalance", "card_no")
    cursorobj.execute(update, val)
    database.commit()
    print("Thank You")
    account()


def DepositAmount():
    accn = int(input("please Enter Account No:"))
    card = int(input("Please Enter you card no:"))
    amount = (int(input("Please Enter you amount: ")))
    database = mysql.connector.connect(host="localhost", user="root", password="", database="atmpy")
    cursor = database.cursor()
    select = "SELECT *FROM `atmpy`"
    cursor.execute(select)
    result = cursor.fetchall()
    for i in result:
        if i[3] == card:
            TotalBalance = i[4] + amount
            print(f"your Total balance is {TotalBalance}")
            print("You deposite your amount successfully")
            # update amount in database


            database = mysql.connector.connect(host="localhost", user="root", password="", database="atmpy")
            cursor = database.cursor()
            Update = "UPDATE `atmpy` set Balance='TotalBalance' WHERE Card='card'"
            cursor.execute(Update)
            database.commit()
            account()


def customerDetails():
    # i want to print all details of that row which is match to accn
    accn = int(input("Please Enter Account No:"))
    database = mysql.connector.connect(host="localhost", user="root", password="", database="atmpy")
    cursor = database.cursor()
    s1 = "SELECT * FROM `atmpy` "
    cursor.execute(s1)
    result = cursor.fetchall()
    for x in result:
        if x[2] == accn:
            #  print(x)
            print(
                f"ID {x[0]}\tNAME:{x[1]}\tACCOUNT NO:{x[2]}\tCARD:{x[3]}\tBALANCE:{x[4]}\tPIN:{x[5]}\tSTATUS:{x[6]}\tTYPE:{x[7]} ")
    account()


def balanceEnquiry():
    card = int(input("Please Enter you card no:"))

    database = mysql.connector.connect(host="localhost", user="root", password="", database="atmpy")
    cursor = database.cursor()
    s1 = "SELECT * FROM `atmpy` "
    cursor.execute(s1)
    result = cursor.fetchall()
    for x in result:
        if x[3] == card:
            print(f"your total balance is {x[4]}")
    account()


def CloseAcc():
    card = int(input("Enter you card no:"))
    # delete  the customer details on server by using by pin
    database = mysql.connector.connect(host="localhost", user="root", password="", database="atmpy")
    cursor = database.cursor()
    delete = "DELETE FROM `atmpy` WHERE `card`='card' "

    cursor.execute(delete)
    database.commit()
    print("your account is close successfully\n Thank you")
    account()


def account():
    print('''
        1.Register The Account
        2.Withdrawl amount
        3.Deposit amount
        4.Display customer details
        5.Balance Enquiry 
        6.Close Account''')
    so = int(input("select your option:"))
    if (so == 1):
        RegisterAcc()
    elif (so == 2):
        AmountWithdrawl()
    elif (so == 3):
        DepositAmount()
    elif (so == 4):
        customerDetails()
    elif (so == 5):
        balanceEnquiry()
    elif (so == 6):
     CloseAcc()

account()