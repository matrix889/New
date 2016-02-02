import numpy as np
import scipy as sp
import pylab as pl
import matplotlib.pyplot as plt
import json
import functools


#x = np.linspace(0, 4 * np.pi)
#plt.plot(x, np.sin(x))
#SayHehe()
fig = plt.figure()

a = range(5)
b = range(6, 10)
#f = lambda x : x * x
#g = lambda x : x * 2
sum = lambda x , y : x + y
#func = [f, g]

print reduce(sum, a)

#print reduce(lambda a, x : map(x, a), func, a)