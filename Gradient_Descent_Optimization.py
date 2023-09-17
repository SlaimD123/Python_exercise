import numpy as np
import matplotlib.pyplot as plt

def g(w):
    return 1/50*(w**4+w**2+10*w) 

def dg(w):
    return 1/25*(2*w**3+w+5)

def gradient_descent(initial_w, learning_rate, num_iteration):
    w = initial_w
    
    plt.plot(initial_w, g(initial_w), 'go')

    for i in range(num_iteration):
        print("iteration:", i)
        gradient = dg(w)
        print ("gradient:", gradient)
        w = w - learning_rate*gradient
        plt.plot(w, g(w), 'rx')

    return w

initial_w = 90
learning_rate = 0.0002
num_iteration = 150000
w = gradient_descent(initial_w, learning_rate, num_iteration)

print("w:", w)
y = g(w)
print("g(w):", y)


# Create a range of w values to plot
w_vals = np.linspace(-100, 100, 201)

# Plot the function g(w)
plt.plot(w_vals, g(w_vals))

# Plot the values of w at each iteration 

# Label the axes and add a title
plt.xlabel('w')
plt.ylabel('g(w)')
plt.title('Gradient Descent')

# Show the plot
plt.show()
