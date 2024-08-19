name= input("Type your name: ")
print("Welcome", name,"to this adventure!")

answer = input ("You are on a road, you can go 'left' or 'right': ")

if answer == "left":
    answer= input ("there are other two paths, do you want to 'swim' the lake or 'cross' the fence: ")
    if answer == "swim":
        print ("you have been eaten by an aligator")
    elif answer == "cross":
        print ("you won")
    else:
        print("Not a valid option")
elif answer== "right":
    print ("there is no path")
else:
    print ("Not a valid option")