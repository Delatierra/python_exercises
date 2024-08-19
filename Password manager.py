master_pwd = input ("What is the master password?")

def view():
    with open("password.txt", "r") as file:
        for line in file. readlines():
            print (line.rstrip())

def add():
    name = input("Account Name:")
    pwd= input ("Password: ")

    with open("password.txt", "a") as file:
        file.write(name + "|" + pwd "\n")
              

while True: 
    mode = input ("Would you like to add a new password or view existing ones (view, add), q to break").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode== "add":
        add()
    else:
        print ("Invalid mode.")