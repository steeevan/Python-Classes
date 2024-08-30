class computer:
    def __init__(self, cpu, ram, storage):
        self.cpu=cpu
        self.ram=ram
        self.storage=storage

class monitor(computer, size, resolution):
    def print_info1self(self, size, resolution):
        self.size=size
        self.resolution=resolution
        print (self.size, self.resolution)
        

class desktop(computer):
    def print_info(self):
        print (self.cpu, self.ram, self.storage)

'''
the scenario would be when I am playing on a pc.

'''
class PC(computer):
    def start_comp(self):
        print ('starting computer')
    def close_comp(self):
        print ('closing computer')

windows=PC()
windows.start_comp('')
windows.close_comp('')
