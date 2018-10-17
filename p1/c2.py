#!/usr/bin/env python3

import random
import os
import time

class JuegoDeLaVida:
    def __init__(self, filas, columnas, linea):
        self.filas = filas
        self.columnas = columnas

        self.matriz = [[0 for x in range(self.columnas)] for y in range(self.filas)]

        if linea == 0:
            for x in range (0, self.filas):
                for y in range (0, self.columnas):
                    if random.randint(0,2) == 1:
                        self.matriz[x][y] = 1

        if linea == 1:
            for y in range (0+1, self.columnas-1):
                self.matriz[int(filas/2)][y] = 1

            for y in range (0+1, self.columnas-1):
                self.matriz[int(filas/4)*3][y] = 1

            for y in range (0+1, self.columnas-1):
                self.matriz[int(filas/4)][y] = 1

    def __str__(self):
        tablero = ''
        for x in range (0, self.filas):
            for y in range (0, self.columnas):
                if self.matriz[x][y] == 1:
                    tablero += '⌂'
                else:
                    tablero += '~'
            tablero += '\n'

        return tablero

    def comprobarVecinos(self, x, y):
        contador = 0

        if x-1 >= 0 and y-1 >= 0:
            if self.matriz[x-1][y-1] == 1:
                contador += 1

        if x-1 >= 0:
            if self.matriz[x-1][y] == 1:
                contador += 1

        if x-1 >= 0 and y+1 < self.columnas:
            if self.matriz[x-1][y+1] == 1:
                contador += 1

        if y-1 >= 0:
            if self.matriz[x][y-1] == 1:
                contador += 1

        if y+1 < self.columnas:
            if self.matriz[x][y+1] == 1:
                contador += 1

        if x+1 < self.filas and y-1 >= 0:
            if self.matriz[x+1][y-1] == 1:
                contador += 1

        if x+1 < self.filas:
            if self.matriz[x+1][y] == 1:
                contador += 1

        if x+1 < self.filas and y+1 < self.columnas:
            if self.matriz[x+1][y+1] == 1:
                contador += 1

        return contador

    def obtenerCasilla(self, x, y):
        return self.matriz[x][y]

    def interaccion(self):
        matriz_copy = [[0 for x in range(self.columnas)] for y in range(self.filas)]

        for x in range (0, self.filas):
            for y in range (0, self.columnas):
                vecinos = self.comprobarVecinos(x, y)
                if self.matriz[x][y] == 0:
                    if vecinos == 3:
                        matriz_copy[x][y] = 1
                    else:
                        matriz_copy[x][y] = 0
                else:
                    if vecinos == 2 or vecinos == 3:
                        matriz_copy[x][y] = 1
                    else:
                        matriz_copy[x][y] = 0
        
        self.matriz = matriz_copy


if __name__ == '__main__':
    filas, columnas, linea = input("Filas: "), input("Columnas: "), input("Linea (0-1): ")

    tiempo = input("Tiempo: ")

    juego = JuegoDeLaVida(int(filas), int(columnas), int(linea))

    iteraciones = 0

    while True:
        os.system("clear")
        print(juego)
        juego.interaccion()
        iteraciones += 1
        print("Iteraciones: " + str(iteraciones))
        time.sleep(float(tiempo))