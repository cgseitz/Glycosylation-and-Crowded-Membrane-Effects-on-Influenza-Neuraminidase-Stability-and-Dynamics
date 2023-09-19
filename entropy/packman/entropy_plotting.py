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
         'ytick.major.size':8,}
pylab.rcParams.update(params)

plt.figure()
plt.rc('xtick', labelsize=26)
plt.rc('ytick', labelsize=26)
plt.rcParams.update({'font.size': 22})
plt.bar(1, 0.522216)
plt.bar(2, 0.283598)
plt.bar(3, 0.218134)
plt.bar(4, 0.161734)
plt.bar(5, 0.134664)
plt.bar(6, 0.132834)
values = np.arange(1,7)
x_labels = ['n', 'n $\pm$ 1', 'n $\pm$ 2', 'n $\pm$ 3', 'n $\pm$ 4', 'n $\pm$ 5']
plt.xticks(values, x_labels)
plt.ylabel(r'Entropy difference ($\dfrac{\rm J}{\rm mol \cdot \rm K}$)')
plt.xlabel(r'Number of residues from sequon $\it{n}$')
plt.ylim(0,0.6)
plt.title('Packing entropy difference from sequon')
plt.savefig('packing_entropy.png')
plt.show()
