#Create a defend method that helps you repel an attack
#Create a loop which simulates a fight and declares a winner
#Test the game 
#Comment your code appropriately





import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self):
        print (f'Player name: {self.name} - Health: {self.health} - Weapon: {self.weapon} - Shield: {self.shield}')
# defining the report method to show the player details
    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))
        print('Attack Power:', attack_power)
        return attack_power
# Defining a random method to generate random attack power  
    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage < 0:
            damage = 0 
            self.health -= damage
            print(f'{self.name} blocked the attack!')
        else:
            self.health -= damage
            print(f'{self.name} block failed! \n Took', damage, 'damage!)')
        print(f'{self.name} health is now:', self.health)
        if self.health <= 0:
            print(f'{self.name} has been defeated!')
            return True
        return False
# Defining the defend method to block the attack and reduce the health of the player
You = Fighter('You', 100, 60, 20)
Jayden = Fighter('Jayden', 200, 15, 10)
You.report()
Jayden.report()

while True:

    print('You are fighting jayden!')
    Jayden.defend(You.random_attack())
    Jayden.report()
    time.sleep(2)
    print('')
    if Jayden.health <= 0:
        print('You have defeated Jayden!')
        break
    You.defend(Jayden.random_attack())
    You.report()
    time.sleep(2)
    if You.health <= 0:
        print('You have been defeated!')
        break
# while loop to keep the game running until one of the players is defeated


