from abc import ABC, abstractmethod
import random

class Dice(ABC):

    @abstractmethod
    def roll(self):
        pass

class SixDice(Dice):
    def roll(self):
        return random.randint(1,6)

class TenDice(Dice):
    def roll(self):
        return random.randint(1,10)

class TwentyDice(Dice):
    def roll(self):
        return random.randint(1,20)


myDice = SixDice()
print(myDice.roll())
