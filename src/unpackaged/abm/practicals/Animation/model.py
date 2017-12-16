# -*- coding: utf-8 -*-
"""
Updated 16 Dec 2017
10 sheep eat away at their environments 
Greedy sheep are sick after 100 units
@author: amandaf
"""

import matplotlib.pyplot
import matplotlib.animation
import csv
import agentframework

num_of_agents = 10
num_of_iterations = 100
agents = []
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
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, maxEnv))
# Move the agents.
def update(frame_number):
    fig.clear()
    matplotlib.pyplot.xlim(0, maxEnv-1)
    matplotlib.pyplot.ylim(0, maxEnv-1)
    matplotlib.pyplot.imshow(environment)
    for j in range(num_of_iterations):
        #print(agents[0].x,agents[0].y)
        for i in range(num_of_agents):           
            agents[i].move()
            #Agent eats values
            agents[i].eat()
            #print("Eating")
            if agents[i].store > 100:
                #Greedy agents are sick if they eat more than 100 units
                agents[i].sick()
                #print ("Being sick")
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

#Display animation
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat = False, frames=num_of_iterations)
matplotlib.pyplot.show()

#Write out environment to file
f2 = open('environment.txt','w', newline='')
writer = csv.writer(f2)
for row in environment:
    writer.writerow(row)
f2.close()
#Write store count to file
f2 = open('store.txt','a')
for i in range(num_of_agents):
    print (agents[i].store)
    f2.write(str(agents[i].store)+"\n")
f2.close()