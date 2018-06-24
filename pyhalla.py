# Pyhalla v1.0
# A short command line decision game created with Python3.6 based on the Viking era
# Can be run by typing 'python3.6 pyhalla.py' in any terminal/command line
# Python must be installed on the PC
# Created by: Goran Nushkov, June 2018

from sys import exit

# Disables typing of anything other than integers.
def intCheck():
    while True:
        try:
            userInput = int(input('> '))
            return userInput
        except ValueError:
            print(f"Do you know what numbers are, {username}? Please type a number if you do.")
            return intCheck()

# A function that throws an error message if the user input is invalid.
def strError(choiceOne, choiceTwo, funcName):
    print(f"Are you feeling ill, {username}? Decide, " +  choiceOne + " or " +  choiceTwo + ".")
    return funcName()

# Exit function that is called when the user chooses to flee from battle. Ends the script.
def coward():
    print(f"You call yourself a Viking, {username}!? You are exiled into the unknown.")
    exit(1)

# Exit function that is called when the user chooses to stay in the dungeon in Mercia. Ends the script.
def rot():
    print(f"You call yourself a Viking, {username}!? You rot away and never reach Valhalla.")
    exit(1)

# Simple function that prints several dots between events for readability in the terminal.
def dots():
    print("." * 5, end="")

# Asks the user to choose a weapon which is stored in a variable, and returned by the function.
def weaponPicker():
    # Prints a list of the first three weapons. Ragnar's Axe is a mild easter egg.
    print("\nChoose your weapon:")
    for i in range(1, len(weapons)):
        print(str(i) + ".", end="")
        print(weapons[i - 1])

    return weaponConditions()

# Function that checks the user input for the weaponPicker() function.    
def weaponConditions():
    choice = intCheck()

    # Ensures that the user types in a number in range of 1 to 3(4).
    if 1 <= choice < len(weapons):
        chosenWeapon = weapons[choice - 1]
        print(f"You have chosen the {chosenWeapon}.")
        dots()
        return chosenWeapon
    elif choice == 4:
        chosenWeapon = weapons[choice - 1]
        print(f"You have chosen {chosenWeapon}. The gods are pleased with your bright mind, {username}.")
        dots()
        return chosenWeapon
    else:
        print(f"Sorry, these are the only ones available, {username}. Choose one of them.")
        return weaponConditions() 

# Asks the user to choose a companion which is stored in a variable, and returned by the function.
def companionPicker():
    print("\nChoose your faithful companion:")
    for i in range(1, len(companions) + 1):
        print(str(i) + ".", end="")
        print(companions[i - 1])
    
    return companionConditions()

# Function that checks the user input for the companionPicker() function.
def companionConditions():
    choice = intCheck()

    if 1 <= choice < (len(companions) + 1):
        chosenComp = companions[choice - 1]
        print(f"You have chosen {chosenComp} as a companion. Great choice!")
        dots()
        return chosenComp
    else:
        print(f"A companion in battle is like wearing a second armour, {username}. Please pick one.")
        return companionConditions()

# Start function that starts after a weapon and a companion are chosen.
def start(comp):
    print("\nYou arrive in Wessex on a boat built by Floki the Builder.")
    print("You are a part of the Great Heathen Army, preparing to raid everything from Wessex to Northumbria.")
    print("You have decided that you are old and it's time to meet the sharp end of the blade and reach Valhalla!")
    print(f"{comp} will fight along you until the end, so you know a great battle lies ahead!\n")
    print(f"{comp} sees a road ahead. He asks for your wisdom. Help him choose if he should lead right or left.")
    
    startConditions()

# Conditions that make the user type anything that contains left or right in it.
def startConditions():
    direction = input('> ')
    
    if "left" in direction and "right" in direction:
        strError("left", "right", startConditions)
    elif "Left" in direction and "Right" in direction:
        strError("left", "right", startConditions)
    elif "Left" in direction and "right" in direction:
        strError("left", "right", startConditions)
    elif "left" in direction and "Right" in direction:
        strError("left", "right", startConditions)
    elif "left" in direction or "Left" in direction:
        winchester(chosenWeapon, chosenCompanion)
    elif "right" in direction or "Right" in direction:
        abingdon(chosenWeapon, chosenCompanion)
    else:
        strError("left", "right", startConditions)

# Function that is called when the user chooses to go left.
def winchester(wep, comp):
    print("\nYou arrive in a town called Winchester. The Saxons know you are here and have prepared!")
    print(f"You take out your {wep} and look at {comp}. You both start yelling and dive into battle.")
    print("After a short battle, the Vikings won. But suddenly, three Saxons show up and attack you. What do you do?")

    for i in range(1, len(winchesterBattleOptions) + 1):
        print(str(i) + ".", end="")
        print(winchesterBattleOptions[i - 1])

    winchesterConditions()

# Conditions that make the user type in a number only.
def winchesterConditions():
    choice = intCheck()

    if choice == 1:
        print("The gods have given you strength and your berserk attack slashed them all! You can proceed to Mercia now.")
        dots()
        mercia(chosenWeapon, chosenCompanion)
    elif choice == 2:
        print("Loki the trickster is pleased with you. The Saxons were tricked into slashing each other! You can proceed to Mercia now.")
        dots()
        mercia(chosenWeapon, chosenCompanion)
    elif choice == 3:
        coward()
    else:
        print("You must choose quickly! Select one of the available options.")
        return winchesterConditions()

