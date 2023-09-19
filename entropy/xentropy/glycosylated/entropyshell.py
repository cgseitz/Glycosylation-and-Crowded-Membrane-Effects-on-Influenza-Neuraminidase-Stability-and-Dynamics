#!/usr/bin/env python3

#use with the my-rdkit-env conda environment, which has pandas and numpy installed

import sys
print(sys.version)

import pandas as pd
import numpy as np

pdg = pd.read_csv('gpsi.txt', sep='\t')

#N891 sequon
n891 = pdg.iloc[383,0]
print("The N891 entropy is:", n891)

n891_plus_one = pdg.iloc[384,0]
n891_plus_two = pdg.iloc[385,0]
n891_plus_three = pdg.iloc[386,0]
n891_plus_four = pdg.iloc[389,0]
n891_plus_five = pdg.iloc[390,0]
n891_minus_one = pdg.iloc[384,0]
n891_minus_two = pdg.iloc[383,0]
n891_minus_three = pdg.iloc[380,0]
n891_minus_four = pdg.iloc[381,0]
n891_minus_five = pdg.iloc[380,0]

data = np.array([n891, n891_plus_one, n891_minus_one])
total = np.average(data)
print("The N891 +- 1 average entropy is:", total, "+-", stddata )

data = np.array([n891, n891_plus_one, n891_plus_two, n891_minus_one, n891_minus_two])
total = np.average(data)
print("The N891 +- 2 average entropy is:", total)

data = np.array([n891, n891_plus_one, n891_plus_two, n891_plus_three, n891_minus_one, n891_minus_two, n891_minus_three])
total = np.average(data)
print("The N891 +- 3 average entropy is:", total)

data = np.array([n891, n891_plus_one, n891_plus_two, n891_plus_three, n891_plus_four, n891_minus_one, n891_minus_two, n891_minus_three, n891_minus_four])
total = np.average(data)
print("The N891 +- 4 average entropy is:", total)

data = np.array([n891, n891_plus_one, n891_plus_two, n891_plus_three, n891_plus_four, n891_plus_five, n891_minus_one, n891_minus_two, n891_minus_three, n891_minus_four, n891_minus_five])
total = np.average(data)
print("The N891 +- 5 average entropy is:", total)

#N1493 sequon
n1493 = pdg.iloc[985, 0]
print("The N1493 entropy is:", n1493)

n1493_plus_one = pdg.iloc[986, 0]
n1493_plus_two = pdg.iloc[987, 0]
n1493_plus_three = pdg.iloc[988, 0]
n1493_plus_four = pdg.iloc[989, 0]
n1493_plus_five = pdg.iloc[990, 0]
n1493_minus_one = pdg.iloc[984, 0]
n1493_minus_two = pdg.iloc[983, 0]
n1493_minus_three = pdg.iloc[982, 0]
n1493_minus_four = pdg.iloc[981, 0]
n1493_minus_five = pdg.iloc[980, 0]

data = np.array([n1493, n1493_plus_one, n1493_minus_one])
total = np.average(data)
print("The N1493 +- 1 average entropy is:", total)

data = np.array([n1493, n1493_plus_one, n1493_plus_two, n1493_minus_one, n1493_minus_two])
total = np.average(data)
print("The N1493 +- 2 average entropy is:", total)

data = np.array([n1493, n1493_plus_one, n1493_plus_two, n1493_plus_three, n1493_minus_one, n1493_minus_two, n1493_minus_three])
total = np.average(data)
print("The N1493 +- 3 average entropy is:", total)

data = np.array([n1493, n1493_plus_one, n1493_plus_two, n1493_plus_three, n1493_plus_four, n1493_minus_one, n1493_minus_two, n1493_minus_three, n1493_minus_four])
total = np.average(data)
print("The N1493 +- 4 average entropy is:", total)

