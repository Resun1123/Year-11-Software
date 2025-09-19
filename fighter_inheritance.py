#Create a Wizard class which inherits from a fighter
#Add a magic attribute 
#Modify the random attack method to include magic
#Comment your code appropriately



import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+','+ ' Health: '+ str(self.__health))

    def is_dead(self):
        if self.__health <= 0:
            return True 
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), (int(self.weapon*2)))
        print('Attack power:', attack_power)
        return attack_power

    def skill_attack(self):
        attack_power = random.randint(int(self.weapon/2), (int(self.weapon*2)))
        target = random.randint(2,6)
        print('Hit enter in exactly',target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 2: 
            multiplier = 0

        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')

class Wizard(Fighter): # Inherits from Fighter class
    def __init__(self,name, starting_health, weapon, shield, magic):
        super().__init__(name,starting_health, weapon, shield)
        self.magic = magic 

    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), (int(self.weapon*2)))
        print('Attack power:', attack_power)
        return attack_power + self.magic
    
you = Fighter('You', 100,60,20)
wiz = Wizard('Wizard', 300,50,10,30)

you.report()
wiz.report()

while True:
    print('You are fighting a', wiz.name)
    wiz.defend(you.skill_attack())
    wiz.report()
    time.sleep(2)
    print('')
    if wiz.is_dead():
        print('YOu have defeated the', wiz.name)
        break
    you.defend(wiz.random_attack())
    you.report()
    time.sleep(2)
    if you.is_dead():
        print('You have been defeated!')
        break
    if you.is_dead() or wiz.is_dead():
        print('Game Over!')
        break
# The Wizard class inherits from the Fighter class and adds a magic attribute.
# The random_attack method in the Wizard class includes the magic attribute to increase the attack power.

