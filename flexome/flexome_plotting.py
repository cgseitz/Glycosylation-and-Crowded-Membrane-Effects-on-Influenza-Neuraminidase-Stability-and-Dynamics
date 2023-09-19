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
plt.title(r'Rigidity by $\alpha$-carbon')
plt.savefig('flexome.png')
plt.show()

gly = [15218, 12745, 7727, 2590, 257, 251]
ungly = [15875, 14479, 3174, 1762, 842, 226]
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
plt.title(r'Rigidity using all atoms')
plt.savefig('flexome_si.png')
plt.show()