# Function that is called when the user chooses to go right.
def abingdon(wep, comp):
    print("\nYou arrive in a town called Abingdon. Their king Ecbert seems to be here too!")
    print(f"You take out your {wep} and look at {comp}. You both start yelling and dive into battle.")
    print(f"You see that {comp} is surrounded by King Ecbert himself and his guards! How are you going to help him?")

    for i in range(1, len(abingdonBattleOptions) + 1):
        print(str(i) + ".", end="")
        print(abingdonBattleOptions[i - 1])

    abingdonConditions()

# Conditions that make the user type in a number only.
def abingdonConditions():
    choice = intCheck()

    if choice == 1:
        print("Your experience in battle is proved once again! King Ecbert's head lies on the ground! You can proceed to Mercia now.")
        dots()
        mercia(chosenWeapon, chosenCompanion)
    elif choice == 2:
        print("Your wisdom helped your faithful companion! After you crushed the guards, Ecbert was alone and smashed to pieces! You can proceed to Mercia now.")
        dots()
        mercia(chosenWeapon, chosenCompanion)
    elif choice == 3:
        coward()
    else:
        print("You must choose quickly! Select one of the available options.")
        return abingdonConditions()

# Function that is called from both winchester() and abingdon() functions when the user finishes working with them.
def mercia(wep, comp):
    print("\nAfter your victory in Wessex, you arrive in Mercia.")
    print("The Great Heathen Army has had a long run and decided to set up a camp. After a long feast, you fell asleep.")
    print("The camp is ambushed by some strong warriors and you are taken as their prisoner.")
    print(f"They have taken your {wep} and you see {comp} running to help you, but it's all in vain.")
    print("After few nights in the dungeon, you see your chance to escape, as both of the guards are asleep.\n")
    print("You see a shiv on the ground in the dungeon. What is your plan?")

    for i in range(1, len(merciaDungeonOptions) + 1):
        print(str(i) + ".", end="")
        print(merciaDungeonOptions[i - 1])

    merciaConditions()

# Function that makes the user type in numbers only.
def merciaConditions():
    choice = intCheck()

    if choice == 1:
        print("You sneaky bastard! You have escaped and rejoined the Great Heathen Army. They have raided everything while you were gone. You can proceed to Northumbria now.")
        dots()
        northumbria(chosenCompanion)
    elif choice == 2:
        print("You brute! You have escaped and rejoined the Great Heathen Army. They have raided everything while you were gone. You can proceed to Northumbria now.")
        dots()
        northumbria(chosenCompanion)
    elif choice == 3:
        rot()
    else:
        print("You must choose quickly! Select one of the available options.")
        return merciaConditions()

# Function that is called from mercia() when the user finishes working with it.
def northumbria(comp):
    print("\nAfter the events in Mercia, you finally arrive in Northumbria, where you meet the filthy King Aelle.")
    print(f"He surrenders after seeing the might of the Great Heathen Army, and {comp} proposed a Blood Eagle death sentence!\n")
    print(f"{comp} wants to give you the honor of doing it. Do you accept?")
    
    northumbriaConditions()

# Function that checks the user input and accepts only specific words or sentences with the word in them.
def northumbriaConditions():
    decision = input('> ')

    if "yes" in decision and "no" in decision:
        strError("yes", "no", northumbriaConditions)
    elif "Yes" in decision and "No" in decision:
        strError("yes", "no", northumbriaConditions)
    elif "Yes" in decision and "no" in decision:
        strError("yes", "no", northumbriaConditions)
    elif "yes" in decision and "No" in decision:
        strError("yes", "no", northumbriaConditions)
    elif "yes" in decision or "Yes" in decision or "y" in decision:
        end(chosenWeapon, chosenCompanion)
    elif "no" in decision or "No" in decision or "n" in decision:
        coward()
    else:
        strError("yes", "no", northumbriaConditions)

# End function that ends the script successfully
def end(wep, comp):
    print(f"\n{comp} gives you his axe and you skinned the god out of Aelle!")
    print("But suddenly you feel a knife through your back! You turn around and see a priest shaking with blood on his hands!")
    print(f"{comp} takes your {wep} and cuts his head off. You fall on the ground and start laughing about the way you are going to Valhalla.")
    print(f"{comp} and all of the Vikings start yelling your name as they send you to the hall of the mighty gods and heroes.")
    print("You die with a smile on your face. You finally met your destiny and reached Valhalla where you are laughing with the gods about the way you died for eternity.\n")
    print("Thanks for playing Pyhalla v1.0 !")

    exit(0)

# Global lists used in the functions.
weapons = ['Sword', 'Axe', 'Spear', 'Ragnar\'s Axe']
companions = ['Ragnar', 'Floki', 'Bjorn', 'Rollo', 'Ivar', 'Ubbe']
winchesterBattleOptions = ['Do a furious berserk attack.', 'Try to trick them into attacking each other.', 'Flee.']
abingdonBattleOptions = ['Throw your weapon at King Ecbert furiously.', 'Run after Ecbert\'s guards first', 'Flee']
merciaDungeonOptions = ['Grab the shiv, pick the lock, take your weapon and silently leave.', 
                        'Call one of the guards, bash his head, take his keys, grab your weapon, and fight everyone on your path.', 
                        'Stay in the cell and wait for your companions to release you.']

# Greets the user and asks for his username. Only alphabetic characters are allowed.
print("Welcome to Pyhalla v1.0\n")
while True:
    username = input('Enter your name.\n> ')
    if username.isalpha():
        break

# Calls the weaponPicker() function and stores the chosen weapon in a variable.
chosenWeapon = weaponPicker()

# Calls the companionPicker() function and stores the chosen companion in a variable.
chosenCompanion = companionPicker()

# Starts the game.
start(chosenCompanion)
