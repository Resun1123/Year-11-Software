# making a fighter class where you can select your fighter
# Make an opponent class which inherits from fighter class and randomises the opponents to fight the player)

import random, time
class Fighter:
    def __init__(self,name,starting_health,weapon_power,shield_defense):
        self.name = name
        self.starting_health = starting_health
        self.weapon_power = weapon_power 
        self. shield_defense = shield_defense
   
    def report(self):
        print(self.name + ' Health:' + str(self.starting_health) + 'Weapon Power:' + str(self.weapon_power) + 'Shield:' + str(self.shield_defense))

    def random_attack(self):
        attack_power = random.randint(int(self.weapon_power/2), int(self.weapon_power*2))
        print('Attack_power:', attack_power)
        return attack_power
    def skill_attack(self, attack_power):# skill is more powerful than normal attack
        attack_power = random.randint(int(self.weapon_power), (int(self.weapon_power*3)))
        target = random.randint(1,5)
        print('Hit enter in exactly',target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 2: 
            multiplier = 0
    def defend(self, attack_power):
        damage = attack_power - self.shield_defense
        if damage > 0:
            self.starting_health -= damage
            print('Damage:', damage)
        else:
            print('No damage taken!')

    def is_dead(self):
        return self.starting_health <= 0

Yukti = Fighter('Yukti', 100, 20, 15)
Jayden = Fighter('Jayden',)
    

