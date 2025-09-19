#Make health private (it becomes __health)
#Use methods to check if the fighter object is dead
#Comment your code appropriately
#Copy your completed code here:






import random, time 

class Fighter:
    def __init__(self,name, starting__health, weapon, shield):
        self.name = name
        self.__health = starting__health #health becomes private
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))


    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), (int(self.weapon*2)))
        print('Attack power:', attack_power)
        return attack_power

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')
    
    def is_dead(self):
        return self.__health <= 0 


you = Fighter('You',100,60,20)
troll = Fighter('Troll',200,30,10)


you.report()
troll.report()
while True:
    print('You are fighting a troll!')
    troll.defend(you.random_attack())
    troll.report()
    time.sleep(2)
    print('')
    troll.random_attack()
    you.defend(troll.random_attack())
    you.report()
    time.sleep(2)
    print('')
    if troll.is_dead():
        print('You have defeated the troll!!')
    if you.is_dead():
        print('YOu have been defeated!')
        break
    if you.is_dead() or troll.is_dead():
        print('Game Over!')
        break
# End of the code

