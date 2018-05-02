#!/bin/python
import numpy as np
import pyfits
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator as rgi

HI_hdulist = pyfits.open('./HI_NS.fits')
HI = HI_hdulist[0].data

H2_hdulist = pyfits.open('./mod-total-rev2int.fit')
H2 = H2_hdulist[0].data

grid_x = np.linspace(-14.95, 14.95,300)
grid_z = np.linspace(-.4875, .4875,40)

H2_Interp = rgi((grid_z,grid_x,grid_x),H2,fill_value=np.float32(0), method='linear', bounds_error=False)

grid_x = np.linspace(-50, 50,501)
grid_z = np.linspace(-2, 2,51)
HI_Interp = rgi((grid_z,grid_x,grid_x),HI,fill_value=np.float32(0), method='linear', bounds_error=False)

x = np.linspace(-1, 1, 100)
y_H2 = []
y_HI = []

for i in x:
    y_H2.append(H2_Interp((i,8,0)))
    y_HI.append(HI_Interp((i,8,0)))

plt.yscale('log')
plt.plot(x, y_H2)
plt.plot(x, y_HI)

plt.show()
