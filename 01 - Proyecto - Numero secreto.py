# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 13:10:14 2020

@author: mcamargo / iturco
"""

''' El Juego del Número Secreto consiste en lo siguiente: la computadora tiene
un número guardado (que el jugador obviamente no conoce) y el jugador debe 
tratar de adivinarlo. Si lo logra, gana el juego y la computadora le avisa en 
cuántos intentos lo hizo. Si no lo logra en cierta cantidad predefinida 
intentos, el juego termina y se le avisa al jugador ha perdido. La cantidad
máxima de intentos que el jugador tendrá a su disposición es un número que 
debe cargarse por teclado antes de comenzar a jugar, al igual que el límite 
derecho del intervalo que contendrá al número secreto elegido por el computador
 (es decir, el usuario debe poder indicar el número estará entre 1 y 30 o bien
 entre 1 y 50 o bien en el intervalo que el propio usuario decida). 
'''
# Librerias
import random

# Variables
intentos = 0
limite_izquierdo = 1
bandera_encontrado = False

# Titulo
print('*'*62)
print('*','Tecnicatura en Ciencias de DATOS e Inteligencia Artificial','*')
print('** ','\t\t\t  El JUEGO del numero SECRETO  \t\t\t','   **')
print('*'*62)

#Entrada de datos
print('Configuracion inicial:')
limite_derecho = int(input('El numero secreto va 1 a ... (ingrese un valor): '))
cant_intentos = int(input('Ingrese la cantidad de intentos permitidos: '))

# Procesos
numero_secreto = random.randint(limite_izquierdo,limite_derecho)
while not bandera_encontrado and intentos < cant_intentos:
    intentos += 1
    print('\nEl numero se encuentra entre ',limite_izquierdo,' y ',limite_derecho)
    numero = -1
    while numero <limite_izquierdo or numero > limite_derecho:
        numero = int(input('[Intento: '+ str(intentos) + '] => Ingrese un numero: '))
        if numero < limite_izquierdo or numero > limite_derecho:
            print('ERROR... debe elegir un numero entre', limite_izquierdo,' y ',
                  limite_derecho,'...')
    if numero == numero_secreto:
        bandera_encontrado = True
    elif numero > numero_secreto:
        limite_derecho = numero
    else:
        limite_izquierdo = numero

# Salida
if bandera_encontrado:
    print('\nGenio, Idolo!!!. Adivinastes el numero en ',intentos,' intentos')
else:
    print('\nLo siento!!!. Se acabaron los intentos.\nEl numero era: ',numero_secreto)

print('\nMuchas gracias por JUGAR!!!')
print('\nRealizado por: \nGrupo 8: Camargo, Maximiliano Jose / Turco, Irene Cecilia')