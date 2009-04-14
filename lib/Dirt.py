from Constants import *
from Object import *

class Dirt(Object):
    def __init__(self, col, row):
        Object.__init__(self, col, row, 'd')
        self.health = 3

    def decrementHealth(self):
        self.health -= 1
        if self.health <= 0:
            self.die()

    def die(self):
        ''' When the Dirt object dies, it becomes an empty space.'''
        self.setType('.')
