import os
os.system("tput setaf 1")
print("\t\t\t Program for Linux User")
os.system("tput setaf 7")
print("\t\t\t------------------------")

password = getpass.getpass("\tEnter Your Password: ")
passwd = "123456"
os.system("clear")
if password != passwd:
    print("Authentication Failed")
    exit()


print("""\t\t\t  Options to Run Programs
\tType "l" for locally login or Type "r" for remotely login or Type "ri" for remotely login with IP address: """, end="")
location_options=input()
if location_options == "ri":
    remoteIP = input("Enter Your IP: ")

while True:
    print("""\t\tPress 1: Date
    \t\tPress 2: Calender
    \t\tPress 3: Web Server Configuration
    \t\tPress 4: Create User
    \t\tPress 5: Creating and Changing Password
    \t\tPress 6: Deleting User
    \t\tPress 7: Create File
    \t\tPress 8: Exit""")

    print("\tEnter Number :", end=" ")
    ch=input ("")

    if location_options == "l":
        if int(ch) == 1:
            os.system("date")
        elif int(ch) == 2:
            os.system("cal")
        elif int(ch) == 3:
            os.system("yum install httpd")
        elif int(ch) == 4:
            print ("UserName: ", end="")
            create_user=input()
            os.system("sudo useradd {}".format(create_user))
        elif int(ch) == 5:
            print ("UserID: ", end="")
            create_password=input()
            os.system("sudo passwd {}".format(create_password))
        elif int(ch) == 6:
            print ("Deleting UserName: ", end="")
            delete_username=input()
            os.system("sudo userdel {}".format(delete_username))
        elif int(ch) == 7:
            print("FileName: ", end="")
            create_file=input()
            os.system("touch {}".format(create_file))
        elif int(ch) == 8:
            exit()
        else:
            print("Option Not Supported")
        
        input("Enter To Continue .......")
        os.system("clear")

    elif location_options == "r":
        if int(ch) == 1:
            os.system("ssh 172.31.94.231 date")
        elif int(ch) == 2:
            os.system("ssh 172.31.94.231 cal")
        elif int(ch) == 3:
            os.system("ssh 172.31.94.231 yum install httpd")
        elif int(ch) == 4:
            print ("UserName: ", end="")
            create_user=input()
            os.system("ssh 172.31.94.231 sudo useradd {}".format(create_user))
        elif int(ch) == 5:
            print ("UserID: ", end="")
            create_password=input()
            os.system("ssh 172.31.94.231 sudo passwd {}".format(create_password))
        elif int(ch) == 6:
            print ("ssh 172.31.94.231 Deleting UserName: ", end="")
            delete_username=input()
            os.system("ssh 172.31.94.231 sudo userdel {}".format(delete_username))
        elif int(ch) == 7:
            print("FileName: ", end="")
            create_file=input()
            os.system("ssh 172.31.94.231 touch {}".format(create_file))
        elif int(ch) == 8:
            exit()
        else:
            print("Option Not Supported")
       
        input("Enter To Continue .......")
        os.system("clear")

    elif location_options == "ri":
        if int(ch) == 1:
            os.system("ssh {0} date".format(remoteIP))
        elif int(ch) == 2:
            os.system("ssh {0} cal".format(remoteIP))
        elif int(ch) == 3:
            os.system("ssh {0} yum install httpd".format(remoteIP))
        elif int(ch) == 4:
            print ("UserName: ", end="")
            create_user=input()
            os.system("ssh {0} sudo useradd {1}".format(remoteIP, create_user))
        elif int(ch) == 5:
            print ("UserID: ", end="")
            create_password=input()
            os.system("ssh {0} sudo passwd {1}".format(remoteIP, create_password))
        elif int(ch) == 6:
            print ("Deleting UserName: ", end="")
            delete_username=input()
            os.system("ssh {0} sudo userdel {1}".format(remoteIP, delete_username))
        elif int(ch) == 7:
            print("FileName: ", end="")
            create_file=input()
            os.system("ssh {0} touch {1}".format(remoteIP, create_file))
        elif int(ch) == 8:
            exit()
        else:
            print("Option Not Supported")

        input("Enter To Continue .......")
        os.system("clear")

    else:
        print("Location is not supported!!!!!")
































