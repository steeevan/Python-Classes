class computer:
  def __init__(self, cpu, ram, storage):
    
    self.cpu='i3'
    self.ram='16 gb'
    self.storage='64 gb'

class monitor:
  def __init__(self, size, resolution):
    
    self.size='23.8'
    self.resolution='1920x1080'

class desktop:
  def __init__(self):
    desktop=computer+moniter

'''
in a real world scenario, computer would be the class,
moniter would be a component, and desktop would also be a
component.
'''

#code above



