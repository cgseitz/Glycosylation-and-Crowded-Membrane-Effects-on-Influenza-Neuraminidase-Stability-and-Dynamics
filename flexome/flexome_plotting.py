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

gly = [1231.53, 1009.57, 393.87, 111.3, 52.93, 36.53]
ungly = [1219.77, 882.5, 373.07, 113.57, 54.27, 39.57]
gly_error = [40.53, 157.03, 265.33, 65.47, 43.10, 20.70]
ungly_error = [45.22, 225.29, 263.81, 86.35, 41.90, 20.62]
plt.figure()
plt.rc('xtick', labelsize=26)
plt.rc('ytick', labelsize=26)
plt.rcParams.update({'font.size': 22})
plt.plot(ungly, color='blue', linewidth=10)
plt.plot(gly, color='green', linewidth=10)
values = np.arange(0,6)
plt.errorbar(values, ungly, yerr=ungly_error, color='blue', linewidth=10)
plt.errorbar(values, gly, yerr=gly_error, color='green', linewidth=10)
plt.ylabel('Clusters')
plt.xlabel(r'Energy cutoff ($\dfrac{\rm kcal}{\rm mol}$)')
x_labels = ['0.5', '1.0', '1.5', '2.0', '2.5', '3.0']
values = np.arange(0,6)
plt.xticks(values, x_labels)
plt.legend(['2009-H1N1-ungly', '2009-H1N1-gly'], loc='upper right')
plt.title(r'Average rigidity by $\alpha$-carbon')
plt.savefig('flexome.png')
plt.show()


gly = [1277, 1094, 668, 219, 37, 36]
ungly = [1340, 1233, 282, 154, 74, 23]
plt.figure()
plt.rc('xtick', labelsize=26)
plt.rc('ytick', labelsize=26)
plt.rcParams.update({'font.size': 22})
plt.plot(ungly, color='blue', linewidth=10)
plt.plot(gly, color='green', linewidth=10)
plt.ylabel('Clusters')
plt.xlabel(r'Energy cutoff ($\dfrac{\rm kcal}{\rm mol}$)')
x_labels = ['0.5', '1', '1.5', '2', '2.5', '3']
values = np.arange(0,6)
plt.xticks(values, x_labels)
plt.legend(['2009-H1N1-ungly', '2009-H1N1-gly'])
plt.title(r'Rigidity by $\alpha$-carbon at 298 K')
plt.savefig('flexome_si298K.png')
plt.show()

gly = [1470, 1369, 1312, 1210, 936, 543]
ungly = [1457, 1422, 1371, 1251, 1086, 372]
plt.figure()
plt.rc('xtick', labelsize=26)
plt.rc('ytick', labelsize=26)
plt.rcParams.update({'font.size': 22})
plt.plot(ungly, color='blue', linewidth=10)
plt.plot(gly, color='green', linewidth=10)
plt.ylabel('Clusters')
plt.xlabel(r'Energy cutoff ($\dfrac{\rm kcal}{\rm mol}$)')
x_labels = ['0.5', '1', '1.5', '2', '2.5', '3']
values = np.arange(0,6)
plt.xticks(values, x_labels)
plt.legend(['2009-H1N1-ungly', '2009-H1N1-gly'])
plt.title(r'Rigidity by $\alpha$-carbon at 0 K')
plt.savefig('flexome_si0K.png')
plt.show()
