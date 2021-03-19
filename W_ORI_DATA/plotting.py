import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
from cycler import cycler
from sklearn import preprocessing

from normalization import *
from variables import *
from error_bars import *



lambdaPLT = np.zeros(189)
FTot1 = np.zeros(189)
F_nu = np.loadtxt(converted_path + F_nu_data)
IRAS = np.loadtxt(converted_path + IRAS_data)
mag = np.loadtxt(converted_path + magnitude_data)
sws = np.loadtxt(converted_path + sws_data)




#F_nu = np.loadtxt('FLUX_converted/FLUX-F-nu.txt')
#IRAS = np.loadtxt('FLUX_converted/FLUX-IRAS.txt')
#mag = np.loadtxt('FLUX_converted/FLUX-magnitude.txt')
#sws = np.loadtxt('FLUX_converted/FLUX-sws.txt')


# Figure 1.1
plt.subplot(1,2,1)
for i in range(start, outputs + 1):

    data = np.loadtxt('Normal_Dusty/' + file + 'ANORMAL' + '%.0d' % i + '.txt') 
    lambdaPLT = data[:,0]
    FTot = data[:,1]
    
    # Differenet colors here 
    colors = [hsv_to_rgb([(i * 0.618033988749895) % 1.0, 1, 1])
          for i in range(outputs)]
    plt.rc('axes', prop_cycle=(cycler('color', colors)))

    plt.plot(lambdaPLT, FTot, label = 'S%.3d' % i)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Wavelength ($\lambda$)')
    plt.ylabel('FTot')
    #plt.xlim([10**-2, 10**5])
    #plt.xlim([10**-1, 10**3])
    plt.xlim([10**-0.8, 10**2])
    plt.title(file)
    plt.legend()
  
plt.scatter(F_nu[:,0], F_nu[:,1], c = 'black', s = 1,label = 'F12-F100')
plt.scatter(mag[:,0], mag[:,1], c = 'black',s = 1, label = 'Filter data')
plt.scatter(sws[:,0], sws[:,1],c = 'black',s = 1, label = 'ISO')
plt.scatter(IRAS[:,0], IRAS[:,1], c = 'black',s = 1, label = 'IRAS')

if EB == True:
    plt.errorbar(x,y,yerr=yerror,markersize=0.5,fmt='o',color='black',elinewidth=1.4,capsize=3)





# Figure 1.2
plt.subplot(1,2,2)

for i in range(start, outputs + 1):

    data = np.loadtxt('Normal_Dusty/' + file + 'ANORMAL' + '%.0d' % i + '.txt') 
    lambdaPLT = data[:,0]
    FTot = data[:,1]
    
    # Differenet colors here 
    colors = [hsv_to_rgb([(i * 0.618033988749895) % 1.0, 1, 1])
          for i in range(outputs)]
    plt.rc('axes', prop_cycle=(cycler('color', colors)))

    plt.plot(lambdaPLT, FTot, label = 'S%.3d' % i)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Wavelength ($\lambda$)')
    plt.ylabel('FTot')
    plt.xlim([4*10**-1, 3*10**0])
    plt.ylim([10**-12, 10**-8])
    plt.title(file)
    plt.legend()

plt.scatter(F_nu[:,0], F_nu[:,1], c = 'black', s = 1,label = 'F12-F100')
plt.scatter(mag[:,0], mag[:,1], c = 'black',s = 1, label = 'Filter data')
plt.scatter(sws[:,0], sws[:,1],c = 'black',s = 1, label = 'ISO')
plt.scatter(IRAS[:,0], IRAS[:,1], c = 'black',s = 1, label = 'IRAS')

if EB == True:
    plt.errorbar(x,y,yerr=yerror,markersize=0.5,fmt='o',color='black',elinewidth=1.4,capsize=3)




# Figure 2
plt.figure(2)
for i in range(start, outputs + 1):

    data = np.loadtxt('Normal_Dusty/' + file + 'ANORMAL' + '%.0d' % i + '.txt') 
    lambdaPLT = data[:,0]
    FTot = data[:,1]
    
    # Differenet colors here 
    colors = [hsv_to_rgb([(i * 0.618033988749895) % 1.0, 1, 1])
          for i in range(outputs)]
    plt.rc('axes', prop_cycle=(cycler('color', colors)))

    plt.plot(lambdaPLT, FTot, label = 'S%.3d' % i)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Wavelength ($\lambda$)')
    plt.ylabel('FTot')
    #plt.xlim([10**-2, 10**5])
    plt.xlim([10**-0.8, 10**2])
    #plt.xlim([10**-0.8, 10**2])
    plt.title(file)
    plt.legend()
  
plt.scatter(F_nu[:,0], F_nu[:,1], c = 'black', s = 1,label = 'F12-F100')
plt.scatter(mag[:,0], mag[:,1], c = 'black',s = 1, label = 'Filter data')
plt.scatter(sws[:,0], sws[:,1],c = 'black',s = 1, label = 'ISO')
plt.scatter(IRAS[:,0], IRAS[:,1], c = 'black',s = 1, label = 'IRAS')

if EB == True:
    plt.errorbar(x,y,yerr=yerror,markersize=0.5,fmt='o',color='black',elinewidth=1.4,capsize=3)



# Figure 3
plt.figure(3)
for i in range(start, outputs + 1):

    data = np.loadtxt('Normal_Dusty/' + file + 'ANORMAL' + '%.0d' % i + '.txt') 
    lambdaPLT = data[:,0]
    FTot = data[:,1]
    
    # Differenet colors here 
    colors = [hsv_to_rgb([(i * 0.618033988749895) % 1.0, 1, 1])
          for i in range(outputs)]
    plt.rc('axes', prop_cycle=(cycler('color', colors)))

    plt.plot(lambdaPLT, FTot, label = 'S%.3d' % i)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Wavelength ($\lambda$)')
    plt.ylabel('FTot')
    plt.xlim([4*10**-1, 3*10**0])
    plt.ylim([10**-12, 10**-8])
    plt.title(file)
    plt.legend()
    
plt.scatter(F_nu[:,0], F_nu[:,1], c = 'black', s = 1,label = 'F12-F100')
plt.scatter(mag[:,0], mag[:,1], c = 'black',s = 1, label = 'Filter data')
plt.scatter(sws[:,0], sws[:,1],c = 'black',s = 1, label = 'ISO')
plt.scatter(IRAS[:,0], IRAS[:,1], c = 'black',s = 1, label = 'IRAS')

if EB == True:
    plt.errorbar(x,y,yerr=yerror,markersize=0.5,fmt='o',color='black',elinewidth=1.4,capsize=3)





# Figure 4
plt.figure(4)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Wavelength ($\lambda$)')
plt.ylabel('FTot')
plt.xlim([10**-0.8, 10**2.4])
plt.ylim([10**-16, 10**-8])
plt.scatter(F_nu[:,0], F_nu[:,1], c = 'blue', s = 10,label = 'F12-F100')
plt.scatter(mag[:,0], mag[:,1], c = 'green',s = 10, label = 'Filter data')
plt.scatter(sws[:,0], sws[:,1],c = 'black',s = 1, label = 'ISO')
plt.scatter(IRAS[:,0], IRAS[:,1], c = 'red',s = 4, label = 'IRAS')
plt.legend()
plt.title('Collected Spectra')


print("plotting.py")

plt.show()

