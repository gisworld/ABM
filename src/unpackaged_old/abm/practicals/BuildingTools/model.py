# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:29:53 2017

@author: amandaf
"""
import random, operator, matplotlib.pyplot, datetime
# Distance between two points
def distance_between(agent0, agent1):
    return (((agent0[0] - agent1[0])**2) + ((agent0[1] - agent1[1])**2))**0.5
# Time taken to run code
def getTimeMS():
    dt = datetime.datetime.now()
    return dt.microsecond + (dt.second * 1000000) + \
    (dt.minute * 1000000 * 60) + (dt.hour * 1000000 * 60 * 60)

start = getTimeMS()  
agents = []
num_of_agents = 10
num_of_iterations = 100
# Set up random position in grid 100x100.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
#print (agents)
# Move agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() <0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0]= (agents[i][0] - 1) % 100
        if random.random() <0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

#Calculate distance between two points
maxdistance = 0
mindistance = 100
for i in range(num_of_agents-1):
    print ("i = " + str(agents[i]))
    for j in range(num_of_agents-1):
        #Do not compare agents against themselves or against previous test
        print ("j= " + str(agents[j]))
        if i != j and j>i:
            print ("Testing agents")
            distance = distance_between(agents[i], agents[j])
            #Calculate max and min distance between agents
            if (distance > maxdistance):
                maxdistance = distance
            elif (distance < mindistance):
                mindistance = distance
            print (mindistance, maxdistance)
print(distance, mindistance, maxdistance)
#Plot points
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
east = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(east[1],east[0], color='red')
matplotlib.pyplot.show()

end = getTimeMS()
#Print time taken
print("time = " + str(end - start))