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
        self.x = self.set_x(self)
        self.y = self.set_y(self)
        #self.x = random.randint(0,maxE)
        #self.y = random.randint(0,maxE)
        self.store = 0
    
    def get_x(self):
        return self._x
	
    def set_x(self, value):
        if value == None:
            self._x = random.randint(0,self.maxE-1)
        else:
            self._x = value

    x = property(get_x, set_x, "Agent's X coordinate")    
    
	
    def get_y(self):
        return self._y
	
    def set_y(self, value):
        if value == None:
            self._y = random.randint(0,self.maxE-1)
        else:
            self._y = value

    y = property(get_y, set_y, "Agent's Y coordinate") 
    
    # Display positional information about Agent
    def __str__ (self):
        return "Agent X,Y: " +str(self.get_x()) + ", "+str(self.get_y()) + ". Store:" + str(self.store)

    #Move the sheep around 1 step at a time
    def move(self):
        if random.random() < 0.5:
            self.set_x((self._x + 1) % self.maxE)
        else:
            self.set_x((self._x - 1) % self.maxE)

        if random.random() < 0.5:
            self.set_y((self._y + 1) % self.maxE)
        else:
            self.set_y((self._y - 1) % self.maxE)  
#    def move(self):
#        if random.random() < 0.5:
#            self.x = (self.x + 1) % self.maxE
#        else:
#            self.x = (self.x - 1) % self.maxE
#
#        if random.random() < 0.5:
#            self.y = (self.y + 1) % self.maxE
#        else:
#            self.y = (self.y - 1) % self.maxE      
    
    #Eat 10 units of grass
    def eat(self):
        if self.environment[self.get_y()][self.get_x()] > 10:
            self.environment[self.get_y()][self.get_x()] -= 10
            self.store += 10
        else:
            self.environment[self.get_y()][self.get_x()] = 0
#    def eat(self):
#        if self.environment[self.y][self.x] > 10:
#            self.environment[self.y][self.x] -= 10
#            self.store += 10
#        else:
#            self.environment[self.y][self.x] = 0
    
    #Greedy sheep will be sick if they exceed the defined amount      
    def sick(self):
        self.environment[self.get_y()][self.get_x()] += self.store
        self.store = 0 