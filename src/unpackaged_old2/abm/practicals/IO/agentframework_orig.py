# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:10:18 2017

@author: amandaf
"""

import random
class Agent():
    def __init__ (self, environment, maxE):
        self.environment = environment
        self.maxE = maxE
        self.x = random.randint(0,maxE)
        self.y = random.randint(0,maxE)
        self.store = 0
    
    # Display positional information about Agent
    def __str__ (self):
        return "Agent X,Y: " +str(self.x) + ", "+str(self.y) + ". Store:" + str(self.store)
    
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % self.maxE
        else:
            self.x = (self.x - 1) % self.maxE

        if random.random() < 0.5:
            self.y = (self.y + 1) % self.maxE
        else:
            self.y = (self.y - 1) % self.maxE      

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.environment[self.y][self.x] = 0
        
    def sick(self):
        self.environment[self.y][self.x] += self.store
        self.store = 0 