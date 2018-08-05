from itertools import *
import numpy as np

#for i in cycle(np.array([1,2])):
#  print(i)

def fun(num=2):
  for i in range(num):
    yield i

for i in fun(10):
  print(i)

r = [1,2,3,3,4,5,6,4]
r.sort()
for i,j in (groupby(r)):
  print(i,j)
