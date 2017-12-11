# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:29:53 2017

@author: amandaf
"""
import random, operator, matplotlib.pyplot
agents = []
num_of_agents = 10
num_of_iterations = 100
# Set up random position in grid 100x100.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
print (agents)
# Move agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):
	# Torus method
        if random.random() <0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0]= (agents[i][0] - 1) % 100
        if random.random() <0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
east = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(east[1],east[0], color='red')
matplotlib.pyplot.show()
