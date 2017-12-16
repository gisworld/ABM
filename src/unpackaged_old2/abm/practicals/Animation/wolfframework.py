# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08

@author: amandaf
"""
 
import random
class Wolf():
    def __init__ (self, environment,agents, maxE, deadsheep):
        self.environment = environment
        self.maxE = maxE
        self.agents = agents
        self.deadsheep = deadsheep
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

    x = property(get_x, set_x, "Wolf's X coordinate")    
    
	
    def get_y(self):
        return self._y
	
    def set_y(self, value):
        if value == None:
            self._y = random.randint(0,self.maxE-1)
        else:
            self._y = value

    y = property(get_y, set_y, "Wolf's Y coordinate") 
    
    # Display positional information about Agent
    def __str__ (self):
        return "Wolf X,Y: " +str(self.get_x()) + ", "+str(self.get_y()) + ". Store:" + str(self.store)

    def move(self):
        if random.random() < 0.5:
            self.set_x((self._x + 1) % self.maxE)
        else:
            self.set_x((self._x - 1) % self.maxE)

        if random.random() < 0.5:
            self.set_y((self._y + 1) % self.maxE)
        else:
            self.set_y((self._y - 1) % self.maxE)  
  

    def eat_neighbouring_sheep(self, neighbourhood):
        #print (neighbourhood)
        # Loop through the agents in self.agents .
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(agent) 
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Sum self.store and agent.store .
                self.agents.remove(agent)
                self.deadsheep.append(agent)
                self.set_x(agent.x)
                self.set_y(agent.y)
                #wolf can only eat one sheep at a time
                break
                               
            # End if
        # End loop
    
    def distance_between(self, agent):
        return (((self.get_x() - agent.x)**2) + ((self.get_y() - agent.y)**2))**0.5