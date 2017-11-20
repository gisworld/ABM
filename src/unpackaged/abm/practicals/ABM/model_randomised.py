# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:29:53 2017

@author: amandaf
"""
import random
# Set up random position in grid 100x100.
y0 = random.randint(0,99)
x0 = random.randint(0,99)
#print (x0)
#print (y0)
# Random walk one step.
if random.random() <0.5:
    y0 += 1 
else:
    y0 -= 1

if random.random() <0.5:
    x0 += 1 
else:
    x0 -= 1

if random.random() <0.5:
    y0 += 1 
else:
    y0 -= 1

if random.random() <0.5:
    x0 += 1 
else:
    x0 -= 1
print (y0, x0)

# Set up random position in grid 100x100.
y1 = random.randint(0,99)
x1 = random.randint(0,99)
# Random walk one step.
if random.random() <0.5:
    y1 += 1 
else:
    y1 -= 1

if random.random() <0.5:
    x1 += 1 
else:
    x1 -= 1

if random.random() <0.5:
    y1 += 1 
else:
    y1 -= 1

if random.random() <0.5:
    x1 += 1 
else:
    x1 -= 1
print (y1, x1)

distance = ((y0-y1)**2 + (x0-x1)**2)**0.5
print (distance)