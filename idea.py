# Pseudo Code
'''
Some game with many rounds
Each round a user can choose to attack or heal
The user will need to kill the boss by the end of the set rounds 
'''

# Importing of Packages

import math
import random

# Object Oriented Programming
class Character:
    
    # Defining Hero name, attack power and health
    def __init__(self, given_name, given_attack_power, given_health):
        self.name = given_name
        self.attack_power = given_attack_power
        self.health = given_health

    # Defining the attack method
    def attack(self, opponent):
            critchance = random.randint(1,150)
            opponent.health -= round((self.attack_power * (critchance/100)),2)
            print(str(self.name) , "attacked", str(opponent.name), "for", str(round((self.attack_power * (critchance/100)),2)) + "\n")

    # Defining the heal method
    def heal(self):
        # insert code here on how to heal hero
        # using math.random function heal the hero between 1-25 health
        # Code Below Here
        randomint = random.randint(1,25)
        self.health += round(randomint,2)
        print(str(self.name), "healed themselves for", randomint, "HP\n")
        

###################################################################################################################
#-----------------------------------------------------------------------------------------------------------------#
###################################################################################################################
'''
# Teaching OOP calling
character = Character("Lightning Mcqueen", 15, 200)
print(character.name)
'''

# Code Below Here
herolist = [Character("Michael Schumacher", 20, 100), Character("Ramone", 30, 100)] # create your heroes using the following format Hero("Name of Hero", Attack Power, Health Points)
opponentlist = [Character("Lightning Mcqueen", 15, 100), Character("Doc Hudson", 20, 100)]

# using python length and random library
herolist_length = len(herolist)
opponentlist_length = len(opponentlist)
randomheroindex = random.randint(0,herolist_length-1)
randomopponentindex = random.randint(0,opponentlist_length-1)

herocharacter = herolist[randomheroindex]
opponentcharacter = opponentlist[randomopponentindex]

print(str(herocharacter.name), "(YOU) VS", str(opponentcharacter.name))
input("Press Enter to continue...")

total_rounds = 16
current_round = 1

###################################################################################################################
#-----------------------------------------------------------------------------------------------------------------#
###################################################################################################################

def opponentturn():
    print(str(opponentcharacter.name) + "'s move")
    movenum = 2 #random.randint(1,2)
    if movenum == 1:
        opponentcharacter.heal()
    else:
        opponentcharacter.attack(herocharacter)

###################################################################################################################
#-----------------------------------------------------------------------------------------------------------------#
###################################################################################################################

while current_round < total_rounds + 1:
    print("Round", current_round, ":\n")
    print("Battle Statistics")
    print("YOU")
    print("---")
    print("Hero Character:", herocharacter.name) 
    print("Hero Health:", round(herocharacter.health,2)) 
    print("Hero Attack Damage:", round(herocharacter.attack_power,2))
    print("")
    print("Opponent")
    print("--------")
    print("Opponent Character:", opponentcharacter.name) 
    print("Opponent Health:", round(opponentcharacter.health,2)) 
    print("Opponent Attack Damage:", round(opponentcharacter.attack_power,2))
    print("---------------------------")
    print("1. Attack\t\t2. Heal")
    print("3. Exit Game\n")
    userinput = input("Enter option: ")
    if userinput == "1":
        herocharacter.attack(opponentcharacter)
        opponentturn()
        input("Press Enter to continue...")
    elif userinput == "2":
        herocharacter.heal()
        opponentturn()
        input("Press Enter to continue...")
    elif userinput == "3":
        break
    else:
        print("Invalid option\n")
        continue
    if opponentcharacter.health <= 0:
        print("\n============== CONGRATULATIONS ==============")
        print(herocharacter.name, "has won the game")
        print("Total rounds survived:", current_round)
        break
    elif herocharacter.health <= 0: 
        print("\n================= GAME OVER =================")
        print(opponentcharacter.name, "has won the game")
        print("Total rounds survived:", current_round)
        break
    elif current_round == total_rounds:
        print("\n================= GAME OVER =================")
        print(opponentcharacter.name, "has won the game")
        print(opponentcharacter.name, "Thas yet to be defeated")
        break
    
    current_round += 1

print("Thank You for playing my game")