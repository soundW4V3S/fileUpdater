def checkTime(): # Checks through user input if they'd like to continue updating/removing

    recurrence = 1

    while recurrence == 1:
        
        simpleCheck = input("\nContinue? (y/n): ")
    
        if simpleCheck == "y":
            finalCheck = "y"
            recurrence = 0
        elif simpleCheck == "n":
            finalCheck = "n"
            recurrence = 0
            print("\nThank you for using the File Updater!")
        else:
            print("\n-- Prompt invalid --")

    return finalCheck

def fileContents(): # Opens up nameFile.txt (File name can be changed with editing)
    
    inFile = open('nameFile.txt', 'r')
    print("\n\nFile contents:")
    print("--------------\n\n")
                
    for i in inFile:
        print(f"{i}")
                    
        
    inFile.close()
    

def main(): # Checker variable loops until checkTime function is given an input of "n"

    checker = "y"
    
    print("Welcome to the File Updater")
    print("---------------------------\n")
    print("How will you choose to update?")

    while checker == "y":

        mainRecurrence = 1
    
        while mainRecurrence == 1:
            
            print()
            x = input("Please select (update/remove) (case sensitive): ")
    
            
            if x == "update":
                    
                fileContents()
            
                y = input("\n\nUpdate with: ")
                y = str(f"\n{y}")
                z = y.strip("\n")
            
                secondInFile = open('nameFile.txt', 'a')
                    
                secondInFile.write(y)
                secondInFile.close()
        
                print(f"\nTerm '{z}' has been added to the nameFile.")
                    
                checker = checkTime()
                mainRecurrence = 0
                    
        
            elif x == "remove":
                    
                fileContents()
        
                y = input("\n\nRemove term: ")
        
                newList = []
        
                with open('nameFile.txt', 'r') as removeInFile:
                    for line in removeInFile:
                        if line.strip() != y:
                            newList.append(line.strip())
        
                with open('nameFile.txt', 'w') as reAddToFile:
                    reAddToFile.write('\n'.join(newList))
        
                print(f"\nTerm '{y}' has been removed.")
        
                checker = checkTime()
                mainRecurrence = 0
        
            else:
        
                print("\n-- Prompt invalid --")


main()
