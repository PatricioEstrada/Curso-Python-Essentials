# -*- coding: utf-8 -*-
# Date: 2021-11-01
# @autor: Patricio Estrada

import numpy as np
import pandas as pd

Datos_2021 = [15, 20, 3, 91, 4, 5, 6, 7, 100, 91, 110, 900, 21, 33, 32, 2, 4, 8, 10, 13, 13, 16, 15, 1302]

par = []
impar = []

for j in Datos_2021:
    if j % 2 == 0:
        par.append(j)
    else:
        impar.append(j)


print(f'Los números de la lista Datos_2021 que son pares son: {par}')
print(f'Los números de la lista Datos_2021 que son impares son: {impar}')

aux = pd.Series(Datos_2021)
# Formula datos atipicos por encima de Q_3 + 1.5 RIQ y por debajo de Q_1 - 1.5 * RIQ
# RIQ = Q_3 - Q_1
out = aux[~aux.between(aux.quantile(0.25) - 1.5*(aux.quantile(0.75)-aux.quantile(0.25)), aux.quantile(0.75) + 1.5*(aux.quantile(0.75) - aux.quantile(0.25)))]
out = list(out)

print(f'Los valores atípicos de la lista Datos_2021 son: {out}')