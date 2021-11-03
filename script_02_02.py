# -*- coding: utf-8 -*-
# Date: 2021-11-01
# @autor: Patricio Estrada

import string

con1 = ['a', 'b', 'c' ,'d', 'e', 'f', 'g', 'h', 'i', 'j']
con2 = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
con3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
con4 = ['$', '%', '*', '@']

valid = False
valid1 = False
valid2 = False
valid3 = False
valid4 = False

while valid == False:
    contrasena = input('Ingrese su contraseña: ')

    letras = set(contrasena)
    if len(contrasena) > 4 and len(contrasena) < 16:
        for c1 in con1:
            if c1 in letras:
                valid1 = True
                break

        if valid1 == False:
            print('La contraseña indicada debe contener al menos uno de los siguientes caracteres:', ' '.join(con1))

        for c2 in con2:
            if c2 in letras:
                valid2 = True
                break
        
        if valid2 == False:
            print('La contraseña indicada debe contener al menos uno de los siguientes caracteres:', ' '.join(con2))

        for c3 in con3:
            if c3 in letras:
                valid3 = True
                break
        
        if valid3 == False:
            print('La contraseña indicada debe contener al menos uno de los siguientes caracteres:', ' '.join(con3))
        
        for c4 in con4:
            if c4 in letras:
                valid4 = True
                break
        
        if valid4 == False:
            print('La contraseña indicada debe contener al menos uno de los siguientes caracteres:', ' '.join(con4))
        
        if valid1 and valid2 and valid3 and valid4:
            valid = True
        
        else:
            valid1 = False
            valid2 = False
            valid3 = False
            valid4 = False

    else:
        print('Longitud de contraseña incorrecta. Escriba una contraseña de mínimo 5 caracteres y máximo 15 caracteres')

print('Contraseña correcta')