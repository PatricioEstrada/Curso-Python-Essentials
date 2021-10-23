# -*- coding: utf-8 -*-
# Date: 2021-10-22
# @autor: Patricio Estrada

print('Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:')

list = ['Primera', 'Segunda', 'Tercera', 'Cuarta', 'Quinta']

for i in list:
    var = input(f'{i} Interacción, ingrese un valor cualquiera:')
    print(f'Este tipo de dato en Python es: \n {type(var)}')

print('¡YA NO SE HARÁN MÁS INTERACCIONES!')