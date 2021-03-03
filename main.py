#An Online Net Banking project by T.Sakthivel, T.Ajay Veerabaghu, S.Mohammed Arif
import random

names = []
amount = []
bal = 0
Pass=[]
def createacc():
    global password
    name = str(input("Enter your name: "))
    phnochk()
def phnochk():
    phno = int(input("Enter Phone number: "))
    chkphno = str(phno)
    if (len(chkphno) == 10):
        global password, Pass
        password = input("Enter password: ")
        Pass.append(password)
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
    global password,Pass
    name = str(input("Enter username: "))
    userpass = input("Enter password: ")
    if (password != userpass):
        print("-----------------")
        print("Forgot Password ?")
        print("Enter 1 to change the password ")
        print("Enter 2 to log in again")
        forgotinp=int(input("Enter the operation to be performed: "))
        if(forgotinp==1):
            password=input("Enter new password: ")
            Pass.clear()
            Pass.append(password)
            print("Password changed successfully.")
            login()
        elif(forgotinp==2):
            login()
    print("---------------")
    print("Welcome!!", str.title(name), ".")
    print("---------------")
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
def addamtbal():
    global bal,add
    bal = bal + add
    print("Amount added successfully!!")
    print("")
    welcome()
def addamt():
    global bal,add
    print("")
    bank=input("From Which Bank: ")
    add=int(input("Amount: "))
    userpass=input("Password: ")
    global bal, Pass
    if(userpass==Pass[0]):
        otpgen()
        addamtbal()
    else:
        print("Incorrect Password!!")
        userpass = input("Password: ")
        addamtbal()
        print("----------------")
        welcome()
def balance():
    print("-----------------")
    print("AVAILABLE BALANCE:")
    print(bal)
    print("-----------------")
    welcome()
def statement():
    print("-----------------")
    for i in range(0,len(names)):
        print(i+1,".","Transferred ",amount[i]," Rupees to ",str.title(names[i]))
    print("-----------------")
    welcome()

def transfund():
    global Pass
    print("")
    print("TRANSFER FUND:")
    receiver = str(input("Receiver account name: "))
    amt = int(input("Amount: "))
    userpass = input("Password: ")
    if(userpass==Pass[0]):
        otpgen()
        print("Amount ", amt, " Transferred to ", receiver, " successfully!!")
        print("-----------------")
        names.append(receiver)
        amount.append(amt)
        global bal
        bal = bal - amt
        print("")
        welcome()
    else:
        print("Incorrect Password!!")
        transfund()

print("\nONLINE NET BANKING")
print("-------------------")
print("Create New Account\n-------------------")
def home():
    createacc()
home()