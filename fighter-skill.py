#Create a skill attack method
#Use the time library to set up a timing measure (skill factor)
#Have the skill increase or decrease the final attack value
#Comment your code appropriately




import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

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
        print('Hit Enter in exactly', target, 'second')
        start_time = time.time()
        input()
        end_time = time.time()
        elapsed_time = end_time - start_time
        multiplier = 3 - abs(target - elapsed_time)
        if multiplier < 2:
            multiplier = 0




        print('Attackpower:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')


         # Random skill factor between 0.5 and 1.5



you = Fighter('You',100,60,20)
troll = Fighter('Troll',300,30,10)

you.report()
troll.report()
print('You are fighting a troll!')
while True:
    troll.defend(you.skill_attack())
    troll.report()
    time.sleep(2)
    print('')
    
    troll.report()
    
    if troll.is_dead():
        print('You have defeated the troll!!')
        break
    
    you.defend(troll.random_attack())
    you.report()
    print('')
    
    if you.is_dead():
        print('You have been defeated!')
        break
    
    time.sleep(2)