# Pseudo Code
'''
Some game with many rounds
Each round a user can choose to attack or heal
The user will need to kill the boss by the end of the set rounds 
'''

# OOP Portion

class Hero:
    
    # Defining Hero name, attack power and health
    def __init__(self, given_name, given_attack_power, given_health):
        self.name = given_name
        self.attack_power = given_attack_power
        self.health = given_health

    herolist = []
    opponentlist = []

    # Defining the attack method
    def attack(self, attacker, attack_power, opponent, opponent_health):
            opponent_health -= attack_power
            
            print(attacker , "attacked", opponent, "for", attack_power)

    # Defining the heal method
    def heal(self, health):
        # insert code here on how to heal hero
        # using math.random function heal the hero between 15-20 health

