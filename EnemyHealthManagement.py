#!/usr/bin/env python3
#This function checks for doneness in a section in the main program
def UserDonenessCheck():
    userDoneness = input("Are you done here? {yes/no}")
    output = ""
    while len(output) == 0:
        if userDoneness.lower() == "yes":
            output = "True"
        elif userDoneness.lower() == "no":
            output = "False"
        else:
            print("Invalid answer, try again please!")
            userDoneness = input("Are you done here? {yes/no} ")
    return output

enemyNames = []         #initialise both lists to be used in the 1st option
enemyHealthScores = []

#main program
quit = False
while quit != True:
    #Start menu
    print("Joe's Battle Manager")
    print("What would you like to do?")
    print("1 - Enter monsters")
    print("2 - Change health of monsters")
    print("3 - Show current monsters in memory")
    print("4 - Save to text file")
    print("Quit/Q/q - quit program - ")
    userInput = input("Option selection: ")
    #first option - enter monsters
    if userInput == "1":
        userDoneness = "False"
        while userDoneness != "True":
            #ask user for number of monsters so that the for loop works
            numOfEnemies = input("How many enemies are the players battling? ")

            #ask user for monsters and their HP
            for i in range(int(numOfEnemies)):
                enemyName = input("Enter the name of the monster or pack of monsters: ") #using raw_input here works better than input() for some reason - gives "SyntaxError: unexpected EOF while parsing" 
                enemyNames.append(enemyName)
                enemyHP = 0
                while enemyHP == 0:
                    try:
                        enemyHP = int(input("Enter the health of the monster or pack of monsters: "))
                    except:
                        print("Non-valid input. Please enter a valid HP please.")
                    else:
                        enemyHealthScores.append(enemyHP)

            #show the user what they have put into the lists
            print("The list of enemies you have so far are: ")  
            print("Enemy name | HP")
            print("---------------")
            for i in range(len(enemyNames)):
                print(enemyNames[i] + " | " + str(enemyHealthScores[i]))
            
            #check if user is done with this section
            finishedCheck = UserDonenessCheck()
            if finishedCheck == "False":
                pass
            else:
                userDoneness = "True"
        print("")
    
    #second option - edit health of monsters
    elif userInput == "2":
        desiredEnemy = input("Which enemy's health do you want to change? ")
        indexOfDesiredEnemey = enemyNames.index(desiredEnemy)
        while enemyHP == 0:
            newHP = input("What is the new health being added/removed? ")
            try:
                enemyHP = int(input("Enter the health of the monster or pack of monsters: "))
            except:
                print("Non-valid input. Please enter a valid HP please.")
            else:
                enemyHealthScores[indexOfDesiredEnemey] = enemyHealthScores[indexOfDesiredEnemey] + int(newHP)
        print("New health of " + enemyNames[indexOfDesiredEnemey] + " is " + str(enemyHealthScores[indexOfDesiredEnemey]) + "\n")
    
    #third option - show current enemies in memory
    elif userInput == "3":
        print("The list of enemies you have so far are: ")  
        print("Enemy name | HP")
        print("---------------")
        for i in range(len(enemyNames)):
            print(enemyNames[i] + " | " + str(enemyHealthScores[i]))
        print("")
    
    #fourth option - save to a file
    elif userInput == "4":
        saveFileName = input("Enter the name of the save file: ")
        saveFile = open(saveFileName, "w+")
        for i in range(len(enemyNames)):
            saveFile.write(enemyNames[i] + " | " + str(enemyHealthScores[i]))
        saveFile.close()
        print("")

    #Quit program
    elif userInput.lower() == "quit" or userInput.lower() == "q":
        quit = True
    else:
        print("Invalid input. Please enter a valid input.\n")
