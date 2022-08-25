import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 1, 50)
p1 = np.power(x, 2)
p2 = np.power(1-x, 2)

plt.plot(x, 1-p1-p2)
plt.xlabel('P_i')
plt.ylabel('Gini Index')
plt.grid()
plt.xlim(0, 1)
plt.xticks([0.1 * i for i in range(11)])

plt.axvline(.5, color='red')
plt.axvline(.48, color='green')
plt.axvline(.176, color='purple')
plt.show()



