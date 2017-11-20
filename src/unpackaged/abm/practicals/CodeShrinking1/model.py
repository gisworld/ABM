# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:29:53 2017

@author: amandaf
"""
import random, operator, matplotlib.pyplot
agents = []
# Set up random position in grid 100x100.
agents.append([random.randint(0,99),random.randint(0,99)])
print (agents)
# Random walk one step.
if random.random() <0.5:
    agents[0][0] += 1 
else:
    agents[0][0]-= 1

if random.random() <0.5:
    agents[0][1] += 1 
else:
    agents[0][1]  -= 1

if random.random() <0.5:
    agents[0][0]  += 1 
else:
    agents[0][0]  -= 1

if random.random() <0.5:
    agents[0][1]  += 1 
else:
    agents[0][1]  -= 1


# Set up random position in grid 100x100.
agents.append([random.randint(0,99),random.randint(0,99)])
# Random walk one step.
if random.random() <0.5:
    agents[1][0]  += 1 
else:
    agents[1][0] -= 1

if random.random() <0.5:
    agents[1][1]  += 1 
else:
    agents[1][1]  -= 1

if random.random() <0.5:
    agents[1][0]  += 1 
else:
    agents[1][0] -= 1

if random.random() <0.5:
    agents[1][1]  += 1 
else:
    agents[1][1]  -= 1
print (agents)
distance = ((agents[0][0]-agents[1][0])**2 + (agents[0][1]-agents[1][1])**2)**0.5
print (distance)
print (max(agents, key=operator.itemgetter(1)))
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='red') 
matplotlib.pyplot.show()
