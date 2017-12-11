
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:10:18 2017

@author: amandaf
"""

import random
class Agent():
    def __init__ (self):
        self.x = self.set_x(self)
        self.y = self.set_y(self)
    
    def get_x(self):
        return self._x
	
    def set_x(self, value):
        if value == None:
            self._x = random.randint(0,99)
        else:
            self._x = value

    x = property(get_x, set_x, "Agent's X coordinate")    
    
	
    def get_y(self):
        return self._y
	
    def set_y(self, value):
        self._y = random.randint(0,99)

    y = property(get_y, set_y, "Agent's Y coordinate") 
    
#    def move(self):
#        if random.random() < 0.5:
#            self.x = (self.x + 1) % 100
#        else:
#            self.x = (self.x - 1) % 100
#
#        if random.random() < 0.5:
#            self.y = (self.y + 1) % 100
#        else:
#            self.y = (self.y - 1) % 100
    def move(self):
        if random.random() < 0.5:
            self.set_x((self._x + 1) % 100)
        else:
            self.set_x((self._x - 1) % 100)

        if random.random() < 0.5:
            self.set_y((self._y + 1) % 100)
        else:
            self.set_y((self._y - 1) % 100)