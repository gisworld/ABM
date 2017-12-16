# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:25:05 2017

@author: amandaf
"""
import tkinter
from tkinter import Message
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot
import matplotlib.animation
import csv
import agentframework

matplotlib.use("TkAgg") 
def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
   
num_of_agents = 10
num_of_iterations = 100
agents = []
fig = matplotlib.pyplot.figure(figsize=(7, 7))


root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 
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
    agents.append(agentframework.Agent(environment, maxEnv))
# Move the agents.
def update(frame_number):
    fig.clear()
    global carry_on
    matplotlib.pyplot.xlim(0, maxEnv-1)
    matplotlib.pyplot.ylim(0, maxEnv-1)
    matplotlib.pyplot.imshow(environment)
    for j in range(num_of_iterations):
        print(agents[0].x,agents[0].y)
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
        # agent is half full
        if agents[i].store > 50:
            carry_on = False
        else:
            carry_on = True
        print (carry_on)
    if carry_on == False:
        w = Message(root, anchor="n", text="All sheep are at least half full")
        w.pack()
        print("All sheep are at least half full")
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
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

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    global num_of_iterations
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        print (a)
#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#matplotlib.pyplot.show()
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat = False, frames=num_of_iterations)
tkinter.mainloop()
#matplotlib.pyplot.show()

for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)