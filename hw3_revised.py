class bankaccount:
    def __init__(self, accountnum, balance):
        self.accountnum=accountnum
        self.balance=50
    def get_balance(self, balance):
        print (self.balance)
    def set_balance(self, balance):
        self.balance=balance
    def withdraw(self, balance):
        a=input('how much to withdraw?')
        self.balance-a
        print (self.balance)

from abc import ABC, abstractmethod
class vehicle(ABC):
    def __init__(self):
        @abstractmethod
        def start_engine(self):
            pass
            
        @abstractmethod
        def stop_engine(self):
            pass
        @abstractmethod
        def drive(self):
            pass

class car(vehicle):

        def start_engine(self):
            print ('starting engine')
        def stop_engine(self):
            print ('engine stopped')
        def drive(self):
            print ('car is now driving')

buggy=car()
buggy.start_engine()
buggy.drive()
buggy.stop_engine()

'''
A real world scenario could be when you drive a motorcycle.
'''

class motorcycle(vehicle):
    def start_engine(self):
        print ('motorcycle goes BRRRMMMMMM')
    def stop_engine(self):
        print ('motorcycle goes SHHHOOooooo...')
    def drive(self):
        print ('motorcycle is now driving')

mc1=motorcycle
mc1.start_engine('')
mc1.drive('')
mc1.stop_engine('')











    
