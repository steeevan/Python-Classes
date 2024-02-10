import random

'''
Class Implementation
Name: Dice
Description: This class will be a blueprint
            to roll a dice given the # of sides.
Input:
    + sides: This parameters takes in an integer, n
Output:

'''
class Dice:
    def __init__(self,sides):
        '''
            Constructors
        '''
        self.sides = sides

    def roll(self):
        '''
        Name: roll
        Description: This function when invoked will generate
                    a random number between 1 to n, given the # of sides.
        Input:
        Output:
            + returns a random integer [1,n]
        '''
        return random.randint(1,self.sides)

'''
Class Implementation
Name: Player
Description: THis is a blueprint for our player which will keep track of its own atrributes.
            It is also able to attack, roll dice, and much more.
Input:
    + name : String type , the name of player
    + health: Int type, sets the players health
    + damage: Int type, sets the amount of damge it gives
    + attack: Int type, the number of times it could hit
Output:

Local attributes:
    + wins: List type , keeps track of the dice that won
    + loses: List type, keeps track of the dice that lost
'''
class Player:
    def __init__(self,name,health,damage,attack):
        self.name = name
        self.health = health
        self.damage = damage
        self.attack = attack
        self.wins = []
        self.loses = []

    def roll_dice(self,dice):
        result = dice.roll()

    def take_damage(self,damage):
        self.health -= damage
        print(f"Player took damage! Health: {self.health}")
        if self.health <= 0:
            print("Player has been defeated!")
            print("Enemy wins")

    def attack_enemy(self,enemy):
        damage_deal = self.damage
        enemy.take_damage(damage_deal)

    def won_roll(self,rolled_dice):
        self.wins.append(rolled_dice)
        
    def lose_roll(self,rolled_dice):
        self.loses.append(rolled_dice)

class Enemy:
    def __init__(self,name,health,damage,attack):
        self.name = name
        self.health = health
        self.damage = damage
        self.attack = attack
        self.wins = []
        self.loses = []

    def roll_dice(self,dice):
        result = dice.roll()

    def take_damage(self,damage):
        self.health -= damage
        print(f"Enemy took damage! Health: {self.health}")
        if self.health <= 0:
            print("Enemey has been defeated!")
            print("Player wins")

    def attack_player(self,player):
        damage_deal = self.damage
        player.take_damage(damage_deal)

    def won_roll(self,rolled_dice):
        self.wins.append(rolled_dice)
        
    def lose_roll(self,rolled_dice):
        self.loses.append(rolled_dice)

if __name__ == "__main__":
    
    myDice = Dice(6)
    print(myDice.roll())

    player1 = Player("Wizard",100,20,5)
    enemy1 = Enemy("Orc",100,20,5)

    for i in range(10):
        
        d = myDice.roll()
        if d < 4:
            player1.attack_enemy(enemy1)
            player1.won_roll(d)
            enemy1.lose_roll(d)
        else:
            enemy1.attack_player(player1)
            player1.lose_roll(d)
            enemy1.won_roll(d)

    print(f"Players wins {len(player1.wins)} : {player1.wins}")
    print(f"Players loses {len(player1.loses)} : {player1.loses}")

    print(f"Enemy wins {len(enemy1.wins)} : {enemy1.wins}")
    print(f"Enemy loses {len(enemy1.loses)} : {enemy1.loses}")
