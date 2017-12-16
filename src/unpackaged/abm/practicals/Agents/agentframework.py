# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:10:18 2017

@author: amandaf
"""

import random
class Agent():
    def __init__ (self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
    
   #Move the sheep around 1 step at a time
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100