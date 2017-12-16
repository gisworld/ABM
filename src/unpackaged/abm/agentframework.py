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
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
