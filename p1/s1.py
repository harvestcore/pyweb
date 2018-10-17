#!/usr/bin/env python3

import random
import os

if __name__ == '__main__':
    rmin = 0
    rmax = 101

    numero = random.randint(rmin, rmax)
    x = 1

    os.system("clear")

    while x < 11:
        entrada = input("Introduce un número: ")
        entrada = int(entrada)
        
        if entrada > numero:
            print("El número es menor.\n")
        elif entrada < numero:
            print("El número es mayor.\n")
        else:
            print("\nEnhorabuena, has encontrado el número.")
            x = 11
        
        x += 1

    if x == 11:
        print("\nFin del juego, no lograste encontrar el número.")

