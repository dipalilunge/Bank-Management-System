def s1():
    a = int(input("enter card no"))
    b = int(input("enter pin"))
    import mysql.connector
    database = mysql.connector.connect(host="localhost", user="root", password="", database="atm_system")
    cursor = database.cursor()
    a1 = "SELECT * from `user_info`"
    cursor.execute(a1)
    result = cursor.fetchall()

    for x in result:
        print(x[4])
        print(x[3])
        if x[4] == a and x[3] == b:
            if (x[7] == "admin"):
                import admin
            elif (x[7] == "user"):
                import user
    print("invalid inputs please try again")
    s1()

s1()