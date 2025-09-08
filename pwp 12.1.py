import numpy as np
import matplotlib.pyplot as plt
fs1 = 1000
t1 = np.linspace(0, 1, fs1, endpoint=False)
sine_5 = np.sin(2 * np.pi * 5 * t1)
sine_10 = np.sin(2 * np.pi * 10 * t1)
sum_signal = sine_5 + sine_10
plt.figure()
plt.plot(t1, sum_signal)
plt.title('a. Sum of 5 Hz and 10 Hz Sine Waves')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')