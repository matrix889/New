import matplotlib.pyplot as plt
import numpy as np
import Tkinter
from numpy.random import randn
from matplotlib.pyplot import axes

fig, axes = plt.subplots(2, 2)
fig = plt.figure()

x = np.linspace(0, 4 * np.pi)
y = np.sin(x)

plt.plot(randn(10).cumsum(), 'ko--', label = 'wzx', drawstyle = 'steps-mid')

plt.legend(loc = 'best')

print plt.xlim()
#plt.show()

#class test(object):
#    def __init__(self, *args, **kwargs):
#        print "call the init"
#        #return super(test, self).__init__(*args, **kwargs)
    
#    def __reduce__(self, **kwargs):
#        print "calling the reduce"
#        #return super(test, self).__reduce__(**kwargs)

#tmp = test()
