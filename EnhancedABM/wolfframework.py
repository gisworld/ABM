# -*- coding: utf-8 -*-
"""
Updated 16 Dec 2017
Framework for a Wolf
Wolves move one step at a time, unless a sheep is nearby
If sheep is within the defined Run (neighbourhood) range, the wolf can eat the sheep

@author: Amanda Forbes
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
        self.store = 0
    
    #Set up X property
    def get_x(self):
        return self._x
	
    def set_x(self, value):
        if value == None:
            self._x = random.randint(0,self.maxE-1)
        else:
            self._x = value

    x = property(get_x, set_x, "Wolf's X coordinate")    
    
	#Set up Y property
    def get_y(self):
        return self._y
	
    def set_y(self, value):
        if value == None:
            self._y = random.randint(0,self.maxE-1)
        else:
            self._y = value

    y = property(get_y, set_y, "Wolf's Y coordinate") 
    
    # Display positional information about Wolf
    def __str__ (self):
        return "Wolf X,Y: " +str(self.get_x()) + ", "+str(self.get_y()) + ". Store:" + str(self.store)

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
  
    #Eat nearby sheep
    def eat_neighbouring_sheep(self, neighbourhood):
        # Loop through the agents in self.agents .
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(agent) 
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Remove sheep from list
                self.agents.remove(agent)
                #Add dead sheep to list
                self.deadsheep.append(agent)
                #Set new position to dead sheep's
                self.set_x(agent.x)
                self.set_y(agent.y)
                #wolf can only eat one sheep at a time
                break
            # End if
        # End loop

#Calculate distance between agents    
    def distance_between(self, agent):
        return (((self.get_x() - agent.x)**2) + ((self.get_y() - agent.y)**2))**0.5