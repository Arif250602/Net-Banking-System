# Ph length 10 digits
# Forgot password

import random
def phnochk():
    phno = int(input("Enter Phone number: "))
    chkphno = str(phno)
    if (len(chkphno) == 10):
        global password
        password = input("Enter password: ")
        print("-----------------")
        print("CONGRATS!! for opening an account with us")
        print("Enjoy our 24/7 service!!")
        print("-----------------")
        print("Now log in to your account.\nTHANK YOU!")
        print(login())
    else:
        print("Enter a 10-digit Number!!")
        phnochk()
def otpgen():
        otp = random.randint(1000, 9999)
        print("OTP:", otp)
        user = int(input("Enter OTP: "))
        if (otp == user):
            print("Access granted!!\n")
            print("--------------")
        else:
            print("Access denied :(\n")
            otpgen()
def createacc():
    global password
    name = str(input("Enter your name: "))
    phnochk()

def login():
    global password
    name = str(input("Enter username: "))
    userpass = input("Enter password: ")
    if (password != userpass):
        print("Enter 1 to change the password ")
        print("Forgot Password?")
        print("Enter 2 to log in again")
        forgotinp=int(input("Enter the operation to be performed"))
        if(forgotinp==1):
            password=input("Enter new password: ")
            print("Password changed successfully.")
            login()
        elif(forgotinp==2):
            login()
    otpgen()
    print("Welcome!!", name, ".")
    print("1.Transfer fund\n2.Accounts\n3.Mini Statement")
    loginp = int(input("Enter the operation no. to be performed: "))

print("Online net banking")
print("-------------------")
print("1.Create New Account\n-------------------")
def home():
    inp = int(input("Enter the operation no. to be performed: "))
    if (inp == 1):
        print(createacc())
    else:
        print("ERROR!! Enter the correct operation no.")
        home()
home()