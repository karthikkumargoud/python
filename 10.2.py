import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = x          # Line 1: y = x
y2 = x**2       # Line 2: y = x^2
y3 = np.sqrt(x) # Line 3: y = √x
plt.plot(x, y1, label="y = x", color='blue')
plt.plot(x, y2, label="y = x²", color='red')
plt.plot(x, y3, label="y = √x", color='green')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Lines on Same Plot karthik")
plt.legend()
plt.show()
