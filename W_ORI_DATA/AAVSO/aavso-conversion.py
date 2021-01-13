import numpy as np

import matplotlib.pyplot as plt

def magnitude_conversion():
    
    magnitudes = 'AAVSO-DATA.txt'
    mag = np.genfromtxt(magnitudes, delimiter = '\t')
    
    lambda_mag = mag[:,0]
    mag_list = mag[:,1]
    F_nu_mag = mag[:,2]

    mag_to_Jy = open('AAVSO-converted.txt', 'w')
    mag_converted = np.empty([8,2])

    for i in range(8):
        
        F_nu_Jy = F_nu_mag[i]*(10**(-0.4*mag_list[i]))
        F_lambda_mag = (F_nu_Jy*(300000000)*(10**-26))/(lambda_mag[i]*lambda_mag[i]*0.000001)
        
        Flux_mag = F_lambda_mag*lambda_mag[i]

        mag_converted[i,1] = Flux_mag
        mag_converted[i,0] = lambda_mag[i]

    mag_out = 'AAVSO-converted.txt'
    np.savetxt(mag_out,mag_converted)

# This function assigns the column containing the W/m^2 data from IRAS_LRS.txt to its own txt


magnitude_conversion()



