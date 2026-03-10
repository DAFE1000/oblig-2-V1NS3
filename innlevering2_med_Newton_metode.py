import numpy as np
import matplotlib.pyplot as plt

# To make more graphs
fig, x = plt.subplots(1,2)
fx = np.linspace(0, 30, 10000)

def funskjon1(x):
    return (np.exp(-x/4))*np.atan(x)

# peak = np.argmax(fy1) # Find the maximum value (toppunktet)
# x_max = fx[peak]
# y_max = fy1[peak]
# x[0].plot(x_max, y_max, 'ro', markersize=3)
# print(f"Toppunktet ligger i ({x_max:4f}, {y_max:4f}).")

fy1 = funskjon1(fx) # Create the y values based on the x, basically f(x)
x[0].plot(fx, fy1) # Create a graph using the x and y values
x[0].set_title("Funksjon 1: (e^(-x/4))*atan(x)") # Mostly user convenience
x[0].grid(True) # Show grid

# Se Utregning1.png for å se hvordan jeg kom meg frem til funskjonen her
def f_derivert(x):
    return np.exp(-x/4)*((4-np.atan(x)*(1+x**2))/(4+4*x**2))

fy2 = f_derivert(fx) # Just used the same fx, shouldn't be an issue

def g(x): # The equation in the assignment
    return np.atan(x)-(4/((x**2)+1))

gy = g(fx) # the equation that shows where the peak is

def g_derivert(x): # For Newtons method
    return (1/((x**2)+1))+(8*x/((x**2)+1)**2)

wanted_margin = 1e-6 # The accuracy
x_2 = 1000000 # Just a starting value
# x_1 = float(input("Set a x0 to start Newton's method: "))
x_1 = 1.5 # Start med 1.5 (totally random guess trust me)
i = 0 # Initializing the variable i to stop infinite looping
while abs(x_2 - x_1) > wanted_margin or i == 10000:
    x_2 = x_1 - g(x_1)/g_derivert(x_1)
    x_1 = x_2 # Set xn to the new x_np1
    i += 1
print(f"Nullpunktet ligger i {x_2:.4f} {funskjon1(x_2):.4f}")

x[1].plot(fx, fy2)
x[1].plot(fx, gy)
x[1].set_title("f'(x) og g(x)")
x[1].grid(True) # Show grid

plt.show() # Show graph