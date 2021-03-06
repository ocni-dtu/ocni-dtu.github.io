__author__ = "Christian Kongsgaard"
__license__ = 'MIT'

# -------------------------------------------------------------------------------------------------------------------- #
# IMPORTS

# Modules
import numpy as np
import math

# -------------------------------------------------------------------------------------------------------------------- #
# Functions


def utci_ladybug(Ta, Tmrt, va, RH):
    # Define a function to change the RH to water saturation vapor pressure in hPa
    def es(ta):
        g = [-2836.5744, -6028.076559, 19.54263612, -0.02737830188, 0.000016261698, (7.0229056 * (10 ** (-10))),
             (-1.8680009 * (10 ** (-13)))]
        tk = ta + 273.15  # air temp in K
        es_ = 2.7150305 * math.log(tk)
        for count, i in enumerate(g):
            es_ = es_ + (i * (tk ** (count - 2)))
        es_ = math.exp(es_) * 0.01  # convert Pa to hPa
        return es_

    # If everything is good, run the data through the model below to get the UTCI.
    # This is a python version of the UTCI_approx function, Version a 0.002, October 2009
    # Ta: air temperature, degree Celsius
    # ehPa: water vapour presure, hPa=hecto Pascal
    # Tmrt: mean radiant temperature, degree Celsius
    # va10m: wind speed 10 m above ground level in m/s

    ehPa = es(Ta) * (RH / 100.0)
    D_Tmrt = Tmrt - Ta
    Pa = ehPa / 10.0  # convert vapour pressure to kPa

    UTCI_approx = Ta + \
                  (0.607562052) + \
                  (-0.0227712343) * Ta + \
                  (8.06470249 * (10 ** (-4))) * Ta * Ta + \
                  (-1.54271372 * (10 ** (-4))) * Ta * Ta * Ta + \
                  (-3.24651735 * (10 ** (-6))) * Ta * Ta * Ta * Ta + \
                  (7.32602852 * (10 ** (-8))) * Ta * Ta * Ta * Ta * Ta + \
                  (1.35959073 * (10 ** (-9))) * Ta * Ta * Ta * Ta * Ta * Ta + \
                  (-2.25836520) * va + \
                  (0.0880326035) * Ta * va + \
                  (0.00216844454) * Ta * Ta * va + \
                  (-1.53347087 * (10 ** (-5))) * Ta * Ta * Ta * va + \
                  (-5.72983704 * (10 ** (-7))) * Ta * Ta * Ta * Ta * va + \
                  (-2.55090145 * (10 ** (-9))) * Ta * Ta * Ta * Ta * Ta * va + \
                  (-0.751269505) * va * va + \
                  (-0.00408350271) * Ta * va * va + \
                  (-5.21670675 * (10 ** (-5))) * Ta * Ta * va * va + \
                  (1.94544667 * (10 ** (-6))) * Ta * Ta * Ta * va * va + \
                  (1.14099531 * (10 ** (-8))) * Ta * Ta * Ta * Ta * va * va + \
                  (0.158137256) * va * va * va + \
                  (-6.57263143 * (10 ** (-5))) * Ta * va * va * va + \
                  (2.22697524 * (10 ** (-7))) * Ta * Ta * va * va * va + \
                  (-4.16117031 * (10 ** (-8))) * Ta * Ta * Ta * va * va * va + \
                  (-0.0127762753) * va * va * va * va + \
                  (9.66891875 * (10 ** (-6))) * Ta * va * va * va * va + \
                  (2.52785852 * (10 ** (-9))) * Ta * Ta * va * va * va * va + \
                  (4.56306672 * (10 ** (-4))) * va * va * va * va * va + \
                  (-1.74202546 * (10 ** (-7))) * Ta * va * va * va * va * va + \
                  (-5.91491269 * (10 ** (-6))) * va * va * va * va * va * va + \
                  (0.398374029) * D_Tmrt + \
                  (1.83945314 * (10 ** (-4))) * Ta * D_Tmrt + \
                  (-1.73754510 * (10 ** (-4))) * Ta * Ta * D_Tmrt + \
                  (-7.60781159 * (10 ** (-7))) * Ta * Ta * Ta * D_Tmrt + \
                  (3.77830287 * (10 ** (-8))) * Ta * Ta * Ta * Ta * D_Tmrt + \
                  (5.43079673 * (10 ** (-10))) * Ta * Ta * Ta * Ta * Ta * D_Tmrt + \
                  (-0.0200518269) * va * D_Tmrt + \
                  (8.92859837 * (10 ** (-4))) * Ta * va * D_Tmrt + \
                  (3.45433048 * (10 ** (-6))) * Ta * Ta * va * D_Tmrt + \
                  (-3.77925774 * (10 ** (-7))) * Ta * Ta * Ta * va * D_Tmrt + \
                  (-1.69699377 * (10 ** (-9))) * Ta * Ta * Ta * Ta * va * D_Tmrt + \
                  (1.69992415 * (10 ** (-4))) * va * va * D_Tmrt + \
                  (-4.99204314 * (10 ** (-5))) * Ta * va * va * D_Tmrt + \
                  (2.47417178 * (10 ** (-7))) * Ta * Ta * va * va * D_Tmrt + \
                  (1.07596466 * (10 ** (-8))) * Ta * Ta * Ta * va * va * D_Tmrt + \
                  (8.49242932 * (10 ** (-5))) * va * va * va * D_Tmrt + \
                  (1.35191328 * (10 ** (-6))) * Ta * va * va * va * D_Tmrt + \
                  (-6.21531254 * (10 ** (-9))) * Ta * Ta * va * va * va * D_Tmrt + \
                  (-4.99410301 * (10 ** (-6))) * va * va * va * va * D_Tmrt + \
                  (-1.89489258 * (10 ** (-8))) * Ta * va * va * va * va * D_Tmrt + \
                  (8.15300114 * (10 ** (-8))) * va * va * va * va * va * D_Tmrt + \
                  (7.55043090 * (10 ** (-4))) * D_Tmrt * D_Tmrt + \
                  (-5.65095215 * (10 ** (-5))) * Ta * D_Tmrt * D_Tmrt + \
                  (-4.52166564 * (10 ** (-7))) * Ta * Ta * D_Tmrt * D_Tmrt + \
                  (2.46688878 * (10 ** (-8))) * Ta * Ta * Ta * D_Tmrt * D_Tmrt + \
                  (2.42674348 * (10 ** (-10))) * Ta * Ta * Ta * Ta * D_Tmrt * D_Tmrt + \
                  (1.54547250 * (10 ** (-4))) * va * D_Tmrt * D_Tmrt + \
                  (5.24110970 * (10 ** (-6))) * Ta * va * D_Tmrt * D_Tmrt + \
                  (-8.75874982 * (10 ** (-8))) * Ta * Ta * va * D_Tmrt * D_Tmrt + \
                  (-1.50743064 * (10 ** (-9))) * Ta * Ta * Ta * va * D_Tmrt * D_Tmrt + \
                  (-1.56236307 * (10 ** (-5))) * va * va * D_Tmrt * D_Tmrt + \
                  (-1.33895614 * (10 ** (-7))) * Ta * va * va * D_Tmrt * D_Tmrt + \
                  (2.49709824 * (10 ** (-9))) * Ta * Ta * va * va * D_Tmrt * D_Tmrt + \
                  (6.51711721 * (10 ** (-7))) * va * va * va * D_Tmrt * D_Tmrt + \
                  (1.94960053 * (10 ** (-9))) * Ta * va * va * va * D_Tmrt * D_Tmrt + \
                  (-1.00361113 * (10 ** (-8))) * va * va * va * va * D_Tmrt * D_Tmrt + \
                  (-1.21206673 * (10 ** (-5))) * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (-2.18203660 * (10 ** (-7))) * Ta * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (7.51269482 * (10 ** (-9))) * Ta * Ta * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (9.79063848 * (10 ** (-11))) * Ta * Ta * Ta * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (1.25006734 * (10 ** (-6))) * va * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (-1.81584736 * (10 ** (-9))) * Ta * va * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (-3.52197671 * (10 ** (-10))) * Ta * Ta * va * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (-3.36514630 * (10 ** (-8))) * va * va * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (1.35908359 * (10 ** (-10))) * Ta * va * va * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (4.17032620 * (10 ** (-10))) * va * va * va * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (-1.30369025 * (10 ** (-9))) * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (4.13908461 * (10 ** (-10))) * Ta * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (9.22652254 * (10 ** (-12))) * Ta * Ta * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (-5.08220384 * (10 ** (-9))) * va * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (-2.24730961 * (10 ** (-11))) * Ta * va * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (1.17139133 * (10 ** (-10))) * va * va * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (6.62154879 * (10 ** (-10))) * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (4.03863260 * (10 ** (-13))) * Ta * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (1.95087203 * (10 ** (-12))) * va * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (-4.73602469 * (10 ** (-12))) * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt + \
                  (5.12733497) * Pa + \
                  (-0.312788561) * Ta * Pa + \
                  (-0.0196701861) * Ta * Ta * Pa + \
                  (9.99690870 * (10 ** (-4))) * Ta * Ta * Ta * Pa + \
                  (9.51738512 * (10 ** (-6))) * Ta * Ta * Ta * Ta * Pa + \
                  (-4.66426341 * (10 ** (-7))) * Ta * Ta * Ta * Ta * Ta * Pa + \
                  (0.548050612) * va * Pa + \
                  (-0.00330552823) * Ta * va * Pa + \
                  (-0.00164119440) * Ta * Ta * va * Pa + \
                  (-5.16670694 * (10 ** (-6))) * Ta * Ta * Ta * va * Pa + \
                  (9.52692432 * (10 ** (-7))) * Ta * Ta * Ta * Ta * va * Pa + \
                  (-0.0429223622) * va * va * Pa + \
                  (0.00500845667) * Ta * va * va * Pa + \
                  (1.00601257 * (10 ** (-6))) * Ta * Ta * va * va * Pa + \
                  (-1.81748644 * (10 ** (-6))) * Ta * Ta * Ta * va * va * Pa + \
                  (-1.25813502 * (10 ** (-3))) * va * va * va * Pa + \
                  (-1.79330391 * (10 ** (-4))) * Ta * va * va * va * Pa + \
                  (2.34994441 * (10 ** (-6))) * Ta * Ta * va * va * va * Pa + \
                  (1.29735808 * (10 ** (-4))) * va * va * va * va * Pa + \
                  (1.29064870 * (10 ** (-6))) * Ta * va * va * va * va * Pa + \
                  (-2.28558686 * (10 ** (-6))) * va * va * va * va * va * Pa + \
                  (-0.0369476348) * D_Tmrt * Pa + \
                  (0.00162325322) * Ta * D_Tmrt * Pa + \
                  (-3.14279680 * (10 ** (-5))) * Ta * Ta * D_Tmrt * Pa + \
                  (2.59835559 * (10 ** (-6))) * Ta * Ta * Ta * D_Tmrt * Pa + \
                  (-4.77136523 * (10 ** (-8))) * Ta * Ta * Ta * Ta * D_Tmrt * Pa + \
                  (8.64203390 * (10 ** (-3))) * va * D_Tmrt * Pa + \
                  (-6.87405181 * (10 ** (-4))) * Ta * va * D_Tmrt * Pa + \
                  (-9.13863872 * (10 ** (-6))) * Ta * Ta * va * D_Tmrt * Pa + \
                  (5.15916806 * (10 ** (-7))) * Ta * Ta * Ta * va * D_Tmrt * Pa + \
                  (-3.59217476 * (10 ** (-5))) * va * va * D_Tmrt * Pa + \
                  (3.28696511 * (10 ** (-5))) * Ta * va * va * D_Tmrt * Pa + \
                  (-7.10542454 * (10 ** (-7))) * Ta * Ta * va * va * D_Tmrt * Pa + \
                  (-1.24382300 * (10 ** (-5))) * va * va * va * D_Tmrt * Pa + \
                  (-7.38584400 * (10 ** (-9))) * Ta * va * va * va * D_Tmrt * Pa + \
                  (2.20609296 * (10 ** (-7))) * va * va * va * va * D_Tmrt * Pa + \
                  (-7.32469180 * (10 ** (-4))) * D_Tmrt * D_Tmrt * Pa + \
                  (-1.87381964 * (10 ** (-5))) * Ta * D_Tmrt * D_Tmrt * Pa + \
                  (4.80925239 * (10 ** (-6))) * Ta * Ta * D_Tmrt * D_Tmrt * Pa + \
                  (-8.75492040 * (10 ** (-8))) * Ta * Ta * Ta * D_Tmrt * D_Tmrt * Pa + \
                  (2.77862930 * (10 ** (-5))) * va * D_Tmrt * D_Tmrt * Pa + \
                  (-5.06004592 * (10 ** (-6))) * Ta * va * D_Tmrt * D_Tmrt * Pa + \
                  (1.14325367 * (10 ** (-7))) * Ta * Ta * va * D_Tmrt * D_Tmrt * Pa + \
                  (2.53016723 * (10 ** (-6))) * va * va * D_Tmrt * D_Tmrt * Pa + \
                  (-1.72857035 * (10 ** (-8))) * Ta * va * va * D_Tmrt * D_Tmrt * Pa + \
                  (-3.95079398 * (10 ** (-8))) * va * va * va * D_Tmrt * D_Tmrt * Pa + \
                  (-3.59413173 * (10 ** (-7))) * D_Tmrt * D_Tmrt * D_Tmrt * Pa + \
                  (7.04388046 * (10 ** (-7))) * Ta * D_Tmrt * D_Tmrt * D_Tmrt * Pa + \
                  (-1.89309167 * (10 ** (-8))) * Ta * Ta * D_Tmrt * D_Tmrt * D_Tmrt * Pa + \
                  (-4.79768731 * (10 ** (-7))) * va * D_Tmrt * D_Tmrt * D_Tmrt * Pa + \
                  (7.96079978 * (10 ** (-9))) * Ta * va * D_Tmrt * D_Tmrt * D_Tmrt * Pa + \
                  (1.62897058 * (10 ** (-9))) * va * va * D_Tmrt * D_Tmrt * D_Tmrt * Pa + \
                  (3.94367674 * (10 ** (-8))) * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * Pa + \
                  (-1.18566247 * (10 ** (-9))) * Ta * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * Pa + \
                  (3.34678041 * (10 ** (-10))) * va * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * Pa + \
                  (-1.15606447 * (10 ** (-10))) * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * Pa + \
                  (-2.80626406) * Pa * Pa + \
                  (0.548712484) * Ta * Pa * Pa + \
                  (-0.00399428410) * Ta * Ta * Pa * Pa + \
                  (-9.54009191 * (10 ** (-4))) * Ta * Ta * Ta * Pa * Pa + \
                  (1.93090978 * (10 ** (-5))) * Ta * Ta * Ta * Ta * Pa * Pa + \
                  (-0.308806365) * va * Pa * Pa + \
                  (0.0116952364) * Ta * va * Pa * Pa + \
                  (4.95271903 * (10 ** (-4))) * Ta * Ta * va * Pa * Pa + \
                  (-1.90710882 * (10 ** (-5))) * Ta * Ta * Ta * va * Pa * Pa + \
                  (0.00210787756) * va * va * Pa * Pa + \
                  (-6.98445738 * (10 ** (-4))) * Ta * va * va * Pa * Pa + \
                  (2.30109073 * (10 ** (-5))) * Ta * Ta * va * va * Pa * Pa + \
                  (4.17856590 * (10 ** (-4))) * va * va * va * Pa * Pa + \
                  (-1.27043871 * (10 ** (-5))) * Ta * va * va * va * Pa * Pa + \
                  (-3.04620472 * (10 ** (-6))) * va * va * va * va * Pa * Pa + \
                  (0.0514507424) * D_Tmrt * Pa * Pa + \
                  (-0.00432510997) * Ta * D_Tmrt * Pa * Pa + \
                  (8.99281156 * (10 ** (-5))) * Ta * Ta * D_Tmrt * Pa * Pa + \
                  (-7.14663943 * (10 ** (-7))) * Ta * Ta * Ta * D_Tmrt * Pa * Pa + \
                  (-2.66016305 * (10 ** (-4))) * va * D_Tmrt * Pa * Pa + \
                  (2.63789586 * (10 ** (-4))) * Ta * va * D_Tmrt * Pa * Pa + \
                  (-7.01199003 * (10 ** (-6))) * Ta * Ta * va * D_Tmrt * Pa * Pa + \
                  (-1.06823306 * (10 ** (-4))) * va * va * D_Tmrt * Pa * Pa + \
                  (3.61341136 * (10 ** (-6))) * Ta * va * va * D_Tmrt * Pa * Pa + \
                  (2.29748967 * (10 ** (-7))) * va * va * va * D_Tmrt * Pa * Pa + \
                  (3.04788893 * (10 ** (-4))) * D_Tmrt * D_Tmrt * Pa * Pa + \
                  (-6.42070836 * (10 ** (-5))) * Ta * D_Tmrt * D_Tmrt * Pa * Pa + \
                  (1.16257971 * (10 ** (-6))) * Ta * Ta * D_Tmrt * D_Tmrt * Pa * Pa + \
                  (7.68023384 * (10 ** (-6))) * va * D_Tmrt * D_Tmrt * Pa * Pa + \
                  (-5.47446896 * (10 ** (-7))) * Ta * va * D_Tmrt * D_Tmrt * Pa * Pa + \
                  (-3.59937910 * (10 ** (-8))) * va * va * D_Tmrt * D_Tmrt * Pa * Pa + \
                  (-4.36497725 * (10 ** (-6))) * D_Tmrt * D_Tmrt * D_Tmrt * Pa * Pa + \
                  (1.68737969 * (10 ** (-7))) * Ta * D_Tmrt * D_Tmrt * D_Tmrt * Pa * Pa + \
                  (2.67489271 * (10 ** (-8))) * va * D_Tmrt * D_Tmrt * D_Tmrt * Pa * Pa + \
                  (3.23926897 * (10 ** (-9))) * D_Tmrt * D_Tmrt * D_Tmrt * D_Tmrt * Pa * Pa + \
                  (-0.0353874123) * Pa * Pa * Pa + \
                  (-0.221201190) * Ta * Pa * Pa * Pa + \
                  (0.0155126038) * Ta * Ta * Pa * Pa * Pa + \
                  (-2.63917279 * (10 ** (-4))) * Ta * Ta * Ta * Pa * Pa * Pa + \
                  (0.0453433455) * va * Pa * Pa * Pa + \
                  (-0.00432943862) * Ta * va * Pa * Pa * Pa + \
                  (1.45389826 * (10 ** (-4))) * Ta * Ta * va * Pa * Pa * Pa + \
                  (2.17508610 * (10 ** (-4))) * va * va * Pa * Pa * Pa + \
                  (-6.66724702 * (10 ** (-5))) * Ta * va * va * Pa * Pa * Pa + \
                  (3.33217140 * (10 ** (-5))) * va * va * va * Pa * Pa * Pa + \
                  (-0.00226921615) * D_Tmrt * Pa * Pa * Pa + \
                  (3.80261982 * (10 ** (-4))) * Ta * D_Tmrt * Pa * Pa * Pa + \
                  (-5.45314314 * (10 ** (-9))) * Ta * Ta * D_Tmrt * Pa * Pa * Pa + \
                  (-7.96355448 * (10 ** (-4))) * va * D_Tmrt * Pa * Pa * Pa + \
                  (2.53458034 * (10 ** (-5))) * Ta * va * D_Tmrt * Pa * Pa * Pa + \
                  (-6.31223658 * (10 ** (-6))) * va * va * D_Tmrt * Pa * Pa * Pa + \
                  (3.02122035 * (10 ** (-4))) * D_Tmrt * D_Tmrt * Pa * Pa * Pa + \
                  (-4.77403547 * (10 ** (-6))) * Ta * D_Tmrt * D_Tmrt * Pa * Pa * Pa + \
                  (1.73825715 * (10 ** (-6))) * va * D_Tmrt * D_Tmrt * Pa * Pa * Pa + \
                  (-4.09087898 * (10 ** (-7))) * D_Tmrt * D_Tmrt * D_Tmrt * Pa * Pa * Pa + \
                  (0.614155345) * Pa * Pa * Pa * Pa + \
                  (-0.0616755931) * Ta * Pa * Pa * Pa * Pa + \
                  (0.00133374846) * Ta * Ta * Pa * Pa * Pa * Pa + \
                  (0.00355375387) * va * Pa * Pa * Pa * Pa + \
                  (-5.13027851 * (10 ** (-4))) * Ta * va * Pa * Pa * Pa * Pa + \
                  (1.02449757 * (10 ** (-4))) * va * va * Pa * Pa * Pa * Pa + \
                  (-0.00148526421) * D_Tmrt * Pa * Pa * Pa * Pa + \
                  (-4.11469183 * (10 ** (-5))) * Ta * D_Tmrt * Pa * Pa * Pa * Pa + \
                  (-6.80434415 * (10 ** (-6))) * va * D_Tmrt * Pa * Pa * Pa * Pa + \
                  (-9.77675906 * (10 ** (-6))) * D_Tmrt * D_Tmrt * Pa * Pa * Pa * Pa + \
                  (0.0882773108) * Pa * Pa * Pa * Pa * Pa + \
                  (-0.00301859306) * Ta * Pa * Pa * Pa * Pa * Pa + \
                  (0.00104452989) * va * Pa * Pa * Pa * Pa * Pa + \
                  (2.47090539 * (10 ** (-4))) * D_Tmrt * Pa * Pa * Pa * Pa * Pa + \
                  (0.00148348065) * Pa * Pa * Pa * Pa * Pa * Pa

    return UTCI_approx


