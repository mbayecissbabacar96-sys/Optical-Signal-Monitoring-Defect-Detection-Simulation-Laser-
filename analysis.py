# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:42:18 2026

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n = 500
laser_power = 50
noise = 2
threshold = 52

signal_normal = laser_power + np.random.normal(0, noise, n)
signal_defect = laser_power + 5 + np.random.normal(0, noise, n)

mean_normal = np.mean(signal_normal)
rms_normal = np.sqrt(np.mean(signal_normal**2))

mean_defect = np.mean(signal_defect)
rms_defect = np.sqrt(np.mean(signal_defect**2))

print("NORMAL:", mean_normal, rms_normal)
print("DEFECT:", mean_defect, rms_defect)

# Figure 1
plt.figure()
plt.plot(signal_normal)
plt.axhline(threshold, linestyle='--')
plt.title("Signal NORMAL")
plt.show(block=False)
plt.pause(2)
plt.close()

# Figure 2
plt.figure()
plt.plot(signal_defect)
plt.axhline(threshold, linestyle='--')
plt.title("Signal DEFECT")
plt.show(block=False)
plt.pause(2)
plt.close()

# Figure 3
plt.figure()
plt.hist(signal_normal, bins=30, alpha=0.5, label="NORMAL")
plt.hist(signal_defect, bins=30, alpha=0.5, label="DEFECT")
plt.legend()
plt.title("Histogramme")
plt.show(block=False)
plt.pause(2)
plt.close()