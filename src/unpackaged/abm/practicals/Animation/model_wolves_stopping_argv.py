# -*- coding: utf-8 -*-
"""
Updated 16 Dec 2017
10 sheep eat away at their environments 
2 wolves are introduced which eat nearby sheep
A record of the dead sheep is recorded on screen
@author: Amanda Forbes
"""

import matplotlib.pyplot
import matplotlib.animation
import csv
import agentframework
import wolfframework
import argparse
#set up variables 
parser = argparse.ArgumentParser(description='Define Agent parameters')
#num_of_agents = 10
parser.add_argument('num_of_agents', type=int,
                    help='Number of agents')
parser.add_argument('num_of_wolves',  type=int, 
                    help='Number of wolves')
parser.add_argument('num_of_iterations', type=int,
                    help='Number of iterations')
parser.add_argument('neighbourhood',  type=int, 
                    help='Size of neighbourhood')
try:
    args = parser.parse_args()
    num_of_agents = args.num_of_agents
    num_of_iterations = args.num_of_iterations
    num_of_wolves = args.num_of_wolves
    neighbourhood = args.neighbourhood
except:
    print ("Please enter numbers only seperated by a space") 
wolves =[]
agents = []
deadsheep=[]
#Set up figure
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
#Setup up global stoppng variable
carry_on = True
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, maxEnv))
#create wolves
for i in range(num_of_wolves):
    wolves.append(wolfframework.Wolf(environment,agents, maxEnv, deadsheep))
# Move the agents.
def update(frame_number):
    fig.clear()
    global carry_on
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
    if len(agents)> 0:
        carry_on = True
    else:
        carry_on =False
        print ("All the sheep have been eaten")
    
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

def gen_function(b = [0]):
    a = 0
    global carry_on 
    global num_of_iterations
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        #print (a)
        
#Animate and display the scenario
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
for i in range(len(agents)):
    f2.write(str(agents[i].store)+"\n")
    print (agents[i].store)
f2.close()