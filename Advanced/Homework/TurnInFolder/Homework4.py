
#Problem 1
class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def info(self):
        print(f"Computer Info: CPU: {self.cpu}, Ram: {self.ram}, Storage: {self.storage}")
class Monitor:
    def __init__(self, size, resolution):
        self.size = size
        self.resolution = resolution

    def info(self):
        print(f"Monitor Info: Size: {size} in., Resolution: {resolution}")
class Desktop:
    def __init__(self, computer, monitor):
        self.computer = computer
        self.monitor = monitor

    def info(self):
        print(f"Desktop Relationship:")
        self.computer.info()
        self.monitor.info()

computer_info = Computer(cpu = "ABC", ram = 3, storage = 333)
monitor_info = Monitor(size = 33, resolution = 3333)
Desktop_info = Desktop(computer = computer_info, monitor = monitor_info)

Desktop_info.info()

#Problem 2
class Backpack:
    def __init__(self, color, space, size):
        self.color = cpu
        self.space = ram
        self.size = storage

    def info(self):
        print(f"Backpack Info: Color: {self.color}, Space: {self.space}, Size: {self.size}")
class Purse:
    def __init__(self, material, brand):
        self.material = material
        self.brand = brand

    def info(self):
        print(f"Purse Info: Material: {self.material}, brand : {self.brand}")
class Bag:
    def __init__(self, backpack, purse):
        self.backpack = backpack
        self.purse = purse

    def info(self):
        print(f"Types of Bags:")
        self.backpack.info()
        self.purse.info()

backpack_info = Backpack(color = "blue", space = "large area" , size= "8x8")
purse_info = Purse(material = "leather", brand = "Gucci")
Bag_info = Bag(backpack = backpack_info, purse = purse_info)

Bag_info.info()
