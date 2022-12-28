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
        self.critchance = 15 

    # Defining the attack method
    def attack(self, opponent):
        randomint1 = random.randint(1,25)
        validint = False
        while validint == False:
            randomint2 = input("Enter a number between 1-25: ").strip()
            try:
                randomint2int = int(randomint2)
                if randomint2int > 26 or randomint2int < 1:
                    validint = False
                else:
                    validint = True
            except:
                validint = False
        if randomint1 == randomint2int:
            self.critchance += randomint2int
            opponent.health -= round((self.attack_power * (self.critchance/100)),2)
            print(str(self.name) , "attacked", str(opponent.name), "for", str(round((self.attack_power * (self.critchance/100)),2)) + "\n")
            critchancecheck(self)
        else:
            if randomint2int > randomint1:
                critchanceaddition = randomint2int - randomint1
            elif randomint1 > randomint2int:
                critchanceaddition = randomint1 - randomint2int
            if (self.critchance-critchanceaddition) > 0:
                opponent.health -= round((self.attack_power * ((self.critchance-critchanceaddition)/100)),2)
                print(str(self.name) , "attacked", str(opponent.name), "for", str(round((self.attack_power * ((self.critchance-critchanceaddition)/100)),2)) + "\n")
            else:
                opponent.health -= round((self.attack_power * ((self.critchance)/100)),2)
                print(str(self.name) , "attacked", str(opponent.name), "for", str(round((self.attack_power * ((self.critchance)/100)),2)) + "\n")
            critchancecheck(self)

    # Defining the heal method
    def heal(self):
        randomint = random.randint(1,25)
        self.health += round(randomint,2)
        print(str(self.name), "healed themselves for", randomint, "HP\n")
    
    # Defining the focus method
    def focus(self):
        randomint1 = random.randint(1,25)
        validint = False
        while validint == False:
            randomint2 = input("Enter a number between 1-25: ").strip()
            try:
                randomint2int = int(randomint2)
                validint = True
            except:
                validint = False
        if randomint1 == randomint2int:
            print(str(self.name), "focused and their critical chance has increased by", randomint1, "%\n")
        else:
            print(str(self.name), "tried to focus but was distracted")
        self.critchance += randomint1
    
    def focusbot(self):
        randomint1 = random.randint(1,25)
        randomint2 = random.randint(1,25)
        if randomint1 == randomint2:
            print(str(self.name), "focused and their critical chance has increased by", randomint1, "%\n")
        else:
            print(str(self.name), "tried to focus but was distracted")
        self.critchance += randomint1
    
    def attackbot(self,opponent):
        randomint1 = random.randint(1,25)
        randomint2 = random.randint(1,25)
        if randomint1 == randomint2:
            self.critchance += randomint2
            opponent.health -= round((self.attack_power * (self.critchance/100)),2)
            print(str(self.name) , "attacked", str(opponent.name), "for", str(round((self.attack_power * (self.critchance/100)),2)) + "\n")
            critchancecheck(self)
        else:
            if randomint2 > randomint1:
                critchanceaddition = randomint2 - randomint1
            elif randomint1 > randomint2:
                critchanceaddition = randomint1 - randomint2
            if (self.critchance-critchanceaddition) > 0:
                opponent.health -= round((self.attack_power * ((self.critchance-critchanceaddition)/100)),2)
                print(str(self.name) , "attacked", str(opponent.name), "for", str(round((self.attack_power * ((self.critchance-critchanceaddition)/100)),2)) + "\n")
            else:
                opponent.health -= round((self.attack_power * ((self.critchance)/100)),2)
                print(str(self.name) , "attacked", str(opponent.name), "for", str(round((self.attack_power * ((self.critchance)/100)),2)) + "\n")
            critchancecheck(self)

# Defining functions  

def herocharacters():
    heroname = input("Enter the Name of Hero: ")
    attackok = False
    while attackok == False:
        heroattack = input("Enter the Attack Damage of Hero (between 5 and 20): ")
        try:
            heroattackint = int(heroattack)
            if heroattackint > 20 or heroattackint < 5:
                print("Hero Attack Damage should be 20 and below")
                attackok = False
            else:
                attackok = True
        except:
            attackok = False
    healthok = False
    while healthok == False:
        herohealth = input("Enter the Health of Hero (between 50 and 150): ")
        try:
            herohealthint = int(herohealth)
            if herohealthint > 150 or herohealthint < 50:
                print("Hero Health should be be above 50 and below 150")
                healthok = False
            else:
                healthok = True
        except:
            healthok = False
    herolist.append(Character(heroname, heroattackint, herohealthint))
    
      
