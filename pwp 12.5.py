import numpy as np
import matplotlib.pyplot as plt
sine_5e = np.sin(2 * np.pi * 5 * t1)
reversed_signal = sine_5e[::-1]
plt.figure()
plt.plot(t1, sine_5e, label='Original')
plt.plot(t1, reversed_signal, label='Reversed')
plt.title('e. Time-Reversed Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()