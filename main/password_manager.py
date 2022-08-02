import mysql
import mysql.connector

conn=mysql.connector.connect(host='localhost',
                            user="root",
                            password="123rootsql")
                            
if conn.is_connected():
    print("""--------------------------------Password Manager----------------------------------
    
    """)
    
cursor=conn.connect()
cur=conn.cursor()


def install():
    cur.execute("CREATE DATABASE passwordmng;")
    cur.execute("use passwordmng;")
    cur.execute("CREATE TABLE passwordmanager(name varchar(15),website varchar(30),password varchar(30));")
    conn.commit()
    print("Application setup successfully finished")

def gen():
    import random
    num=['1','2','3','4','5','6','7','8','9','0']
    letter=["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter_cap=['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbol=['!','@','#','$','%','^',"&",'*','?']
    password = ''
    for i in range(0,12):
        f = random.randint(1,4)
        if f==1:
            password = password + num[random.randint(0,9)]
        elif f==2:
            password = password + letter[random.randint(0,25)]
        elif f==3:
            password = password + letter_cap[random.randint(0,25)]
        else:
            password = password + symbol[random.randint(0,8)]
    print("generated password -  ",password)
    name = input("enter your name ")
    website = input("enter the website corressponding to the password")
    cur.execute("INSERT INTO passwordmanager(name,website,password) VALUES('{}','{}','{}');".format(name,website,password))
    conn.commit()
    print("Entry successfully registered")

def find():
    name = input("enter your name ")
    website = input("enter the website's name")
    cur.execute("SELECT * FROM passwordmanager WHERE name = '{}' AND website = '{}';".format(name,website))
    print("Here is the entry registered pertaining to the above details")
    print(cur.fetchone())

def findall():
    name = input("enter your name")
    cur.execute("SELECT * FROM passwordmanager2 WHERE name = '{}';").format(name)
    print("Here are all the entries pertaining to the name -  ",name)
    print(cur.fetchall())
     
c =1     
while c in[1,4] :
   print("Menu")
   print("1.Install the application")
   print("2.generate a password")
   print("3.retrieve a password")
   print("4.retrieve all the passwords pertaining to a specific user")
   print("5.exit the application")


   mento= int(input("enter your choice"))
   if mento==1:
        install()
   elif mento==2:
        gen()
   elif mento==3:
        find()
   elif mento==4:
        findall()
   elif mento==5:
        break
