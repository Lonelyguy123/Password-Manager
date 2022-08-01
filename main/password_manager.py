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
        print("The generated password is",random.choice(mixture),end="")
