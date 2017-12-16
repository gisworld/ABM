# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:25:05 2017

@author: amandaf
"""

import matplotlib.pyplot
import matplotlib.animation
import csv
import agentframework
import wolfframework

#set up variables 
num_of_agents = 10
num_of_iterations = 100
num_of_wolves = 2
wolves =[]
agents = []
deadsheep=[]
neighbourhood = 10
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
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
carry_on = True
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, maxEnv))
#create wolves
for i in range(num_of_wolves):
    wolves.append(wolfframework.Wolf(environment,agents, maxEnv, deadsheep))
# Move the agents.
def update(frame_number):
    fig.clear()
    matplotlib.pyplot.xlim(0, maxEnv-1)
    matplotlib.pyplot.ylim(0, maxEnv-1)
    matplotlib.pyplot.imshow(environment)
    for j in range(num_of_iterations):
        for i in range(len(agents)):           
            agents[i].move()
            #Agent eats values
            agents[i].eat()
            #print("Eating")
            if agents[i].store > 100:
                #Greedy agents are sick if they eat more than 100 units
                agents[i].sick()
                #print ("Being sick")
        for k in range(num_of_wolves):
            #print(wolves[0].x,wolves[0].y)
            wolves[k].move()
            #wolves eat sheep if they are within neighbourhood distance
            #the wolf is now at sheeps position
            wolves[k].eat_neighbouring_sheep(neighbourhood)
    #display sheep
    for i in range(len(agents)):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    #display wolves
    for i in range(len(wolves)):
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color='black', marker='D')
    #display dead sheep if the wolves have eaten any
    if len(deadsheep) != 0:
        for i in range(len(deadsheep)):
             matplotlib.pyplot.scatter(deadsheep[i].x,deadsheep[i].y, color='red', marker='X')
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


#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat = False, frames=num_of_iterations)
matplotlib.pyplot.show()
