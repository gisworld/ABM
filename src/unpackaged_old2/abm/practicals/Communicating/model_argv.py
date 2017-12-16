# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:25:05 2017

@author: amandaf
"""

import matplotlib.pyplot
import csv
import random
import agentframework
import argparse

parser = argparse.ArgumentParser(description='Define Agent parameters')
#num_of_agents = 10
parser.add_argument('num_of_agents', type=int,
                    help='Number of agents')
parser.add_argument('num_of_iterations', type=int,
                    help='Number of iterations')
#num_of_iterations = 100
agents = []
#Create size of neighbourhood
#neighbourhood = 20
parser.add_argument('neighbourhood',  type=int, 
                    help='Size of neighbourhood')

args = parser.parse_args()
num_of_agents = args.num_of_agents
num_of_iterations = args.num_of_iterations
neighbourhood = args.neighbourhood
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
    agents.append(agentframework.Agent(environment, agents, maxEnv))
# Move the agents.
random.shuffle(agents)
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        #Agent eats values
        agents[i].eat()
        #Agent shares with neighbours
        agents[i].share_with_neighbours(neighbourhood)
        if agents[i].store > 100:
            #Greedy agents are sick if they eat more than 100 units
            agents[i].sick()
            
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
