
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:10:18 2017

@author: amandaf
"""
#This doesn't work 
import random
class Agent():
    def __init__ (self):
        self.x = None
        self.y = None
    
    def get_x(self):
        return self._x
    def set_x(self):
        self._x = random.randint(0,99)
    def del_x(self):
        del self._x
    x = property(get_x, set_x, del_x)    
    
    def get_y(self):
        return self._y
    def set_y(self):
        self._y = random.randint(0,99)
    def del_y(self):
        del self._y 
    y = property(get_y, set_y, del_y) 
    
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100