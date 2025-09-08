import numpy as np
import matplotlib.pyplot as plt
shift = 0.1
sine_orig = np.sin(2 * np.pi * 5 * t1)
sine_shifted = np.sin(2 * np.pi * 5 * (t1 - shift))
plt.figure()
plt.plot(t1, sine_orig, label='Original')
plt.plot(t1, sine_shifted, label='Shifted')
plt.title('c. Time Shifted Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()