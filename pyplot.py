import numpy as np
import matplotlib.pylab as plt
import math

Xp1=[]
Yp1=[]
tag = False
file= "1.txt" if tag else "2.txt"
fun = lambda x:abs(x-1)

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
