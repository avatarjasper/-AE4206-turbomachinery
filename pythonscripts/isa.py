
from math import *

g = 9.80665     # [m/s^2]
R = 287.052874  # [J/kg*K]
T_0 = 288.15    # [K]
p_0 = 101325.0  # [Pa]
rho_0 = 1.225   # [kg/m^3]
mu_0 = 1.789e-5 # [Pa*s]
T_S = 110       # [K] Sutherland's constant
gamma = 1.4     # [-]


def ISA(h):
    """
    Calculate and return the ISA temperature [K], pressure [Pa], density [kg/m^3], dynamic viscosity [Pa*s] and speed
    of sound [m/s] at altitude h [m]
    """

    if h <= 11000:
        a = -0.0065     # [K/m]
        T_1 = T_0 + a * (h)
        p_1 = p_0 * ((T_1 / T_0) ** (-(g / (a * R))))
        rho_1 = p_1 / (R * T_1)
        #rho_1 = rho_0 * ((T_1 / T_0) ** (-((g / (a * R)) + 1)))
        #T, p, rho = T_1, p_1, rho_1
        mu = mu_0 * ((T_1/T_0)**(3/2) * (T_0 + T_S)/(T_1 + T_S))
        a = sqrt(gamma*R*T_1)
        return T_1, p_1, rho_1, mu, a

    elif 11000 < h <= 20000:
        h1 = 11000

        a1 = -0.0065
        a2 = 0

        T_1 = T_0 + a1 * (h1)
        T_2 = T_1 + a2 * (h - h1)

        p_1 = p_0 * ((T_1 / T_0) ** (-(g / (a1 * R))))
        p_2 = p_1 * (e ** ((-g / (R * T_2)) * (h - h1)))

        rho_2 = p_2 / (R * T_1)
        mu = mu_0 * ((T_2 / T_0) ** (3 / 2) * (T_0 + T_S) / (T_2 + T_S))
        a = sqrt(gamma * R * T_2)

        return T_2, p_2, rho_2, mu, a

    elif 20000 < h <= 32000:
        h1 = 11000
        h2 = 20000

        a1 = -0.0065
        a2 = 0
        a3 = 0.0010

        T_1 = T_0 + a1 * (h1)
        T_2 = T_1 + a2 * (h2 - h1)
        T_3 = T_2 + a3 * (h - h2)

        p_1 = p_0 * ((T_1 / T_0) ** (-(g / (a1 * R))))
        p_2 = p_1 * (e ** ((-g / (R * T_2)) * (h2 - h1)))
        p_3 = p_2 * ((T_3 / T_1) ** (-(g / (a3 * R))))

        rho_3 = p_3 / (R * T_3)

        mu = mu_0 * ((T_3 / T_0) ** (3 / 2) * (T_0 + T_S) / (T_3 + T_S))
        a = sqrt(gamma * R * T_3)

        return T_3, p_3, rho_3, mu, a

    elif 47000 < h <= 51000:
        h1 = 11000
        h2 = 20000
        h3 = 32000
        h4 = 47000

        a1 = -0.0065
        a2 = 0
        a3 = 0.0010
        a4 = 0.0028
        a5 = 0

        T_1 = T_0 + a1 * (h1)
        T_2 = T_1 + a2 * (h2 - h1)
        T_3 = T_2 + a3 * (h3 - h2)
        T_4 = T_3 + a4 * (h4 - h3)
        T_5 = T_4 + a5 * (h - h4)

        p_1 = p_0 * ((T_1 / T_0) ** (-(g / (a1 * R))))
        p_2 = p_1 * (e ** ((-g / (R * T_2)) * (h2 - h1)))
        p_3 = p_2 * ((T_3 / T_1) ** (-(g / (a3 * R))))
        p_4 = p_3 * ((T_4 / T_3) ** (-(g / (a4 * R))))
        p_5 = p_4 * (e ** ((-g / (R * T_5)) * (h - h4)))

        rho_5 = p_5 / (R * T_5)
        mu = mu_0 * ((T_5 / T_0) ** (3 / 2) * (T_0 + T_S) / (T_5 + T_S))
        a = sqrt(gamma * R * T_5)

        return T_5, p_5, rho_5, mu, a

    elif 51000 < h <= 71000:
        h1 = 11000
        h2 = 20000
        h3 = 32000
        h4 = 47000
        h5 = 51000

        a1 = -0.0065
        a2 = 0
        a3 = 0.0010
        a4 = 0.0028
        a5 = 0
        a6 = -0.0028

        T_1 = T_0 + a1 * (h1)
        T_2 = T_1 + a2 * (h2 - h1)
        T_3 = T_2 + a3 * (h3 - h2)
        T_4 = T_3 + a4 * (h4 - h3)
        T_5 = T_4 + a5 * (h5 - h4)
        T_6 = T_5 + a6 * (h - h5)

        p_1 = p_0 * ((T_1 / T_0) ** (-(g / (a1 * R))))
        p_2 = p_1 * (e ** ((-g / (R * T_2)) * (h2 - h1)))
        p_3 = p_2 * ((T_3 / T_1) ** (-(g / (a3 * R))))
        p_4 = p_3 * ((T_4 / T_3) ** (-(g / (a4 * R))))
        p_5 = p_4 * (e ** ((-g / (R * T_5)) * (h5 - h4)))
        p_6 = p_5 * ((T_6 / T_5) ** (-(g / (a6 * R))))

        rho_6 = p_6 / (R * T_6)

        mu = mu_0 * ((T_6 / T_0) ** (3 / 2) * (T_0 + T_S) / (T_6 + T_S))
        a = sqrt(gamma * R * T_6)

        return T_6, p_6, rho_6, mu, a

    elif 71000 < h <= 86000:
        h1 = 11000
        h2 = 20000
        h3 = 32000
        h4 = 47000
        h5 = 51000
        h6 = 71000

        a1 = -0.0065
        a2 = 0
        a3 = 0.0010
        a4 = 0.0028
        a5 = 0
        a6 = -0.0028
        a7 = -0.0020

        T_1 = T_0 + a1 * (h1)
        T_2 = T_1 + a2 * (h2 - h1)
        T_3 = T_2 + a3 * (h3 - h2)
        T_4 = T_3 + a4 * (h4 - h3)
        T_5 = T_4 + a5 * (h5 - h4)
        T_6 = T_5 + a6 * (h6 - h5)
        T_7 = T_6 + a7 * (h - h6)

        p_1 = p_0 * ((T_1 / T_0) ** (-(g / (a1 * R))))
        p_2 = p_1 * (e ** ((-g / (R * T_2)) * (h2 - h1)))
        p_3 = p_2 * ((T_3 / T_1) ** (-(g / (a3 * R))))
        p_4 = p_3 * ((T_4 / T_3) ** (-(g / (a4 * R))))
        p_5 = p_4 * (e ** ((-g / (R * T_5)) * (h5 - h4)))
        p_6 = p_5 * ((T_6 / T_5) ** (-(g / (a6 * R))))
        p_7 = p_6 * ((T_7 / T_6) ** (-(g / (a7 * R))))

        rho_7 = p_7 / (R * T_7)

        mu = mu_0 * ((T_7 / T_0) ** (3 / 2) * (T_0 + T_S) / (T_7 + T_S))
        a = sqrt(gamma * R * T_7)

        return T_7, p_7, rho_7, mu, a

    #return T, p, rho

if __name__ == "__main__":
    print("test")
    print(ISA(11000))

