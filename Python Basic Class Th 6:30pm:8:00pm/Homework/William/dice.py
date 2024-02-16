from abc import ABC, abstractmethod
import random

class Dice(ABC):
    @abstractmethod
    def roll(self):
        pass

class SixSidedDice(Dice):
    def roll(self):
        return random.randint(1, 6)

class TenSidedDice(Dice):
    def roll(self):
        return random.randint(1, 10)

class TwentySidedDice(Dice):
    def roll(self):
        return random.randint(1, 20)
