import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
from cycler import cycler
from sklearn import preprocessing

from variables import *

# Change the start number to the equivalent of x you want to start
# running the S00x files from
start = 1

#file = 'grf-DL-1625td-S2-2'
#outputs = 3
fullHolder = np.zeros((190,2))

file1 = open('Normal_Dusty/' + file + 'ANORMAL1.txt', "w")
file2 = open('Normal_Dusty/' + file + 'ANORMAL2.txt', "w")
file3 = open('Normal_Dusty/' + file + 'ANORMAL3.txt', "w")

for i in range(start, outputs + 1):

    normalHolder = np.zeros(190)

    # Use the line below for the two shell model for grf
    oldData = np.loadtxt(path + file + '/' + file + 'A.S%.3d' % i)

    lambdaPLT = oldData[:,0]
    FTot = oldData[:,1]

    for j in range(189):

        
        FTotNorm = FTot[j] / (FTot[normal_index]) * normalization_value # 3.7 micron
        #FTotNorm = FTot[j] / (FTot[22]) * 5.303027027027026896e-10 # 3.7 micron
        #FTotNorm = FTot[j] / (FTot[61]) * 1.643625000000000037e-11 # 16 micron
        #FTotNorm = FTot[j] / (FTot[169]) * 4.325749999999999900e-11 # 12 micron
        normalHolder[j] = FTotNorm
        fullHolder[:,0] = lambdaPLT 
        fullHolder[:,1] = normalHolder

    if i == 1:
        np.savetxt(file1,fullHolder)
    elif i == 2:
        np.savetxt(file2,fullHolder)
    elif i == 3:
        np.savetxt(file3,fullHolder)

print("normalization.py")





















