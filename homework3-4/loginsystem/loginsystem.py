#Student name, date, simple login program
#import packages
import sys, time
import string, random


def generate_random_password():
    ## characters to generate password from
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    ## length of password from the user
    
    length = int(input("Enter password length: "))

    ## shuffling the characters
    random.shuffle(characters)
    ## picking random characters from the list
    createpassword = []
    for i in range(length):
        createpassword.append(random.choice(characters))

    ## shuffling the resultant password
    random.shuffle(createpassword)

    ## converting the list to string
    ## printing the list
    print("".join(createpassword))
    return "".join(createpassword)   




def UserLogin():

    Username=input("please enter your username: ")
    Password=input("please enter your password: ")
    with open("accounts.txt","r") as file:
        content = file.readlines() # generate a list
        for line in content:
            
            strippedline=line.split(" ")
            print(strippedline)
            getuser=strippedline[0].strip()
            getpassword=strippedline[1].strip()
            print(getuser, getpassword)
            if(Username==getuser and Password==getpassword):
                print(getuser, getpassword)
                print("welcome back")
                return "login successful"
    print("login fail")
                 
    
    return None
    
def CreateAccount():
    username=input("please enter a valid username: ")
    file=open("accounts.txt","r")
    info=file.read()
    print(info)
    if username in info:
        return print("sorry this "+username+" akready used")
    else:
        print("---please state how you want the password---")
        print("Enter (a) to create your own password or (r)to generate one")
        p=input("please choose (a) or (r): ")
        if (p=="a" ):
            password=input("enter your own password: ")
        elif (p=="r"):
            password=generate_random_password()
        
        #now ready to register username and password
        with open("accounts.txt","a") as file:
            file.write(username+" "+password+"\n")
            print("your account has been registered")
            print("please login")


    return None

def ViewAccounts():
    administrators=["admin", "admin123", "admin1", "admin2"]

    string=" ".join(administrators)
    #print(string)
    print("---------------\n")
    print("Entering View Accounts() procedure\n")
    print("---------------\n")
    #open the file in read mode and read line by line and display on screen. This will display all the account details from the file.
    validlogin, username=UserLogin()
    #print(validlogin, username)
    if validlogin:
        print("list of accounts (usernames and passwords)\n")
        f=open("accounts.txt","r")
        for line in f:
            if username in administrators:
                userlist, password=line.split(" ")
                print(userlist,"==", password)
                #print(userlist)
                if userlist not in administrators:
                    print(line.strip())
          
        f.close
    else:
        print("sorry only adminstrators can view accounts")


    return None
       
 
def logoff(i):
    #option c exits the program after a delay of 2 seconds
    print("\n Signal "+str(i) + " Exiting program...")
    time.sleep(2)
    sys.exit()


def UserProcess():
    username = ""
    password = ""
    print("\n\nWelcome to Login and Registration system...")
    print("\nWould you like to:")
    #print the main menu
    print("\nL) Login")
    print("N) Create new account")
    print("V) View accounts")
    print("Q) Quit")
    
    #enter the menu choice
    i = input("\nChoose [l/n/v/q]: ")
# Login option
    if (i == "l" or i == "L"):
        UserLogin()
    elif (i == "n" or i == "N"):
        CreateAccount()
    elif (i == "v" or i == "V"):
        ViewAccounts()
    elif (i == "q" or i == "Q"):
        logoff(i)
  



while True:
    UserProcess()