data = np.array([n1493, n1493_plus_one, n1493_plus_two, n1493_plus_three, n1493_plus_four, n1493_plus_five, n1493_minus_one, n1493_minus_two, n1493_minus_three, n1493_minus_four, n1493_minus_five])
total = np.average(data)
print("The N1493 +- 5 average entropy is:", total)

#N1506 sequon
n1506 = pdg.iloc[998, 0]
print("The N1506 entropy is:", n1506)

n1506_plus_one = pdg.iloc[999, 0]
n1506_plus_two = pdg.iloc[1000, 0]
n1506_plus_three = pdg.iloc[1001, 0]
n1506_plus_four = pdg.iloc[1002, 0]
n1506_plus_five = pdg.iloc[1003, 0]
n1506_minus_one = pdg.iloc[997, 0]
n1506_minus_two = pdg.iloc[996, 0]
n1506_minus_three = pdg.iloc[995, 0]
n1506_minus_four = pdg.iloc[994, 0]
n1506_minus_five = pdg.iloc[993, 0]

data = np.array([n1506, n1506_plus_one, n1506_minus_one])
total = np.average(data)
print("The N1506 +- 1 average entropy is:", total)

data = np.array([n1506, n1506_plus_one, n1506_plus_two, n1506_minus_one, n1506_minus_two])
total = np.average(data)
print("The N1506 +- 2 average entropy is:", total)

data = np.array([n1506, n1506_plus_one, n1506_plus_two, n1506_plus_three, n1506_minus_one, n1506_minus_two, n1506_minus_three])
total = np.average(data)
print("The N1506 +- 3 average entropy is:", total)

data = np.array([n1506, n1506_plus_one, n1506_plus_two, n1506_plus_three, n1506_plus_four, n1506_minus_one, n1506_minus_two, n1506_minus_three, n1506_minus_four])
total = np.average(data)
print("The N1506 +- 4 average entropy is:", total)

data = np.array([n1506, n1506_plus_one, n1506_plus_two, n1506_plus_three, n1506_plus_four, n1506_plus_five, n1506_minus_one, n1506_minus_two, n1506_minus_three, n1506_minus_four, n1506_minus_five])
total = np.average(data)
print("The N1506 +- 5 average entropy is:", total)

#N1511 sequon
n1511 = pdg.iloc[1003, 0]
print("The N1511 entropy is:", n1511)

n1511_plus_one = pdg.iloc[1004, 0]
n1511_plus_two = pdg.iloc[1005, 0]
n1511_plus_three = pdg.iloc[1006, 0]
n1511_plus_four = pdg.iloc[1007, 0]
n1511_plus_five = pdg.iloc[1008, 0]
n1511_minus_one = pdg.iloc[1002, 0]
n1511_minus_two = pdg.iloc[1001, 0]
n1511_minus_three = pdg.iloc[1000, 0]
n1511_minus_four = pdg.iloc[999, 0]
n1511_minus_five = pdg.iloc[998, 0]

data = np.array([n1511, n1511_plus_one, n1511_minus_one])
total = np.average(data)
print("The N1511 +- 1 average entropy is:", total)

data = np.array([n1511, n1511_plus_one, n1511_plus_two, n1511_minus_one, n1511_minus_two])
total = np.average(data)
print("The N1511 +- 2 average entropy is:", total)

data = np.array([n1511, n1511_plus_one, n1511_plus_two, n1511_plus_three, n1511_minus_one, n1511_minus_two, n1511_minus_three])
total = np.average(data)
print("The N1511 +- 3 average entropy is:", total)

data = np.array([n1511, n1511_plus_one, n1511_plus_two, n1511_plus_three, n1511_plus_four, n1511_minus_two, n1511_minus_three, n1511_minus_four])
total = np.average(data)
print("The N1511 +- 4 average entropy is:", total)

data = np.array([n1511, n1511_plus_one, n1511_plus_two, n1511_plus_three, n1511_plus_four, n1511_plus_five, n1511_minus_one, n1511_minus_two, n1511_minus_three, n1511_minus_four, n1511_minus_five])
total = np.average(data)
print("The N1511 +- 5 average entropy is:", total)

