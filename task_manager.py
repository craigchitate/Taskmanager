#only admin is allowed to login in this program
#the username is admin and the passord  is adm1n
#without admin username and password the user cannot access
#admin needs to login first
#no other user can access this program to register the users or view tasks
#so any random user cannot login this program
#unless the user is registerd thats when they can open and view other tasks  but they cannot register users
#the passwords are stored in user.txt file
#if the user is registerd they can access the menu but they cannot register another user

from datetime import date #imports the current date

def login():
    login_value = False
    u_username = input("Insert Username:")
    u_password = input("Insert Password:")
    with open('user.txt','r') as f:
        
        data = f.readlines()
        for line in data:
            
            s_username = line.split(',')[0]
            s_password = line.split(',')[1].strip()

            if s_username != u_username:
                continue
            if s_username == u_username:
                if s_password == u_password:
                    print("logged In as" + u_username)
                    return s_username 
                else:
                    print("invalid password")
                    login()
    print("user not found")
    login()

    



def register():
    print("Register New User")
    
    new_username = input("New Username:")
    new_password = input("New Password:")
    conf_password = input("confirm password")
    if new_password == conf_password:
        with open("user.txt",'a') as f:
            f.write(new_username + "," + new_password + '\n' )
            f.close()
    else:
        print("password does not match \n")
        register()


def addTask():#allows users to add tasks 
    print("Adding New Tasks \n")
    username = input("Assignee username:")
    taskTittle = input("Title Of Task:")
    taskdescript = input("Description Of Task:")
    dueDate = input("Due Date:")
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    with open ("tasks.txt" ,'a') as f:
               f.write('\n' + username+ ","+ taskTittle + "," + taskdescript + ","+ today + dueDate + "NO")
    
    
    
def viewTask(): #allows users to view tasks 
    print("Viewing Available Tasks \n")
    with open ("tasks.txt",'r') as f:
        for line in  f:
            task = line.split(",")
            line = ''
            for element in task:
                line = line + '\t' + element 
            print(line)


            print("\n")

def viewMyTask():#allows users to view their own tasks 
    print("Viewing Tasks For User" + s_username + "\n")
    with open ("tasks.txt",'r') as f:
        for line in f:
            if line.split(",")[0] == s_username:
                print(line)
                


def makeChoiceAdmin(): #allows admin to make his/her choice by either registering users or viewing tasks 
    print("r - register user \n")
    print("s - View Statistics \n")
    
def stats():
    taskNum = 0
    with open("tasks.txt",'r') as f:
        for line in f:
            taskNum +=1
    userNum = 0
    with open('user.txt',"r") as f:
        for line in f:
            userNum += 1
            
    stat = " Number Of Tasks " + str(taskNum) + " \n Number Of Users " + str(userNum)
    print(stat)
    


def makeChoice(s_username):#allows user to make choice
    print("please select one the following options: \n")
    if s_username == "admin":
        makeChoiceAdmin()
    print("a - add task \n")
    print("va - view all my task \n")
    print("vm- view my task \n")
    print("e - exit \n")

    choice = input("Insert Option:")

    if choice == "r" and s_username == "admin":
        register()
    elif choice == "s" and s_username == "admin":
        stats()
    elif choice == "a":
        addTask()
    elif choice == "va":
        viewTask()
    elif choice == "vm":
        viewMyTask()
    elif choice == "e":
        exit()
          
    else:
        print("Invalid Selection")
    makeChoice()
        
s_username = login()
makeChoice(s_username)
