import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x = [random. uniform(0,100) for _ in range(1000)]
y= [random. uniform(0,100) for _ in range(1000)]


plt.scatter(x, y)

print(x, "\n",y)
plt.clf()
plt.scatter(x, y, lable = "Random Data Points", color= "green", marker= '*', alpha=0.5)
plt.title("Scatter plot Example")
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.savefig("*./scatter.png")
plt.show()
