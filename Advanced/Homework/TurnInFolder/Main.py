class Computer:
    def __init__(cpu,ram,storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

class Monitor:
    def __init__(size,resolution):
        self.size = size
        self.resolution = resolution

'''
If you want to build a mouse, you need a blueprint. You can build a similar
mouse, but you have the use the blueprint.
'''
class Mouse:
    def __init__(size,rgb,sensitivity):
        self.size = size
        self.rgb = rgb
        self.sensitivity = sensitivity
        
