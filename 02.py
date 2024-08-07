import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x = [random. uniform(0,100) for _ in range(200)]
y= [2* val + 1 + random. uniform(-10,10)for val in x]

x_line = range(101)
y_line = [2* val + 1 for val in x_line]

plt.clf()
plt.scatter(x, y, label = "Random Data Points", color= "green", marker= 'x', s=30, alpha=0.5)
plt.plot(x_line, y_line, label='y=2x+1', color = 'red')

plt.title("Scatter plot Example")
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.savefig("./scatter.png")
plt.show()