#N1829 sequon
n1829 = pdg.iloc[1321, 0]
print("The N1829 entropy is:", n1829)

n1829_plus_one = pdg.iloc[1322, 0]
n1829_plus_two = pdg.iloc[1323, 0]
n1829_plus_three = pdg.iloc[1324, 0]
n1829_plus_four = pdg.iloc[1325, 0]
n1829_plus_five = pdg.iloc[1326, 0]
n1829_minus_one = pdg.iloc[1320, 0]
n1829_minus_two = pdg.iloc[1319, 0]
n1829_minus_three = pdg.iloc[1318, 0]
n1829_minus_four = pdg.iloc[1317, 0]
n1829_minus_five = pdg.iloc[1316, 0]

data = np.array([n1829, n1829_plus_one, n1829_minus_one])
total = np.average(data)
print("The N1829 +- 1 average entropy is:", total)

data = np.array([n1829, n1829_plus_one, n1829_plus_two, n1829_minus_one, n1829_minus_two])
total = np.average(data)
print("The N1829 +- 2 average entropy is:", total)

data = np.array([n1829, n1829_plus_one, n1829_plus_two, n1829_plus_three, n1829_minus_one, n1829_minus_two, n1829_minus_three])
total = np.average(data)
print("The N1829 +- 3 average entropy is:", total)

data = np.array([n1829, n1829_plus_one, n1829_plus_two, n1829_plus_three, n1829_plus_four, n1829_minus_one, n1829_minus_two, n1829_minus_three, n1829_minus_four])
total = np.average(data)
print("The N1829 +- 4 average entropy is:", total)

data = np.array([n1829, n1829_plus_one, n1829_plus_two, n1829_plus_three, n1829_plus_four, n1829_plus_five, n1829_minus_one, n1829_minus_two, n1829_minus_three, n1829_minus_four, n1829_minus_five])
total = np.average(data)
print("The N1829 +- 5 average entropy is:", total)

#N1360 sequon
n1360 = pdg.iloc[852, 0]
print("The N1360 entropy is:", n1360)

n1360_plus_one = pdg.iloc[853, 0]
n1360_plus_two = pdg.iloc[854, 0]
n1360_plus_three = pdg.iloc[855, 0]
n1360_plus_four = pdg.iloc[856, 0]
n1360_plus_five = pdg.iloc[857, 0]
n1360_minus_one = pdg.iloc[851, 0]
n1360_minus_two = pdg.iloc[850, 0]
n1360_minus_three = pdg.iloc[849, 0]
n1360_minus_four = pdg.iloc[848, 0]
n1360_minus_five = pdg.iloc[847, 0]

data = np.array([n1360, n1360_plus_one, n1360_minus_one])
total = np.average(data)
print("The N1360 +- 1 average entropy is:", total)

data = np.array([n1360, n1360_plus_one, n1360_plus_two, n1360_minus_one, n1360_minus_two])
total = np.average(data)
print("The N1360 +- 2 average entropy is:", total)

data = np.array([n1360, n1360_plus_one, n1360_plus_two, n1360_plus_three, n1360_minus_one, n1360_minus_two, n1360_minus_three])
total = np.average(data)
print("The N1360 +- 3 average entropy is:", total)

data = np.array([n1360, n1360_plus_one, n1360_plus_two, n1360_plus_three, n1360_plus_four, n1360_minus_one, n1360_minus_two, n1360_minus_three, n1360_minus_four])
total = np.average(data)
print("The N1360 +- 4 average entropy is:", total)

data = np.array([n1360, n1360_plus_one, n1360_plus_two, n1360_plus_three, n1360_plus_four, n1360_plus_five, n1360_minus_one, n1360_minus_two, n1360_minus_three, n1360_minus_four, n1360_minus_five])
total = np.average(data)
print("The N1360 +- 5 average entropy is:", total)