def utci_numpy(temperature_air, temperature_mrt, wind_speed, relative_humidity):
    # Convert to correct units
    delta_temperature = temperature_mrt - temperature_air
    vapour_pressure = saturated_vapour_pressure(temperature_air) * (relative_humidity / 100.0) / 1000.0  # convert vapour pressure to kPa

    utci_approx = temperature_air + 0.607562052 \
                  - 0.0227712343 * temperature_air + \
                  (8.06470249 * (10 ** (-4))) * np.power(temperature_air, 2) + \
                  (-1.54271372 * (10 ** (-4))) * np.power(temperature_air, 3) + \
                  (-3.24651735 * (10 ** (-6))) * np.power(temperature_air, 4) + \
                  (7.32602852 * (10 ** (-8))) * np.power(temperature_air, 5) + \
                  (1.35959073 * (10 ** (-9))) * np.power(temperature_air, 6) + \
                  (-2.25836520) * wind_speed + \
                  0.0880326035 * temperature_air * wind_speed + \
                  0.00216844454 * np.power(temperature_air, 2) * wind_speed + \
                  (-1.53347087 * (10 ** (-5))) * np.power(temperature_air, 3) * wind_speed + \
                  (-5.72983704 * (10 ** (-7))) * np.power(temperature_air, 4) * wind_speed + \
                  (-2.55090145 * (10 ** (-9))) * np.power(temperature_air, 5) * wind_speed + \
                  (-0.751269505) * np.power(wind_speed, 2) + \
                  (-0.00408350271) * temperature_air * np.power(wind_speed, 2) + \
                  (-5.21670675 * (10 ** (-5))) * np.power(temperature_air, 2) * np.power(wind_speed, 2) + \
                  (1.94544667 * (10 ** (-6))) * np.power(temperature_air, 3) * np.power(wind_speed, 2) + \
                  (1.14099531 * (10 ** (-8))) * np.power(temperature_air, 4) * np.power(wind_speed, 2) + \
                  0.158137256 * np.power(wind_speed, 3) + \
                  (-6.57263143 * (10 ** (-5))) * temperature_air * np.power(wind_speed, 3) + \
                  (2.22697524 * (
                          10 ** (-7))) * np.power(temperature_air, 2) * np.power(wind_speed, 3) + \
                  (-4.16117031 * (10 ** (
                      -8))) * np.power(temperature_air, 3) * np.power(wind_speed, 3) + \
                  (-0.0127762753) * np.power(wind_speed, 4) + \
                  (9.66891875 * (10 ** (-6))) * temperature_air * np.power(wind_speed, 4) + \
                  (2.52785852 * (10 ** (
                      -9))) * np.power(temperature_air, 2) * np.power(wind_speed, 4) + \
                  (4.56306672 * (10 ** (-4))) * np.power(wind_speed, 5) + \
                  (-1.74202546 * (10 ** (
                      -7))) * temperature_air * np.power(wind_speed, 5) + \
                  (-5.91491269 * (10 ** (
                      -6))) * np.power(wind_speed, 6) + \
                  (0.398374029) * delta_temperature + \
                  (1.83945314 * (10 ** (-4))) * temperature_air * delta_temperature + \
                  (-1.73754510 * (10 ** (-4))) * np.power(temperature_air, 2) * delta_temperature + \
                  (-7.60781159 * (
                          10 ** (-7))) * np.power(temperature_air, 3) * delta_temperature + \
                  (3.77830287 * (10 ** (
                      -8))) * np.power(temperature_air, 4) * delta_temperature + \
                  (5.43079673 * (10 ** (
                      -10))) * np.power(temperature_air, 5) * delta_temperature + \
                  (-0.0200518269) * wind_speed * delta_temperature + \
                  (8.92859837 * (10 ** (-4))) * temperature_air * wind_speed * delta_temperature + \
                  (3.45433048 * (10 ** (-6))) * np.power(temperature_air, 2) * wind_speed * delta_temperature + \
                  (-3.77925774 * (10 ** (
                      -7))) * np.power(temperature_air, 3) * wind_speed * delta_temperature + \
                  (-1.69699377 * (10 ** (
                      -9))) * np.power(temperature_air, 4) * wind_speed * delta_temperature + \
                  (1.69992415 * (10 ** (-4))) * np.power(wind_speed, 2) * delta_temperature + \
                  (-4.99204314 * (10 ** (-5))) * temperature_air * np.power(wind_speed, 2) * delta_temperature + \
                  (2.47417178 * (10 ** (
                      -7))) * np.power(temperature_air, 2) * np.power(wind_speed, 2) * delta_temperature + \
                  (1.07596466 * (10 ** (
                      -8))) * np.power(temperature_air, 3) * np.power(wind_speed, 2) * delta_temperature + \
                  (8.49242932 * (10 ** (-5))) * np.power(wind_speed, 3) * delta_temperature + \
                  (1.35191328 * (10 ** (
                      -6))) * temperature_air * np.power(wind_speed, 3) * delta_temperature + \
                  (-6.21531254 * (10 ** (
                      -9))) * np.power(temperature_air, 2) * np.power(wind_speed, 3) * delta_temperature + \
                  (-4.99410301 * (10 ** (-6))) * np.power(wind_speed, 4) * delta_temperature + \
                  (-1.89489258 * (10 ** (
                      -8))) * temperature_air * np.power(wind_speed, 4) * delta_temperature + \
                  (8.15300114 * (10 ** (
                      -8))) * np.power(wind_speed, 5) * delta_temperature + \
                  (7.55043090 * (10 ** (-4))) * np.power(delta_temperature, 2) + \
                  (-5.65095215 * (10 ** (-5))) * temperature_air * np.power(delta_temperature, 2) + \
                  (-4.52166564 * (
                          10 ** (-7))) * np.power(temperature_air, 2) * np.power(delta_temperature, 2) + \
                  (2.46688878 * (10 ** (
                      -8))) * np.power(temperature_air, 3) * np.power(delta_temperature, 2) + \
                  (2.42674348 * (10 ** (
                      -10))) * np.power(temperature_air, 4) * np.power(delta_temperature, 2) + \
                  (1.54547250 * (10 ** (-4))) * wind_speed * np.power(delta_temperature, 2) + \
                  (5.24110970 * (10 ** (-6))) * temperature_air * wind_speed * np.power(delta_temperature, 2) + \
                  (-8.75874982 * (10 ** (
                      -8))) * np.power(temperature_air, 2) * wind_speed * np.power(delta_temperature, 2) + \
                  (-1.50743064 * (10 ** (
                      -9))) * np.power(temperature_air, 3) * wind_speed * np.power(delta_temperature, 2) + \
                  (-1.56236307 * (10 ** (-5))) * np.power(wind_speed, 2) * np.power(delta_temperature, 2) + \
                  (-1.33895614 * (10 ** (
                      -7))) * temperature_air * np.power(wind_speed, 2) * np.power(delta_temperature, 2) + \
                  (2.49709824 * (10 ** (
                      -9))) * np.power(temperature_air, 2) * np.power(wind_speed, 2) * np.power(delta_temperature, 2) + \
                  (6.51711721 * (10 ** (
                      -7))) * np.power(wind_speed, 3) * np.power(delta_temperature, 2) + \
                  (1.94960053 * (10 ** (
                      -9))) * temperature_air * np.power(wind_speed, 3) * np.power(delta_temperature, 2) + \
                  (-1.00361113 * (10 ** (
                      -8))) * np.power(wind_speed, 4) * np.power(delta_temperature, 2) + \
                  (-1.21206673 * (10 ** (-5))) * np.power(delta_temperature, 3) + \
                  (-2.18203660 * (10 ** (
                      -7))) * temperature_air * np.power(delta_temperature, 3) + \
                  (7.51269482 * (10 ** (
                      -9))) * np.power(temperature_air, 2) * np.power(delta_temperature, 3) + \
                  (9.79063848 * (10 ** (
                      -11))) * np.power(temperature_air, 3) * np.power(delta_temperature, 3) + \
                  (1.25006734 * (10 ** (-6))) * wind_speed * np.power(delta_temperature, 3) + \
                  (-1.81584736 * (10 ** (
                      -9))) * temperature_air * wind_speed * np.power(delta_temperature, 3) + \
                  (-3.52197671 * (10 ** (
                      -10))) * np.power(temperature_air, 2) * wind_speed * np.power(delta_temperature, 3) + \
                  (-3.36514630 * (10 ** (
                      -8))) * np.power(wind_speed, 2) * np.power(delta_temperature, 3) + \
                  (1.35908359 * (10 ** (
                      -10))) * temperature_air * np.power(wind_speed, 2) * np.power(delta_temperature, 3) + \
                  (4.17032620 * (10 ** (
                      -10))) * np.power(wind_speed, 3) * np.power(delta_temperature, 3) + \
                  (-1.30369025 * (10 ** (
                      -9))) * np.power(delta_temperature, 4) + \
                  (4.13908461 * (10 ** (
                      -10))) * temperature_air * np.power(delta_temperature, 4) + \
                  (9.22652254 * (10 ** (
                      -12))) * np.power(temperature_air, 2) * np.power(delta_temperature, 4) + \
                  (-5.08220384 * (10 ** (
                      -9))) * wind_speed * np.power(delta_temperature, 4) + \
                  (-2.24730961 * (10 ** (
                      -11))) * temperature_air * wind_speed * np.power(delta_temperature, 4) + \
                  (1.17139133 * (10 ** (
                      -10))) * np.power(wind_speed, 2) * np.power(delta_temperature, 4) + \
                  (6.62154879 * (10 ** (
                      -10))) * np.power(delta_temperature, 5) + \
                  (4.03863260 * (10 ** (
                      -13))) * temperature_air * np.power(delta_temperature, 5) + \
                  (1.95087203 * (10 ** (
                      -12))) * wind_speed * np.power(delta_temperature, 5) + \
                  (-4.73602469 * (10 ** (
                      -12))) * np.power(delta_temperature, 6) + \
                  (5.12733497) * vapour_pressure + \
                  (-0.312788561) * temperature_air * vapour_pressure + \
                  (-0.0196701861) * np.power(temperature_air, 2) * vapour_pressure + \
                  (9.99690870 * (10 ** (-4))) * np.power(temperature_air, 3) * vapour_pressure + \
                  (9.51738512 * (10 ** (
                      -6))) * np.power(temperature_air, 4) * vapour_pressure + \
                  (-4.66426341 * (10 ** (
                      -7))) * np.power(temperature_air, 5) * vapour_pressure + \
                  (0.548050612) * wind_speed * vapour_pressure + \
                  (-0.00330552823) * temperature_air * wind_speed * vapour_pressure + \
                  (-0.00164119440) * np.power(temperature_air, 2) * wind_speed * vapour_pressure + \
                  (-5.16670694 * (10 ** (
                      -6))) * np.power(temperature_air, 3) * wind_speed * vapour_pressure + \
                  (9.52692432 * (10 ** (
                      -7))) * np.power(temperature_air, 4) * wind_speed * vapour_pressure + \
                  (-0.0429223622) * np.power(wind_speed, 2) * vapour_pressure + \
                  (0.00500845667) * temperature_air * np.power(wind_speed, 2) * vapour_pressure + \
                  (1.00601257 * (10 ** (
                      -6))) * np.power(temperature_air, 2) * np.power(wind_speed, 2) * vapour_pressure + \
                  (-1.81748644 * (10 ** (
                      -6))) * np.power(temperature_air, 3) * np.power(wind_speed, 2) * vapour_pressure + \
                  (-1.25813502 * (10 ** (-3))) * np.power(wind_speed, 3) * vapour_pressure + \
                  (-1.79330391 * (
                          10 ** (-4))) * temperature_air * np.power(wind_speed, 3) * vapour_pressure + \
                  (2.34994441 * (10 ** (
                      -6))) * np.power(temperature_air, 2) * np.power(wind_speed, 3) * vapour_pressure + \
                  (1.29735808 * (10 ** (-4))) * np.power(wind_speed, 4) * vapour_pressure + \
                  (1.29064870 * (10 ** (
                      -6))) * temperature_air * np.power(wind_speed, 4) * vapour_pressure + \
                  (-2.28558686 * (10 ** (
                      -6))) * np.power(wind_speed, 5) * vapour_pressure + \
                  (-0.0369476348) * delta_temperature * vapour_pressure + \
                  (0.00162325322) * temperature_air * delta_temperature * vapour_pressure + \
                  (-3.14279680 * (
                          10 ** (-5))) * np.power(temperature_air, 2) * delta_temperature * vapour_pressure + \
                  (2.59835559 * (10 ** (
                      -6))) * np.power(temperature_air, 3) * delta_temperature * vapour_pressure + \
                  (-4.77136523 * (10 ** (
                      -8))) * np.power(temperature_air, 4) * delta_temperature * vapour_pressure + \
                  (8.64203390 * (10 ** (-3))) * wind_speed * delta_temperature * vapour_pressure + \
                  (-6.87405181 * (10 ** (-4))) * temperature_air * wind_speed * delta_temperature * vapour_pressure + \
                  (-9.13863872 * (10 ** (
                      -6))) * np.power(temperature_air, 2) * wind_speed * delta_temperature * vapour_pressure + \
                  (5.15916806 * (10 ** (
                      -7))) * np.power(temperature_air, 3) * wind_speed * delta_temperature * vapour_pressure + \
                  (-3.59217476 * (10 ** (-5))) * np.power(wind_speed, 2) * delta_temperature * vapour_pressure + \
                  (3.28696511 * (10 ** (
                      -5))) * temperature_air * np.power(wind_speed, 2) * delta_temperature * vapour_pressure + \
                  (-7.10542454 * (10 ** (
                      -7))) * np.power(temperature_air, 2) * np.power(wind_speed,
                                                                      2) * delta_temperature * vapour_pressure + \
                  (-1.24382300 * (10 ** (
                      -5))) * np.power(wind_speed, 3) * delta_temperature * vapour_pressure + \
                  (-7.38584400 * (10 ** (
                      -9))) * temperature_air * np.power(wind_speed, 3) * delta_temperature * vapour_pressure + \
                  (2.20609296 * (10 ** (
                      -7))) * np.power(wind_speed, 4) * delta_temperature * vapour_pressure + \
                  (-7.32469180 * (10 ** (-4))) * np.power(delta_temperature, 2) * vapour_pressure + \
                  (-1.87381964 * (
                          10 ** (-5))) * temperature_air * np.power(delta_temperature, 2) * vapour_pressure + \
                  (4.80925239 * (10 ** (
                      -6))) * np.power(temperature_air, 2) * np.power(delta_temperature, 2) * vapour_pressure + \
                  (-8.75492040 * (10 ** (
                      -8))) * np.power(temperature_air, 3) * np.power(delta_temperature, 2) * vapour_pressure + \
                  (2.77862930 * (10 ** (-5))) * wind_speed * np.power(delta_temperature, 2) * vapour_pressure + \
                  (-5.06004592 * (10 ** (
                      -6))) * temperature_air * wind_speed * np.power(delta_temperature, 2) * vapour_pressure + \
                  (1.14325367 * (10 ** (
                      -7))) * np.power(temperature_air, 2) * wind_speed * np.power(delta_temperature,
                                                                                   2) * vapour_pressure + \
                  (2.53016723 * (10 ** (
                      -6))) * np.power(wind_speed, 2) * np.power(delta_temperature, 2) * vapour_pressure + \
                  (-1.72857035 * (10 ** (
                      -8))) * temperature_air * np.power(wind_speed, 2) * np.power(delta_temperature,
                                                                                   2) * vapour_pressure + \
                  (-3.95079398 * (10 ** (
                      -8))) * np.power(wind_speed, 3) * np.power(delta_temperature, 2) * vapour_pressure + \
                  (-3.59413173 * (10 ** (
                      -7))) * np.power(delta_temperature, 3) * vapour_pressure + \
                  (7.04388046 * (10 ** (
                      -7))) * temperature_air * np.power(delta_temperature, 3) * vapour_pressure + \
                  (-1.89309167 * (10 ** (
                      -8))) * np.power(temperature_air, 2) * np.power(delta_temperature, 3) * vapour_pressure + \
                  (-4.79768731 * (10 ** (
                      -7))) * wind_speed * np.power(delta_temperature, 3) * vapour_pressure + \
                  (7.96079978 * (10 ** (
                      -9))) * temperature_air * wind_speed * np.power(delta_temperature, 3) * vapour_pressure + \
                  (1.62897058 * (10 ** (
                      -9))) * np.power(wind_speed, 2) * np.power(delta_temperature, 3) * vapour_pressure + \
                  (3.94367674 * (10 ** (
                      -8))) * np.power(delta_temperature, 4) * vapour_pressure + \
                  (-1.18566247 * (10 ** (
                      -9))) * temperature_air * np.power(delta_temperature, 4) * vapour_pressure + \
                  (3.34678041 * (10 ** (
                      -10))) * wind_speed * np.power(delta_temperature, 4) * vapour_pressure + \
                  (-1.15606447 * (10 ** (
                      -10))) * np.power(delta_temperature, 5) * vapour_pressure + \
                  (-2.80626406) * np.power(vapour_pressure, 2) + \
                  (0.548712484) * temperature_air * np.power(vapour_pressure, 2) + \
                  (-0.00399428410) * np.power(temperature_air, 2) * np.power(vapour_pressure, 2) + \
                  (-9.54009191 * (10 ** (
                      -4))) * np.power(temperature_air, 3) * np.power(vapour_pressure, 2) + \
                  (1.93090978 * (10 ** (
                      -5))) * np.power(temperature_air, 4) * np.power(vapour_pressure, 2) + \
                  (-0.308806365) * wind_speed * np.power(vapour_pressure, 2) + \
                  (0.0116952364) * temperature_air * wind_speed * np.power(vapour_pressure, 2) + \
                  (4.95271903 * (10 ** (
                      -4))) * np.power(temperature_air, 2) * wind_speed * np.power(vapour_pressure, 2) + \
                  (-1.90710882 * (10 ** (
                      -5))) * np.power(temperature_air, 3) * wind_speed * np.power(vapour_pressure, 2) + \
                  (0.00210787756) * np.power(wind_speed, 2) * np.power(vapour_pressure, 2) + \
                  (-6.98445738 * (10 ** (
                      -4))) * temperature_air * np.power(wind_speed, 2) * np.power(vapour_pressure, 2) + \
                  (2.30109073 * (10 ** (
                      -5))) * np.power(temperature_air, 2) * np.power(wind_speed, 2) * np.power(vapour_pressure, 2) + \
                  (4.17856590 * (
                          10 ** (-4))) * np.power(wind_speed, 3) * np.power(vapour_pressure, 2) + \
                  (-1.27043871 * (10 ** (
                      -5))) * temperature_air * np.power(wind_speed, 3) * np.power(vapour_pressure, 2) + \
                  (-3.04620472 * (10 ** (
                      -6))) * np.power(wind_speed, 4) * np.power(vapour_pressure, 2) + \
                  (0.0514507424) * delta_temperature * np.power(vapour_pressure, 2) + \
                  (-0.00432510997) * temperature_air * delta_temperature * np.power(vapour_pressure, 2) + \
                  (8.99281156 * (10 ** (
                      -5))) * np.power(temperature_air, 2) * delta_temperature * np.power(vapour_pressure, 2) + \
                  (-7.14663943 * (10 ** (
                      -7))) * np.power(temperature_air, 3) * delta_temperature * np.power(vapour_pressure, 2) + \
                  (-2.66016305 * (10 ** (-4))) * wind_speed * delta_temperature * np.power(vapour_pressure, 2) + \
                  (2.63789586 * (10 ** (
                      -4))) * temperature_air * wind_speed * delta_temperature * np.power(vapour_pressure, 2) + \
                  (-7.01199003 * (10 ** (
                      -6))) * np.power(temperature_air, 2) * wind_speed * delta_temperature * np.power(vapour_pressure,
                                                                                                       2) + \
                  (-1.06823306 * (10 ** (
                      -4))) * np.power(wind_speed, 2) * delta_temperature * np.power(vapour_pressure, 2) + \
                  (3.61341136 * (10 ** (
                      -6))) * temperature_air * np.power(wind_speed, 2) * delta_temperature * np.power(vapour_pressure,
                                                                                                       2) + \
                  (2.29748967 * (10 ** (
                      -7))) * np.power(wind_speed, 3) * delta_temperature * np.power(vapour_pressure, 2) + \
                  (3.04788893 * (
                          10 ** (-4))) * np.power(delta_temperature, 2) * np.power(vapour_pressure, 2) + \
                  (-6.42070836 * (10 ** (
                      -5))) * temperature_air * np.power(delta_temperature, 2) * np.power(vapour_pressure, 2) + \
                  (1.16257971 * (10 ** (
                      -6))) * np.power(temperature_air, 2) * np.power(delta_temperature, 2) * np.power(vapour_pressure,
                                                                                                       2) + \
                  (7.68023384 * (10 ** (
                      -6))) * wind_speed * np.power(delta_temperature, 2) * np.power(vapour_pressure, 2) + \
                  (-5.47446896 * (10 ** (
                      -7))) * temperature_air * wind_speed * np.power(delta_temperature, 2) * np.power(vapour_pressure,
                                                                                                       2) + \
                  (-3.59937910 * (10 ** (
                      -8))) * np.power(wind_speed, 2) * np.power(delta_temperature, 2) * np.power(vapour_pressure, 2) + \
                  (-4.36497725 * (10 ** (
                      -6))) * np.power(delta_temperature, 3) * np.power(vapour_pressure, 2) + \
                  (1.68737969 * (10 ** (
                      -7))) * temperature_air * np.power(delta_temperature, 3) * np.power(vapour_pressure, 2) + \
                  (2.67489271 * (10 ** (
                      -8))) * wind_speed * np.power(delta_temperature, 3) * np.power(vapour_pressure, 2) + \
                  (3.23926897 * (10 ** (
                      -9))) * np.power(delta_temperature, 4) * np.power(vapour_pressure, 2) + \
                  (-0.0353874123) * np.power(vapour_pressure, 3) + \
                  (-0.221201190) * temperature_air * np.power(vapour_pressure, 3) + \
                  (
                      0.0155126038) * np.power(temperature_air, 2) * np.power(vapour_pressure, 3) + \
                  (-2.63917279 * (10 ** (
                      -4))) * np.power(temperature_air, 3) * np.power(vapour_pressure, 3) + \
                  (0.0453433455) * wind_speed * np.power(vapour_pressure, 3) + \
                  (
                      -0.00432943862) * temperature_air * wind_speed * np.power(vapour_pressure, 3) + \
                  (1.45389826 * (10 ** (
                      -4))) * np.power(temperature_air, 2) * wind_speed * np.power(vapour_pressure, 3) + \
                  (2.17508610 * (10 ** (
                      -4))) * np.power(wind_speed, 2) * np.power(vapour_pressure, 3) + \
                  (-6.66724702 * (10 ** (
                      -5))) * temperature_air * np.power(wind_speed, 2) * np.power(vapour_pressure, 3) + \
                  (3.33217140 * (10 ** (
                      -5))) * np.power(wind_speed, 3) * np.power(vapour_pressure, 3) + \
                  (-0.00226921615) * delta_temperature * np.power(vapour_pressure, 3) + \
                  (3.80261982 * (10 ** (
                      -4))) * temperature_air * delta_temperature * np.power(vapour_pressure, 3) + \
                  (-5.45314314 * (10 ** (
                      -9))) * np.power(temperature_air, 2) * delta_temperature * np.power(vapour_pressure, 3) + \
                  (-7.96355448 * (10 ** (
                      -4))) * wind_speed * delta_temperature * np.power(vapour_pressure, 3) + \
                  (2.53458034 * (10 ** (
                      -5))) * temperature_air * wind_speed * delta_temperature * np.power(vapour_pressure, 3) + \
                  (-6.31223658 * (10 ** (
                      -6))) * np.power(wind_speed, 2) * delta_temperature * np.power(vapour_pressure, 3) + \
                  (3.02122035 * (10 ** (
                      -4))) * np.power(delta_temperature, 2) * np.power(vapour_pressure, 3) + \
                  (-4.77403547 * (10 ** (
                      -6))) * temperature_air * np.power(delta_temperature, 2) * np.power(vapour_pressure, 3) + \
                  (1.73825715 * (10 ** (
                      -6))) * wind_speed * np.power(delta_temperature, 2) * np.power(vapour_pressure, 3) + \
                  (-4.09087898 * (10 ** (
                      -7))) * np.power(delta_temperature, 3) * np.power(vapour_pressure, 3) + \
                  (0.614155345) * np.power(vapour_pressure, 4) + \
                  (
                      -0.0616755931) * temperature_air * np.power(vapour_pressure, 4) + \
                  (
                      0.00133374846) * np.power(temperature_air, 2) * np.power(vapour_pressure, 4) + \
                  (0.00355375387) * wind_speed * np.power(vapour_pressure, 4) + \
                  (-5.13027851 * (10 ** (
                      -4))) * temperature_air * wind_speed * np.power(vapour_pressure, 4) + \
                  (1.02449757 * (10 ** (
                      -4))) * np.power(wind_speed, 2) * np.power(vapour_pressure, 4) + \
                  (
                      -0.00148526421) * delta_temperature * np.power(vapour_pressure, 4) + \
                  (-4.11469183 * (10 ** (
                      -5))) * temperature_air * delta_temperature * np.power(vapour_pressure, 4) + \
                  (-6.80434415 * (10 ** (
                      -6))) * wind_speed * delta_temperature * np.power(vapour_pressure, 4) + \
                  (-9.77675906 * (10 ** (
                      -6))) * np.power(delta_temperature, 2) * np.power(vapour_pressure, 4) + \
                  (
                      0.0882773108) * np.power(vapour_pressure, 5) + \
                  (
                      -0.00301859306) * temperature_air * np.power(vapour_pressure, 5) + \
                  (
                      0.00104452989) * wind_speed * np.power(vapour_pressure, 5) + \
                  (2.47090539 * (10 ** (
                      -4))) * delta_temperature * np.power(vapour_pressure, 5) + \
                  (
                      0.00148348065) * np.power(vapour_pressure, 6)

    return utci_approx


def saturated_vapour_pressure(temperature: float) -> float:
    """
    Computes the saturated vapour pressure for a given temperature.
    Source: Peuhkuri, Ruut, and Carsten Rode. 2016.
    ???Heat and Mass Transfer in Buildings.???

    :param temperature: Temperature in Celsius
    :type temperature: float
    :return: Vapour pressure in Pa
    :rtype: float
    """

    return 288.68 * (1.098 + temperature / 100) ** 8.02
