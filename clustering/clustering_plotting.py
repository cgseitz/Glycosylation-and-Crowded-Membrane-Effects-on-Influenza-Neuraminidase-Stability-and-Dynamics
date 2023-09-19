#load the necessary functions
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as pylab
import itertools
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 15),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large',
         'font.weight':'medium', 
         'xtick.major.size':8,
         'ytick.major.size':8}
pylab.rcParams.update(params)

gly = [100, 98, 33, 14, 7, 4]
ungly = [100, 99, 38, 16, 8, 5]
vir = [100, 100, 100, 71, 30, 16]
gly_error = [0, 1, 3, 1, 1, 1]
ungly_error = [0, 0, 2, 1, 1, 0]
plt.figure()
plt.rc('xtick', labelsize=26)
plt.rc('ytick', labelsize=26)
plt.rcParams.update({'font.size': 22})
plt.plot(ungly, color='blue', linewidth=10)
plt.plot(gly, color='green', linewidth=10)
plt.plot(vir, color='orange', linewidth=10)
values = np.arange(0,6)
plt.errorbar(values, ungly, yerr=ungly_error, color='blue', linewidth=10)
plt.errorbar(values, gly, yerr=gly_error, color='green', linewidth=10)
plt.ylabel('Percent of total frames in cluster')
y_labels = ['0%', '20%', '40%', '60%', '80%', '100%']
values = np.arange(0,101, 20)
plt.yticks(values, y_labels)
plt.xlabel(u'Distance cutoff (\u212b)')
x_labels = ['0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
values = np.arange(0,6)
plt.xticks(values, x_labels)
plt.legend(['2009-H1N1-ungly', '2009-H1N1-gly', '2009-H1N1-vir'], loc='upper right')
plt.title(r'RMSD clusters')
plt.savefig('clustering.png')
plt.show()
