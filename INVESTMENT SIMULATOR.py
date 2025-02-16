import random as r



import mysql.connector as con

mydb=con.connect(host='localhost',user='root',password='adwaith30',database='invest')
cur=mydb.cursor(buffered=True)


def del_acc():
    us=input("Enter Username of account to Delete : ")
    cur.execute("delete from accounts where username='{}'".format(us))
    cur.execute("delete from shares where username='{}'".format(us))
    mydb.commit()
    print()
    print("Account Deleted")
    print()

def signup():
    uid = input("Enter your Username: ")
    pwd = input("Enter your Password: ")
    cur.execute("SELECT username FROM accounts")
    for i in cur:
        if i[0] == uid:
            print("Username already taken")
            return signup()
    if len(pwd) < 8:
        print("Password must be at least 8 characters long")
        return signup()
    n = input("Enter your Name: ")
    e = input("Enter your email: ")
    p = input("Enter your Phone Number: ")
    a = input("Enter your address: ")
    cur.execute("INSERT INTO accounts VALUES('{}','{}','{}','{}','{}','{}')".format(uid, pwd, n, e, p, a))
    cur.execute("Insert into shares values('{}',0,0,0,0,0,0,0,0,0,0,0,0)".format(uid))
    mydb.commit()
    print("Sign-up successful")

def login():
    for _ in range(3):
        uid = input("Enter your Username: ")
        pwd = input("Enter your Password: ")
        cur.execute("SELECT username, password FROM accounts")
        for i in cur:
            if i[0] == uid and i[1] == pwd:
                print("Login Successful")
                return uid
        else:
            print("Username or Password incorrect. Try again")
    else:
        print("3 incorrect attempts. Try again later")
        return None

def bitcoin():
    print("Bitcoin is one of the first cryptocurrencies to become popular, in the crypto world it is generally a safe option to buy them but as they are cryptocurrencies they can dip in value really fast and are generally expensive")
    print("The prediction of whether the stock will go up or down is:",r.randint(5,20))
    while True:
               
        bt=input("Would you like to buy shares for bitcoin:")
        if bt=='y' or 'yes':
            bt2=int(input("How many shares of bitcoins would you like to buy:"))
            if bt2>50:
                print("you can only buy 50 shares of bitcoin, please buy a financially reasonable amount of bitcoins")
        
            else:
                cur.execute("update shares set bitcoin=bitcoin+{} where username=='{}'".format(bt2,uid))
                mydb.commit()
                break

def ethereum():
    print("ethereum is one of the first cryptocurrencies to become popular, in the crypto world it is generally a slightly risky option to buy them because their values is quite volatile and dips and peaks suddenly")
    print("The prediction of whether the stock will go up or down is:",r.randint(-1,20))
    while True:
               
        et=input("Would you like to buy ethereum:")
        if et=='y' or 'yes':
            et2=int(input("How many shares of ethereum would you like to buy:"))
            if et2>50:
                print("you can only buy 50 shares of ethereum, please buy a financially reasonable amount of ethereum")
        
            else:
                cur.execute("update shares set ethereum=ethereum+{} where username=='{}'".format(et2,uid))
                mydb.commit()
                break
def tesla():
    print("Tesla, Inc. is an American multinational automotive company which designs and manufactures electric vehicles, stationary battery energy storage devices")
    print("The prediction of whether the stock will go up or down is:",r.randint(-3,20))
    while True:
        
        te=input("would you like to buy shares for tesla:")
        if te=='y' or 'yes':
            te2=int(input("How many shares would you like to buy:"))
            if te2>50:
                print("you can only buy 50 shares, please buy a financially reasonable amount of shares")
        
            else:
                cur.execute("update shares set tesla=tesla+{} where username=='{}'".format(te2,uid))
                mydb.commit()
                break
        

