# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:25:05 2017

@author: amandaf
"""

import matplotlib.pyplot
import csv
import agentframework

def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []
#Empty environmental list
environment = []
#Read the file
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#Loop through file
for row in reader:	# A list of rows
    #create new rowlist
    rowlist = []	
    for value in row:	# A list of value
        rowlist.append(value)
    #Add rowlist to environment
    environment.append(rowlist)
f.close() 
#Calculate size of environment
maxEnv = len(environment)
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, maxEnv))
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        #Agent eats values
        agents[i].eat()
        print("Eating")
        if agents[i].store > 100:
            #Greedy agents are sick if they eat more than 100 units
            agents[i].sick()
            print ("Being sick")
#Write out environment to file
f2 = open('environment.txt','w', newline='')
writer = csv.writer(f2)
for row in environment:
    writer.writerow(row)
f2.close()
#Write store count to file
f2 = open('store.txt','a')
for i in range(num_of_agents):
    f2.write(str(agents[i].store)+"\n")
f2.close()

matplotlib.pyplot.xlim(0, maxEnv-1)
matplotlib.pyplot.ylim(0, maxEnv-1)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)