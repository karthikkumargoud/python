import numpy as np
import matplotlib.pyplot as plt
sine_10d = np.sin(2 * np.pi * 10 * t1)
scaled = 3 * sine_10d
plt.figure()
plt.plot(t1, sine_10d, label='Original')
plt.plot(t1, scaled, label='Scaled')
plt.title('d. Scaled Amplitude of 10 Hz Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()