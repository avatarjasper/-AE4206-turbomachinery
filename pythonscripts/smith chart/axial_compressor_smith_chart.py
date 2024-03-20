import numpy as np
from scipy.interpolate import interpn
import os
path = os.getcwd()
print(path)

def get_repeated_stage_efficiency(phi, lam, r):
    """ This function takes the flow coefficient, work coefficient, and degree
    of reaction of a hypothetical axial compressor (assuming identical,
    repeating stages) and returns the estimated total-to-total isentropic
    efficiency of a well-designed axial compressor matched to those duty
    coefficients. It uses digitized versions of contour plots developed by
    M.V. Casey in 1987 and included on page 90 of:
        R.I. Lewis, "Turbomachinery Performance Analysis," Elsevier Science &
        Technology Books, May 1996. ISBN: 0340631910
    """

    # ***** INPUT *****
    # phi = flow coefficient
    # lam = lambda = work coefficient = 2 * psi
    # r = degree of reaction

    # ***** OUTPUT *****
    # eta_tt = total-to-total isentropic efficiency

    psi = lam / 2  # Conversion to alternative definition of work coefficient.
    eta_tt_min = 0.1  # Return this value as a "minimum" efficiency.

    # X and Y axis of the equivalent Smith charts, with Z axis determining
    # which chart to use depending on degree of reaction.
    x = np.linspace(0.1, 1, 1801)  # flow coefficient range
    y = np.linspace(0.05, 0.5, 901)  # work coefficient range
    z = np.array([0.5, 0.7, 0.9])  # degree of reaction

    # Due to how Python reads in the data, and how the 2D tables get stacked
    # in 3D, the 1st, 2nd, and 3rd dimensions of the final 3D lookup table
    # actually correspond to the z, y, and x axis, respectively.
    points = (z, y, x)  # z = r, y = psi, x = phi

    if phi < min(x) or phi > max(x) \
            or psi < min(y) or psi > max(y) \
            or r < min(z) or r > max(z):
        print("At least one duty coefficient exceeds the range of "
              "applicability of the axial compressor equivalent Smith charts. "
              "Minimum value returned.")
        return eta_tt_min

    # Specific point to be searched based on duty coefficient selection.
    point = np.array([r, psi, phi])

    # Read stored table data.
    values_r0p5 = np.genfromtxt("pythonscripts\smith chart\\axial_compressor_R0p5.dat", delimiter=",")
    values_r0p7 = np.genfromtxt("pythonscripts\smith chart\\axial_compressor_R0p7.dat", delimiter=",")
    values_r0p9 = np.genfromtxt("pythonscripts\smith chart\\axial_compressor_R0p9.dat", delimiter=",")

    # Stack 2D tables into 3D lookup table.
    values = np.array([values_r0p5, values_r0p7, values_r0p9])

    # Interpolate efficiency corresponding to given set of duty coefficients.
    eta_tt = interpn(points, values, point)

    if eta_tt < eta_tt_min:
        eta_tt = eta_tt_min

    return eta_tt


print(get_repeated_stage_efficiency(0.6,0.2,0.5))