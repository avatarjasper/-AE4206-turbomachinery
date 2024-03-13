import numpy as np
from isa import ISA

#### BASIC VALUES ###
h_cruise = 10000
M_cruise = 0.78
Pr_t = 1.6
RPM = 5000
gamma = 1.4
R = 287 
m_dot = 80
cp = R*(gamma/(gamma-1))

def tot_properties():
    Ts_cruise, Ps_cruise, rho_s_cruise, mu, a = ISA(h_cruise)
    Tt_cruise = Ts_cruise*(1+(gamma-1)/2*M_cruise**2)
    Pt_cruise = Ps_cruise*(1+(gamma-1)/2*M_cruise**2)**(gamma/(gamma-1))
    return Tt_cruise, Pt_cruise

def enthalpy_change(): #fully isentropic
    Tr = Pr_t**((gamma-1)/gamma)
    T_in,P_in = tot_properties()
    T_out = T_in*Tr
    Dt=T_out-T_in
    return cp*Dt

print("P01: ",tot_properties()[1],"pa","\nT01: ",tot_properties()[0],"K")
print("Enthalpy change: ",enthalpy_change())
