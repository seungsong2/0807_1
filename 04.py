import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

data = np.random.rand(10,10)

plt.clf()
heatmap = plt.imshow(data, cmap= "YlGnBu", aspect= 'auto')
plt.colorbar(heatmap)
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.savefig("./boxplot.png")
plt.show()