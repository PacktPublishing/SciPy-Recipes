import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_chebyt

fig = plt.figure()

xvalues = np.linspace(-1, 1, 300)
nmax = 5
for n in range(nmax+1):
    yvalues = eval_chebyt(n, xvalues)
    plt.plot(xvalues, yvalues)
plt.title('Chebyshev polynomials $T_n(x)$ for $n=0,\\ldots,{}$'.format(nmax))
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlabel('$x$')
plt.ylabel('$T_n(x)$')

print('Displaying graph')

plt.show()