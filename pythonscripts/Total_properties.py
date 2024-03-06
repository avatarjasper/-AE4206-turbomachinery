import numpy as np
from isa import ISA

#### BASIC VALUES ###
h_cruise = 10000
M_cruise = 0.78
Pr_t = 1.6
RPM = 5000
gamma = 1.4

def tot_properties():
    Ts_cruise, Ps_cruise, rho_s_cruise, mu, a = ISA(h_cruise)
    Tt_cruise = Ts_cruise*(1+(gamma-1)/2*M_cruise**2)
    Pt_cruise = Ps_cruise*(1+(gamma-1)/2*M_cruise**2)**(gamma/(gamma-1))
    return Tt_cruise, Pt_cruise

