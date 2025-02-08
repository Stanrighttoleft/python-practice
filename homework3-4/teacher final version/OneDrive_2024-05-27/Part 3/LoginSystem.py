#Ming Chi Hsiao, 27/05/2024, simple login programS
#import packages
import sys ,time   # internal modue
import string, random # internal modules


def generate_random_password():
    ## characters to generate password from
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    ## length of password from the user
    
    length = int(input("Enter password length: "))

    ## shuffling the characters
    random.shuffle(characters)
    ## picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    print("".join(password))
    return "".join(password)   


# login function
def Login():
    '''
    version1:
    
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

    input username and password:
    username = ask the user for username:
    password = ask the user for password:
    '''
    username = input("Please Enter your Username: ")
    password = input("Please Enter your Password: ")
    # read accounts.txt and search for valid username:
    file = open("accounts.txt", "r")  # Open accounts file for reading
    info = file.read() # read the whole as a string
    # testing reading the accounts.txt file
    #print(">>>"+info+"<<<") # I proved the file is a string
    file.close()
    infolist= info.split()
    # test the contents of the string that we read from accounts 
    #print(infolist)
    if username in infolist: # check my username is already in accounts.txt
        index = infolist.index(username) +1 # gent the index of the password in accounts.txt
        account_password = infolist[index]
        #test if it work by print it out
        #print(account_password)
        if password == account_password:
            print("Welcome Back "+ username+ " Login Successful")
            return [True,username]
        else:
            print("Sorry "+ username + ": password invalid")
            return [False,username]
    else:
        print("Sorry  "+ username+ " Login denied")
        return [False,username]
    

# Register function
def Register():
    username = input("Please Enter a valid username: ")
    file = open("accounts.txt", "r")  # Open accounts file for reading
  
    info = file.read() # read the whole as a string
    file.close()
    #print(info)
    if username in info:
       return print("Sorry username:  "+ username + " already Exisits")
    else:
        print("============= password handling ===================")
        print("Enter (a) to create your own password, or (e) to generate password")
        p = input("Please choose (a) or (e) : " )
        if p == "a":
            password = input("Enter your own password: ")
        elif p == "e":
            password = generate_random_password()
        # now ready to register username and assword:
        with open("accounts.txt", "a") as file:
            #writeline = "\n"+username + " " + str(password)
            #print(writeline)
            file.write("\n"+username + " " + password)
            print("Your account has been registered ")
            print("Please login")
 
def View():
    Administrators = ["admin", "admin2" ]
    string = " ".join(Administrators) 
    #print(string)
    print("------------------------------------\n")
    print("Entering View Accounts() procedure  \n")
    print("------------------------------------\n")
    #open the file in read mode and read line by line and display on 
    #screen. This will display all the account details from the file.
    validlogin, username = Login()
    #print(validlogin, username)
    if validlogin:
        print("List of accounts (usernames and Passwords):\n")
        f = open("accounts.txt","r")
        for line in f:
            if username in Administrators:
                userlist, password =line.split(" ") 
                #print(userlist,"==", password)
                #print(userlist)
                if userlist not in Administrators:
                    print(line.strip())
            if username not in Administrators:
                print("Sorry Only Adminstrators can view accounts")  
                return      
        f.close
    else:
        print("Sorry Only Adminstrators can view accounts")
        
    
     
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
    print("R) Register new account")
    print("V) View accounts")
    print("Q) Quit")
    
    #enter the menu choice
    i = input("\nChoose [l/r/v/q]: ")
# Login option
    if (i == "l" or i == "L"):
        Login()
    elif (i == "r" or i == "R"):
        Register()
    elif (i == "v" or i == "V"):
        View()
    elif (i == "q" or i == "Q"):
        logoff(i)
  

while True:
    UserProcess()