#N1975 sequon
n1975 = pdg.iloc[1467, 0]
print("The N1975 entropy is:", n1975)

n1975_plus_one = pdg.iloc[1468, 0]
n1975_plus_two = pdg.iloc[1469, 0]
n1975_plus_three = pdg.iloc[1470, 0]
n1975_plus_four = pdg.iloc[1471, 0]
n1975_plus_five = pdg.iloc[1472, 0]
n1975_minus_one = pdg.iloc[1466, 0]
n1975_minus_two = pdg.iloc[1465, 0]
n1975_minus_three = pdg.iloc[1464, 0]
n1975_minus_four = pdg.iloc[1463, 0]
n1975_minus_five = pdg.iloc[1462, 0]

data = np.array([n1975, n1975_plus_one, n1975_minus_one])
total = np.average(data)
print("The N1975 +- 1 average entropy is:", total)

data = np.array([n1975, n1975_plus_one, n1975_plus_two, n1975_minus_one, n1975_minus_two])
total = np.average(data)
print("The N1975 +- 2 average entropy is:", total)

data = np.array([n1975, n1975_plus_one, n1975_plus_two, n1975_plus_three, n1975_minus_one, n1975_minus_two, n1975_minus_three])
total = np.average(data)
print("The N1975 +- 3 average entropy is:", total)

data = np.array([n1975, n1975_plus_one, n1975_plus_two, n1975_plus_three, n1975_plus_four, n1975_minus_one, n1975_minus_two, n1975_minus_three, n1975_minus_four])
total = np.average(data)
print("The N1975 +- 4 average entropy is:", total)

data = np.array([n1975, n1975_plus_one, n1975_plus_two, n1975_plus_three, n1975_plus_four, n1975_plus_five, n1975_minus_one, n1975_minus_two, n1975_minus_three, n1975_minus_four, n1975_minus_five])
total = np.average(data)
print("The N1975 +- 5 average entropy is:", total)

#N2298 sequon
n2298 = pdg.iloc[1790, 0]
print("The N2298 entropy is:", n2298)

n2298_plus_one = pdg.iloc[1791, 0]
n2298_plus_two = pdg.iloc[1792, 0]
n2298_plus_three = pdg.iloc[1793, 0]
n2298_plus_four = pdg.iloc[1794, 0]
n2298_plus_five = pdg.iloc[1795, 0]
n2298_minus_one = pdg.iloc[1789, 0]
n2298_minus_two = pdg.iloc[1788, 0]
n2298_minus_three = pdg.iloc[1787, 0]
n2298_minus_four = pdg.iloc[1786, 0]
n2298_minus_five = pdg.iloc[1785, 0]

data = np.array([n2298, n2298_plus_one, n2298_minus_one])
total = np.average(data)
print("The N2298 +- 1 average entropy is:", total)

data = np.array([n2298, n2298_plus_one, n2298_plus_two, n2298_minus_one, n2298_minus_two])
total = np.average(data)
print("The N2298 +- 2 average entropy is:", total)

data = np.array([n2298, n2298_plus_one, n2298_plus_two, n2298_plus_three, n2298_minus_one, n2298_minus_two, n2298_minus_three])
total = np.average(data)
print("The N2298 +- 3 average entropy is:", total)

data = np.array([n2298, n2298_plus_one, n2298_plus_two, n2298_plus_three, n2298_plus_four, n2298_minus_one, n2298_minus_two, n2298_minus_three, n2298_minus_four])
total = np.average(data)
print("The N2298 +- 4 average entropy is:", total)

data = np.array([n2298, n2298_plus_one, n2298_plus_two, n2298_plus_three, n2298_plus_four, n2298_plus_five, n2298_minus_one, n2298_minus_two, n2298_minus_three, n2298_minus_four, n2298_minus_five])
total = np.average(data)
print("The N2298 +- 5 average entropy is:", total)
