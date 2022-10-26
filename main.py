# Pseudo Code
'''
Some game with many rounds
Each round a user can choose to attack or heal
The user will need to kill the boss by the end of the set rounds 
'''

# Importing of Packages

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
            opponent.health -= self.attack_power
            print(self.name , "attacked", opponent.name, "for", self.attack_power)

    # Defining the heal method
    def heal(self):
        # insert code here on how to heal hero
        # using math.random function heal the hero between 15-20 health
        # Code Below Here
        randomint = random.randint(50,150)
        self.health += randomint
        print(self.name, "healed themselves for", randomint, "HP")
        

###################################################################################################################
#-----------------------------------------------------------------------------------------------------------------#
###################################################################################################################
'''
# Teaching OOP calling
character = Character("Lightning Mcqueen", 15, 200)
print(character.name)
'''

# Code Below Here
herolist = [Character("Michael Schumacher", 10, 300), Character("Ramone", 30, 100)] # create your heroes using the following format Hero("Name of Hero", Attack Power, Health Points)
opponentlist = [Character("Lightning Mcqueen", 15, 200), Character("Doc Hudson", 20, 150)]

# using python length and random library
herolist_length = len(herolist)
opponentlist_length = len(opponentlist)
randomheroindex = random.randint(0,herolist_length)
randomopponentindex = random.randint(0,opponentlist_length)

herocharacter = herolist[randomheroindex]
opponentcharacter = opponentlist[randomopponentindex]

total_rounds = 16
current_round = 1

###################################################################################################################
#-----------------------------------------------------------------------------------------------------------------#
###################################################################################################################

def opponentturn():
    if opponentcharacter.health <= 50:
        opponentcharacter.heal()
    else:
        opponentcharacter.attack(herocharacter)

###################################################################################################################
#-----------------------------------------------------------------------------------------------------------------#
###################################################################################################################

while current_round < total_rounds + 1:
    print("Round", current_round, ":")
    print("\n\n---------------------------")
    print("1. Attack\t\t2. Heal")
    print("3. Exit Game\n")
    userinput = input("Enter option: ")
    if userinput == "1":
        herocharacter.attack(opponentcharacter)
        opponentturn()
    elif userinput == "2":
        herocharacter.heal()
        opponentturn()
    elif userinput == "3":
        break
    else:
        print("Invalid option")
        continue
    if opponentcharacter.health <= 0:
        print("==================GAME OVER==================")
        print(herocharacter, "has won the game")
        print("Total rounds survived:", current_round)
    elif herocharacter.health <= 0: 
        print("==================GAME OVER==================")
        print(opponentcharacter, "has won the game")
        print("Total rounds survived:", current_round)
    elif current_round == total_rounds:
        print("==================GAME OVER==================")
        print(opponentcharacter, "has won the game")
        print(opponentcharacter, "Thas yet to be defeated")
    
    current_round += 1

print("Thank You for playing my game")