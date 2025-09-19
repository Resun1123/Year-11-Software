#Create a loop which simulates a fight and declares a winner
#Test the game 
#Implement the game with a private __health attribute
#Comment your code appropriately

import random

class Fighter:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        damage = random.randint(10,self.attack_power)
        opponent.health -= damage
        print(f'{self.name} attacks {opponent.name} for {damage} damage! {opponent.name} has {opponent.health} health left.')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')
            return True
        return False
    def is_alive(self):
        return self.health > 0
    def __str__(self):
        return f'{self.name} - Health: {self.health}, Attack Power: {self.attack_power}'

class FighterGame:
    def __init__(self):
        self.fighter1 = None
        self.fighter2 = None
        self.rounds = 0
        self.winner = None
    def create_fighter(self,name, health, attack_power):
        return Fighter(name, health, attack_power)
    def start_game(self):
        print('Welcome to the fighter game!')
        self.fighter1 = self.create_fighter('Yukti', 100, 20)
        self.fighter2 = self.create_fighter('Jayden', 100, 15)
        print(f'Fighter 1: {self.fighter1}')
        print(f'Fighter 2: {self.fighter2}')
        print('Let the fight begin!')
    
    def fight(self):
        while self.fighter1.is_alive() and self.fighter2.is_alive():
            self.rounds += 1
            print(f'round {self.rounds}')
            if self.fighter1.attack(self.fighter2):
                self.winner = self.fighter1
                break
            if self.fighter2.attack(self.fighter1):
                self.winner = self.fighter2
                break
        if self.winner:
            print(f'{self.winner.name} is the winner of the fight!')
        else: 
            print('The fight ended in a draw!')
    def play(self):
        self.start_game()
        self.fight()
        print('Game Over! Thanks for playing!')
if __name__ == '__main__':
    game = FighterGame()
    game.play()
# The code above is a simple fighter game where two fighters can attack each other until one of them is defeated.
# The game uses a random number generator to determine the damage dealt in each attack.
# The game continues until one of the fighters' health reaches zero or below.
# The game also keeps track of the number of rounds fought and announces the winner at the end.
# The game is played in a loop, so thst multiple rounds of fighting happens until a winner is declared.


    
