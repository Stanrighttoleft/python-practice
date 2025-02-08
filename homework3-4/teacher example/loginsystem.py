#Student name, date, simple login program
#import packages
import sys, time
import string, random


def generate_random_password():
    password = "got the password"
    return password
 




def UserLogin():
    return None
    
def CreateAccount():
    return None
 
def ViewAccounts():
    return None
       
def GeneratePassword(username):
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