def opponentturn():
    print(str(opponentcharacter.name) + "'s move")
    movenum = random.randint(1,3)
    if movenum == 1:
        opponentcharacter.heal()
    elif movenum == 3:
        opponentcharacter.focusbot()
    else:
        opponentcharacter.attackbot(herocharacter)

def critchancecheck(character):
    if character.critchance > 100:
        character.critchance = character.critchance % 100

def battlestatsandoptions():
    print(str(herocharacter.name), "(YOU) VS", str(opponentcharacter.name))
    print("Battle Statistics")
    print("YOU")
    print("---")
    print("Hero Character:", herocharacter.name) 
    print("Hero Health:", round(herocharacter.health,2)) 
    print("Hero Attack Damage:", round(herocharacter.attack_power,2))
    print("Hero Critical Chance:", herocharacter.critchance)
    print("Total Heros Alive: ",  total_alive_heros)
    print("")
    print("Opponent")
    print("--------")
    print("Opponent Character:", opponentcharacter.name) 
    print("Opponent Health:", round(opponentcharacter.health,2)) 
    print("Opponent Attack Damage:", round(opponentcharacter.attack_power,2))
    print("Total Opponents Alive: ",  total_opponent_left)
    print("---------------------------")
    print("1. Attack\t\t2. Heal")
    print("3. Focus\t\t0. Exit Game\n")

def useroption():
    optionok = False
    while optionok == False:
        userinput = input("Enter option: ").strip()
        match userinput:
            case '1':
                herocharacter.attack(opponentcharacter)
                opponentturn()
                input("Press Enter to continue...")
                optionok = True

            case '2':
                herocharacter.heal()
                opponentturn()
                input("Press Enter to continue...")
                optionok = True
            
            case '3':
                herocharacter.focus()
                opponentturn()
                input("Press Enter to continue...")
                optionok = True

            case '0':
                print("Thank You for playing my game")
                optionok = True
                exit()
            
            case _:
                print("Invalid option\n")
                optionok = False
                continue
            


# Initiating Lists and defining variables

herolist = []
opponentlist = [Character("Lightning Mcqueen", 15, 10), Character("Doc Hudson", 20, 10)]
opponentlistdup = opponentlist.copy()

current_round = 1
total_alive_heros = 3
total_opponent_left = len(opponentlist)
i = 1

###################################################################################################################
#-----------------------------------------------------------------------------------------------------------------#
###################################################################################################################

# Prompting user for character
# create your heroes using the following format Hero("Name of Hero", Attack Power, Health Points)
while i < 3:
    herocharacters()
    i += 1
    print()

herolistdup = herolist.copy()

if len(herolistdup) == len(herolist):
    herocharacter = herolist[0]

if len(opponentlistdup) == len(opponentlist):
    opponentcharacter = opponentlist[0]

while total_alive_heros > 1:

    total_alive_heros = len(herolistdup)
    total_opponent_left = len(opponentlistdup)

    print("Round", current_round, ":\n")
    battlestatsandoptions()
    useroption()
    if opponentcharacter.health <= 0 and total_opponent_left >= 1:
        opponentlistdup.remove(opponentcharacter)
        print("Opponent Defeated")
        input("Press any key to continue")
        opponentcharacter = opponentlistdup[0]

    elif herocharacter.health <= 0 and total_alive_heros >= 1: 
        herolistdup.remove(herocharacter)
        print("Hero Defeated")
        input("Press any key to continue")
        herocharacter = herolistdup[0]

    if opponentcharacter.health <= 0 and total_opponent_left < 1:
        print("\n============== CONGRATULATIONS ==============")
        print("You have won the game")
        print("Total rounds played:", current_round)
        print("Total heros left:", total_alive_heros)
        break
    elif herocharacter.health <= 0 and total_alive_heros < 1: 
        print("\n================= GAME OVER =================")
        print("Nice Try")
        print("Total rounds survived:", current_round)
        print("Total opponents left:", total_opponent_left)
        break
    current_round += 1

