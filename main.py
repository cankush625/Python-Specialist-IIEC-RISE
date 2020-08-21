import os
import time

os.system("tput setaf 1")
print("\t\t\t\tWelcome to Your Assistant!")
os.system("tput setaf 7")
print("\t\t\t--------------------------------------------")

flag = "y"

def launchGoogleChrome():
    print("Sure")
    time.sleep(1)
    os.system("start chrome")

def launchNotepad():
    print("SureN")
    time.sleep(1)
    os.system("notepad")

def launchVSCode():
    print("SureVS")
    time.sleep(1)
    os.system("code")

def launchFileExplorer():
    print("SureF")
    time.sleep(1)
    os.system("explorer")

def launch():
    print("Sure")
    time.sleep(1)
    os.system("start chrome")

while(flag == "Y" or flag == "y"):
    userRequest = input("Tell me what to do: ")

    if (("chrome" in userRequest) and (("start" in userRequest) or ("open" in userRequest))):
        launchGoogleChrome()
    elif (("notepad" in userRequest) and (("open" in userRequest) or ("start" in userRequest) or ("launch" in userRequest))):
        launchNotepad()
    elif ((("visual" in userRequest) or ("vs" in userRequest)) and (("start" in userRequest) or ("open" in userRequest) or ("launch" in userRequest))):
        launchVSCode()
    elif ((("file" in userRequest) and ("explorer" in userRequest)) and (("start" in userRequest) or ("open" in userRequest) or ("launch" in userRequest))):
        launchFileExplorer()
    else:
        print("Unable to perform!")
    flag = input("do you want to continue? Press Y/y for yes or N/n for no")