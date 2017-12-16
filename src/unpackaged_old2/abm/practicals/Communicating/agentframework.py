# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:10:18 2017

@author: amandaf
"""
#This doesn't work 
import random
class Agent():
    def __init__ (self, environment,agents, maxE):
        self.environment = environment
        self.agents = agents
        self.maxE = maxE
        self.x = self.set_x(self)
        self.y = self.set_y(self)
        self.store = 0
    
    # Display positional information about Agent
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

    def move(self):
        if random.random() < 0.5:
            self.set_x((self._x + 1) % self.maxE)
        else:
            self.set_x((self._x - 1) % self.maxE)

        if random.random() < 0.5:
            self.set_y((self._y + 1) % self.maxE)
        else:
            self.set_y((self._y - 1) % self.maxE)  

    def eat(self):
        if self.environment[self.get_y()][self.get_x()] > 10:
            self.environment[self.get_y()][self.get_x()] -= 10
            self.store += 10
        else:
            self.environment[self.get_y()][self.get_x()] = 0
        
    def sick(self):
        self.environment[self.get_y()][self.get_x()] += self.store
        self.store = 0 
        
    def share_with_neighbours(self, neighbourhood):
        #print (neighbourhood)
        # Loop through the agents in self.agents .
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(agent) 
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Sum self.store and agent.store .
                sum = self.store + agent.store
                # Divide sum by two to calculate average.
                average = sum/2
                self.store = average
                agent.store = average
                print("sharing " + str(distance) + " " + str(average))
            # End if
        # End loop
    
    def distance_between(self, agent):
        return (((self.get_x() - agent.x)**2) + ((self.get_y() - agent.y)**2))**0.5