def tatamotors():
    print("Tata Motors Limited is an Indian Multinational automotive company, headquartered in Mumbai, and part of the Tata Group. The company produces cars, trucks, vans, and busses. Subsidiaries include British Jaguar Land Rover and South Korean Tata Daewoo")
    print("The prediction of whether the stock will go up or down is:",r.randint(-10,20))
    while True:

        tm=input("Would you like to buy shares for Tata:")
        if tm=='y' or 'yes':
            tm2=int(input("How many shares would you like to buy:"))

            if tm2>50:
                print("you can only buy 50 shares, please buy a financially reasonable amount of shares")
        
            else:
                cur.execute("update shares set Tata=Tata+{} where username='{}'".format(tm2,uid))
                mydb.commit()               
                break

def bethesda():
    print("Bethesda Game Studios, the award-winning development team behind The Elder Scrolls, Fallout and Starfield, Bethesda Game Studios values its employees and their contributions to creating world-class entertainment properties")
    print("The prediction of whether the stock will go up or down is:",r.randint(-20,20))
    while True:

        be=input("Would you like to buy shares for Bethesda:")
        if be=='y' or 'yes':
            be2=int(input("How many shares would you like to buy:"))

            if be2>50:
                print("you can only buy 50 shares, please buy a financially reasonable amount of shares")
        
            else:
                cur.execute("update shares set Bethesda=Bethesda+{} where username='{}'".format(be2,uid))
                mydb.commit()
                break
            
def ubisoft():
    print("Ubisoft Entertainment SA is a French video game publisher headquartered in Saint-Mandé with development studios across the world. Its video game franchises include Assassin's Creed, Far Cry, For Honor, Just Dance, Prince of Persia, Rabbids, Rayman, Tom Clancy's, and Watch Dogs")
    print("The prediction of whether the stock will go up or down is:",r.randint(-5,20))
    while True:

        ub=input("Would you like to buy shares for Ubisoft:")
        if ub=='y' or 'yes':
            ub2=int(input("How many shares would you like to buy:"))

            if ub2>50:
                print("you can only buy 50 shares, please buy a financially reasonable amount of shares")
        
            else:
                cur.execute("update shares set Ubisoft=Ubisoft+{} where username='{}'".format(ub2,uid))
                mydb.commit()
                break
            
def nvidia():
    print("Nvidia Corporation is a prominent American technology company specializing in graphics processing units (GPUs) for gaming, AI, and data center applications, their shares have shown strong growth, driven by demand for their GPUs in gaming, AI, and data centers, making them a tech industry leader.")
    print("The prediction of whether the stock will go up or down is:",r.randint(1,20))
    while True:

        nv=input("Would you like to buy shares for Nvidia:")
        if nv=='y' or 'yes':
            nv2=int(input("How many shares would you like to buy:"))

            if nv2>50:
                print("you can only buy 50 shares, please buy a financially reasonable amount of shares")
        
            else:
                cur.execute("update shares set nvidia=nvidia+'{}' where username='{}'".format(nv2,uid))
                mydb.commit()
    
                break  

def intel():
    print("Intel Corporation is a prominent American semiconductor company primarily known for its CPUs. Over the years, Intel's stock performance has been influenced by market competition, technological shifts, and leadership changes, but it remains a key player in the tech industry.")
    print("The prediction of whether the stock will go up or down is:",r.randint(5,20))
    while True:

        il=input("Would you like to buy shares for Intel:")
        if il=='y' or 'yes':
            il2=int(input("How many shares would you like to buy:"))

            if il2>50:
                print("you can only buy 50 shares, please buy a financially reasonable amount of shares")
        
            else:
                cur.execute("update shares set Intel=Intel+{} where username='{}'".format(il2,uid))
                mydb.commit()
                break
            
def amd():
    print("Advanced Micro Devices (AMD) is a notable American semiconductor company specializing in CPUs and GPUs. AMD's shares have exhibited substantial growth, driven by competitive products and market demand, positioning the company as a significant player in the tech industry.")
    print("The prediction of whether the stock will go up or down is:",r.randint(5,20))
    while True:

        am=input("Would you like to buy shares for Amd:")
        if am=='y' or 'yes':
            am2=int(input("How many shares would you like to buy:"))

            if am2>50:
                print("you can only buy 50 shares, please buy a financially reasonable amount of shares")
        
            else:
                cur.execute("update shares set Amd=Amd+{} where username='{}'".format(am2,uid))
                mydb.commit()

                break
