import numpy as np
import matplotlib.pyplot as plt

# To make more graphs
fig, x = plt.subplots(1,2)
fx = np.linspace(0, 30, 1000)

def funskjon1(x):
    return (np.exp(-x/4))*np.atan(x)

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

fy1 = funskjon1(fx) # Create the y values based on the x, basically f(x)
peak = np.argmax(fy1) # Find the maximum value (toppunktet)
x_max = fx[peak]
y_max = fy1[peak]
print(f"Toppunktet ligger i ({x_max:4f}, {y_max:4f}).")

x[0].plot(fx, fy1) # Create a graph using the x and y values
x[0].plot(x_max, y_max, 'ro', markersize=3)
x[0].set_title("Funksjon 1: (e^(-x/4))*atan(x)") # Mostly user convenience
x[0].grid(True) # Show grid

# Se Utregning1.png for å se hvordan jeg kom meg frem til funskjonen her
def f_derivert(x):
    return np.exp(-x/4)*((4-np.atan(x)*(1+x**2))/(4+4*x**2))

fy2 = f_derivert(fx) # Just used the same fx, shouldn't be an issue

def g(x):
    return np.atan(x)-(4/((x**2)+1))

gy = g(fx) # the equation that shows where the peak is

x[1].plot(fx, fy2)
x[1].plot(fx, gy)
x[1].set_title("f'(x) og g(x)")
x[1].grid(True) # Show grid

plt.show() # Show graph