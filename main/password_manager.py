#password_manager
import random

def password_generator():
    maxlength=12

    num=['1','2','3','4','5','6','7','8','9','0']
    letter=["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter_cap=['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbol=['!','@','#','$','%','^',"&",'*','?']

    mixture=num+letter+letter_cap+symbol

    for x in range(maxlength-4):
        print(random.choice(mixture),end="")

menyoo=1
while menyoo==1:
    print("--------------------------------------Password Manager---------------------------------------")
    print("---------------------------------------version 1.0-------------------------------------------")
    print("""
        1.Password Generator
        2.Add a password
        3.View saved passwords
    """)
    choice=int(input("Enter your choice: "))
    if choice==1:
        password_generator()
    if choice==2:
        print
    if choice==3:
        print
