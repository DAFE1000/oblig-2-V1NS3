import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.e**(-x/4))*np.atan(x)

'''
Explanation for the x-line (mostly for personal learning)
Can use either linspace or arrange,
difference is if you want to have step size
or how many points in the graph.

linspace: (start value, end value, number of points to create [spaced evenly])
    The good thing with linspace is that its basically also a
    "how accurate do you want the graph to be", so if you put a number like 1 in
    the third argument you will get only one point in the graph and... not a lot of
    information out of that tbh. However if you put a number like 1000 you get 1000
    individual points in the graph and the computer essentially draws from each point
    to another.

arrange: (start value, end value, the distance between each point in the graph)
'''
x = np.linspace(0, 30, 100) 
y = f(x) # Create the y values based on the x, basically f(x)

# To make more graphs in case
fig, fx = plt.subplots()

fx.plot(x,y) # Create a graph using the x and y values
fx.set_title("(e**(-x/4))*atan(x)") # Mostly user convenience
plt.show() # Show graph