#!/usr/bin/env python3

import os

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    nombre, salida = input("Entrada: "), input("Salida: ")
    archivoSalida = 0

    if os.path.isfile(salida):
        os.remove(salida)
        archivoSalida = open(salida, 'x')
    else:
        archivoSalida = open(salida, 'x')


    if not os.path.isfile(nombre):
        print("El archivo de entrada no existe.")
    else:
        archivo = open(nombre, 'r')
        numero = int(archivo.read())
        archivoSalida.write(str(fib(numero)) + "\n")
        archivo.close()
        archivoSalida.close()
