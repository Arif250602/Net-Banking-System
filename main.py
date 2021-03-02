# Ph length 10 digits
# Forgot password

import random

names = []
amount = []
bal = 0

def createacc():
    global password
    name = str(input("Enter your name: "))
    phnochk()
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
    print("Welcome!!", str.title(name), ".")
    welcome()
def welcome():

    print("1.Add Amount\n2.Transfer Fund\n3.Available Balance\n4.Account Statement")
    homeinp = int(input("Enter the operation no. to be performed: "))
    if(homeinp==1):
        addamt()
    elif(homeinp==2):
        transfund()
    elif(homeinp==3):
        balance()
    elif(homeinp==4):
        statement()
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
def addamt():
    print("")
    bank=input("From Which Bank: ")
    add=int(input("Amount: "))
    userpass=input("Password: ")
    otpgen()
    global bal
    bal=bal+add
    print("Amount added successfully!!")
    print("")
    welcome()
def balance():
    print("")
    print("AVAILABLE BALANCE:")
    print(bal)
    print("")
    welcome()
def statement():
    print("")
    for i in range(0,len(names)):
        print(i+1,".","Transferred ",amount[i]," Rupees to ",str.title(names[i]))
    print("")
    welcome()

def transfund():
    print("")
    print("TRANSFER FUND:")
    print("1.RTGS(Amt>2,00,000)\n2.NEFT(Amt<2,00,000)\n3.IMPS(Fast transfer)")
    mode=int(input("Enter the Mode Number: "))
    if(mode==0 or mode>=4 or mode<0):
        print("ERROR!?!?! Enter the correct operation no.")
        transfund()
    else:
        receiver = str(input("Receiver account name: "))
        amt = int(input("Amount: "))
        userpass = input("Password: ")
        otpgen()
        print("Amount ",amt," Transferred to ",receiver," successfully!!")
        names.append(receiver)
        amount.append(amt)
        global bal
        bal=bal-amt
        print("")
        welcome()
statement()
print("\nONLINE NET BANKING")
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