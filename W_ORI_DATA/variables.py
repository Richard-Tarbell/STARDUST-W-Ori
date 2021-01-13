
# The name of the Model
file = 'amC-hann-1625td'

# The path your S00x files are located
path = './DUSTY_files/Models/'
#path = 'D:/Documents/STARDUST/RESEARCH/DUSTY/Models/grf-two-shell/'


# The path your converted data is located and the file names for each
converted_path = 'FLUX_converted/'
F_nu_data = 'FLUX-F-nu.txt'
IRAS_data = 'FLUX-IRAS.txt'
magnitude_data = 'FLUX-magnitude.txt'
sws_data = 'FLUX-sws.txt'

# The path to your AAVSO data in order to create your error bars
path_AAVSO = './AAVSO/'
AAVSO_file = 'AAVSO-converted.txt'

# How many S003 files do you want to plot
outputs = 3

# The line that your lambda value takes place in your S00x files
# Remember that any line with a "#" does not count and it starts counting
# from 0 (0, 1, 2, 3.... normal_index)
normal_index = 22

normalization_value = 5.303027027027026896e-10 # 3.7 micron
# 5.303027027027026896e-10 # 3.7 micron
# 1.643625000000000037e-11 # 16 micron
# 4.325749999999999900e-11 # 12 micron

print("variables.py")