def ecorp():
    print("Evil Corp is one of the largest multi-national conglomerates in the world Among their enterprises, they manufacture computers, phones, and tablets, and maintain a banking and consumer credit division")
    print("The prediction of whether the stock will go up or down is:",r.randint(-25,20))
    while True:

        ep=input("Would you like to buy shares for ecorp:")
        if ep=='y' or 'yes':
            ep2=int(input("How many shares would you like to buy:"))

            if ep2>50:
                print("you can only buy 50 shares, please buy a financially reasonable amount of shares")
        
            else:
                cur.execute("update shares set Ecorp=Ecorp+{}where username='{}'".format(ec2,uid))
                mydb.commit()                

                break
def cdpr():
    print("CD Projekt Red, a Polish video game developer, is famous for The Witcher series and Cyberpunk 2077. Their shares are publicly traded on the Warsaw Stock Exchange (WSE) under the symbol CDR.")
    print("The prediction of whether the stock will go up or down is:",r.randint(5,20))
    while True:

        cdpr=input("Would you like to buy shares for CD project RED:")
        if cdpr=='y' or 'yes':
            cdpr2=int(input("How many shares would you like to buy:"))

            if cdpr2>50:
                print("you can only buy 50 shares, please buy a financially reasonable amount of shares")
        
            else:
                cur.execute("update shares set cdpr=cdpr+{} where username='{}'".format(cdpr2,uid))
                mydb.commit()
                break


def nintendo():
    print("Nintendo is a renowned Japanese video game company, creating iconic franchises like Mario and Legend of Zelda. Their shares trade on the Tokyo Stock Exchange (TSE) under the symbol 7974. Nintendo's stock performance is influenced by console sales, game releases, and industry innovation.")
    print("The prediction of whether the stock will go up or down is:",r.randint(5,20))
    while True:

        nin=input("Would you like to buy shares for Nintendo:")
        if nin=='y' or 'yes':
            nin2=int(input("How many shares would you like to buy:"))

            if nin2>50:
                print("you can only buy 50 shares, please buy a financially reasonable amount of shares")
        
            else:
                cur.execute("update shares set Nintendo=Nintendo+{} where username='{}'".format(nin2,uid))
                mydb.commit()
                break
                
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Buy Shares")
        print("2. Logout")
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            print("Select a company to buy shares from:")
            print("")
            y= print("1.bitcoin", "2.ethereum", "3.tesla", "4.tata-motors", "5.bethesda", "6.ubisoft", "7.Nvidia", "8.intel", "9.amd", "10.ecorp", "11.cdpr", "12.nintendo")
            companies=print(y)
            print("")

            company_choice = int(input("Enter the number next to the company you want to invest in: "))
            print("")
            print("""The number next to the company defines the likeliness of the shares going up or down
                            The less the number the less likely shares will go and more the number the more likely the shares will go up""")

            print("")
            
            if company_choice==1:
                bitcoin()
            elif company_choice==2:
                ethereum()
            elif company_choice==3:
                tesla()
            elif company_choice==4:
                tatamotors()
            elif company_choice==5:
                bethesda()
            elif company_choice==6:
                ubisoft()
            elif company_choice==7:
                nvidia()
            elif company_choice==8:
                intel()
            elif company_choice==9:
                amd()
            elif company_choice==10:
                ecorp()
            elif company_choice==11:
                cdpr()
            elif company_choice==12:
                nintendo()
                
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice == "2":
            print("Logging out...")
            break


while True:
    title=("Welcome to the Investment Simulator!")
    x=title.center(165)
    print(x)
    print("1. Sign-up")
    print("2. Login")
    print("3.delete account")
    print("4. Exit")
    option = input("Enter your choice: ")
    print()
    if option == "1":
        signup()
    elif option == "2":
        uid = login()
        if uid:
            main_menu()
    elif option =="3":
        del_acc()
    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

    




          
