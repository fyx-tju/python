import numpy as np
import matplotlib
#matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import math
import pandas as pd

Xp1=[]
Yp1=[]
tag = False
file= "1.txt" if tag else "2.txt"
fun = lambda x:abs(x-1)
#series = pd.Series([1,2,3,4],index=["a","b","c","d"])
#plt.plot(series)
#plt.title("an example to plot series")
#plt.show()

print(sorted([1,3,5,-1],key=fun))

with open(file, 'r') as f:
  for line in f.readlines():
    pose = np.fromstring(line, dtype=float, sep=' ')
    x=float(pose[0])
    y=float(pose[1])
    Xp1.append(x)
    Yp1.append(y)
plt.plot(Xp1, Yp1, 'b-', label='example')
plt.legend()
plt.show()
