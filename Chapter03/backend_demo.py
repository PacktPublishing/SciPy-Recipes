# backend_demo

import numpy as np
import matplotlib
# matplotlib.use('PDF')
import matplotlib.pyplot as plt

f = lambda x: 1/((x-3)**2+.01) + 1/((x-9)**2+.04) - 6
xvalues = np.linspace(2, 10, 300)
yvalues = f(xvalues)

plt.plot(xvalues, yvalues)
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title('The "humps" function')

plt.show()

print('Done plotting.')
