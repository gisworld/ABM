# -*- coding: utf-8 -*-
"""
Updated 16 Dec 2017
10 sheep eat away at their environments 
Greedy sheep are sick after 100 units
The model stops running when all sheep are at least half full 
@author: amandaf
"""

import matplotlib.pyplot
import matplotlib.animation
import csv
import agentframework
import random

#setup variables
num_of_agents = 10
num_of_iterations = 100
agents = []
#Set to 7 x 6 in order to prevent Qwindowswindows::unable to set geometry
fig = matplotlib.pyplot.figure(figsize=(7, 6))
ax = fig.add_axes([0, 0, 1, 1])
#Empty environmental list
environment = []
#Define neighbourhood
neighbourhood = 10
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
#Setup up global stoppng variable
carry_on = True
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, maxEnv))
# Move the agents.
def update(frame_number):
    fig.clear()
    global carry_on
    #setup figure limits so it stops resizing
    matplotlib.pyplot.xlim(0, maxEnv-1)
    matplotlib.pyplot.ylim(0, maxEnv-1)
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.title("Iteration:" + str(frame_number) + "/" + str(num_of_iterations))
    #print (num_of_iterations)
    #randomise order
    random.shuffle(agents)
    #make the sheep move, eat and be sick
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            #Agent eats values
            agents[i].eat()
            #print("Eating")
            #Agent shares with neighbours
            agents[i].share_with_neighbours(neighbourhood)
            if agents[i].store > 100:
                #Greedy agents are sick if they eat more than 100 units
                agents[i].sick()
                #print ("Being sick")
    test = 0
    for i in range(num_of_agents):
        # agent is half full
        if agents[i].store > 50:
            test += 1
            
    #print (test)
    if test == num_of_agents:
        carry_on = False
    if carry_on == False:
        print("All sheep are at least half full")
        matplotlib.pyplot.title("Model finished! All sheep are at least half full.")
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #print(agents[i].x,agents[i].y)

def gen_function(b = [0]):
    a = 0
    global carry_on 
    global num_of_iterations
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        #print (a)

animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

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
    f2.write(str(agents[i].store)+"\n")
f2.close()