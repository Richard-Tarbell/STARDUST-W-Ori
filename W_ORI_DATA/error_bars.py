
import numpy as np

from variables import *


error_bars = np.loadtxt(path_AAVSO + AAVSO_file)
error_bars_lambda = error_bars[:,0]
error_bars_flux = error_bars[:,1]

lambda_errors = np.empty(4)
flux_errors = np.empty(4)
for i in range(4):
        lambda_errors[i] = error_bars_lambda[i * 2]

j = 0
for i in range(4):
        flux_errors[i] = (error_bars_flux[j+1] + error_bars_flux[j]) / 2
        j = j + 2 

yerrormin = np.zeros(4)
j = 0
for i in range(4):
        yerrormin[i] =  flux_errors[i] - error_bars_flux[j]
        j = j + 2

yerrormax = np.zeros(4)
j = 1
for i in range(4):
        yerrormax[i] = error_bars_flux[j] - flux_errors[i]
        j = j + 2

x = lambda_errors
y = flux_errors
yerror = [yerrormin, yerrormax]

print("error_bars.py")
