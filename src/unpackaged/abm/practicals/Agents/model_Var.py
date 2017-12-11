# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:06:40 2017

@author: amandaf
"""

import random
import operator
import matplotlib.pyplot
import agentframework_variables

#a = agentframework.Agent()
#print (a.y, a.x)
#a.move()
#print (a.y, a.x)
def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework_variables.Agent())
    print (agents[i].x)
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)