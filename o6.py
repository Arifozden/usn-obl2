import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = -x**2 -5

plt.plot(x, y, label='f(x) = -x^2 -5')
plt.xlabel('x')