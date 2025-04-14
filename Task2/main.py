import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 100)  
unit_step = np.heaviside(t, 1)
ramp = t * unit_step 

plt.subplot(1, 2, 1)
plt.plot(t, unit_step, drawstyle='steps-post')
plt.title('Unit Step Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(t, ramp)
plt.title('Ramp Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()

plt.show()