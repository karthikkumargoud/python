import numpy as np
import matplotlib.pyplot as plt
fs2 = 500
t2 = np.linspace(0, 2, 2 * fs2, endpoint=False)
sine_5b = np.sin(2 * np.pi * 5 * t2)
cos_10b = np.cos(2 * np.pi * 10 * t2)
product = sine_5b * cos_10b
plt.figure()
plt.plot(t2, product)
plt.title('b. Product of 5 Hz Sine and 10 Hz Cosine')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
