
#question1
class computer:
    def __init__(self,cpu,ram,storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def print_info(self):
        print(f"cpu: {self.cpu} , ram: {self.ram} , storage: {self.storage}")

class monitor:
    def __init__(self,size,resolution):
        self.size = size
        self.resolution = resolution

    def print_info(self):
        print(f"size: {self.size} , resolution: {self.resolution}")

        
class desktop:
    def __init__(self,computer,monitor):
        self.computer = computer
        self.monitor = monitor

    def print_info(self):
        self.computer.print_info()
        self.monitor.print_info()

computer1 = computer("Intel I7","160 GB","1T GB")
monitor1 = monitor("36in","1,920 x 1,080")
desktop1 = desktop(computer1,monitor1)
desktop1.print_info()

#question2
class plane:
    def __init__(self,wing,body):
        self.wing = wing
        self.body = body

    def print_info(self):
        print(f"plane wing: {self.wing} ,plane body: {self.body}")

class tank:
    def __init__(self,turrent,tracks):
        self.turrent = turrent
        self.tracks = tracks

    def print_info(self):
        print(f"tank turrent: {self.turrent} ,tank tracks: {self.tracks}")

        
class army:
    def __init__(self,plane,tank):
        self.plane = plane
        self.tank = tank

    def print_info(self):
        self.plane.print_info()
        self.tank.print_info()

plane1 = plane("60ft","100ft")
tank1 = tank("3in","10ft")
army1 = army(plane1,tank1)
army1.print_info()
