import numpy as np
import pyfits
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator as rgi

H2_hdulist = pyfits.open('./mod-total-rev2int.fit')
H2 = H2_hdulist[0].data

grid_x = np.linspace(-14.95, 14.95, 300)
grid_z = np.linspace(-.4875, .4875, 40)

H2_Interp = rgi((grid_z,grid_x,grid_x), H2, fill_value=np.float32(0), method='linear', bounds_error=False)

x = np.linspace(-1, 1, 100)
y = []

for i in x:
    y.append(H2_Interp((i,8,0)))

plt.yscale('log')
plt.plot(x, y)

plt.show()
