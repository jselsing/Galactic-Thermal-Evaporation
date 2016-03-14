
import numpy as np
import matplotlib.pyplot as pl

def boltzmann(v, m, T):
    k = 1.38064852e-23
    return np.sqrt(   (m /  2. * np.pi * T)**3        ) * 4. * np.pi * v**2 * np.e  ** ( - ((m *v**2. )   / (2. * k * T)   ))

def mass_interior_NFW(r, rho_o, R_s, c = 10.):
    return 4. * np.pi * rho_o * R_s**3. * (   np.log(  (R_s + r) / R_s)  - r / (R_s + r)    )

def escape_velocity(r, M):
    return np.sqrt(2. * G * M / r)




M_O = 15.9994 * 1.66054e-27

v = np.arange(0, 100000, 1)

pl.plot(boltzmann(v, M_O, 1e5))
print(np.sum(boltzmann(v, M_O, 1e5)))
# print(quad(boltzmann, 0, np.inf, args=(M_O, 1e6))[0] )
pl.show()
