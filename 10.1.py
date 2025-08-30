import matplotlib.pyplot as plt
import numpy as np
# Generate x values from 0 to 10
x = np.linspace(0, 10, 100)
# Define y as a function of x (say y = 2x + 1)
y = 2 * x + 1
# Plot the line
plt.plot(x, y, label="y = 2x + 1", color='blue')
# Add labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Plot Example karthik")
# Show legend
plt.legend()
# Display the plot
plt.show()
