#!/usr/bin/env python3

import random
from time import time

def arrayAleatorio(array, tam):
    for x in range (0, tam):
        array[x] = random.randint(0, 100)

    return array

def burbuja(array):
    for passnum in range(len(array)-1,0,-1):
        for i in range(passnum):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

def insercion(array):
   for index in range(1, len(array)):

     currentvalue = array[index]
     position = index

     while position > 0 and array[position-1] > currentvalue:
         array[position] = array[position-1]
         position = position-1

     array[position] = currentvalue

def seleccion(array):
   for fillslot in range(len(array)-1, 0, -1):
       positionOfMax = 0
       for location in range(1, fillslot + 1):
           if array[location] > array[positionOfMax]:
               positionOfMax = location

       temp = array[fillslot]
       array[fillslot] = array[positionOfMax]
       array[positionOfMax] = temp

def quickSort(array):
   quickSortHelper(array, 0, len(array)-1)

def quickSortHelper(array, first, last):
   if first < last:

       splitpoint = partition(array,first,last)

       quickSortHelper(array, first, splitpoint-1)
       quickSortHelper(array, splitpoint+1, last)


def partition(array,first,last):
   pivotvalue = array[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       while leftmark <= rightmark and array[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while array[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = array[leftmark]
           array[leftmark] = array[rightmark]
           array[rightmark] = temp

   temp = array[first]
   array[first] = array[rightmark]
   array[rightmark] = temp


   return rightmark

if __name__ == '__main__':
    tam = 5000

    array = [0] * tam

    array = arrayAleatorio(array, tam)
    inicio = time()
    burbuja(array)
    fin = time()
    #print("Burbuja:\t", array)
    print("Burbuja: ", fin - inicio)

    array = arrayAleatorio(array, 15)
    inicio = time()
    insercion(array)
    fin = time()
    #print("Inserción:\t", array)
    print("Inserción: ", fin - inicio)

    array = arrayAleatorio(array, 15)
    inicio = time()
    seleccion(array)
    fin = time()
    #print("Selección:\t", array)
    print("Selección: ", fin - inicio)

    array = arrayAleatorio(array, 15)
    inicio = time()
    quickSort(array)
    fin = time()
    #print("QuickSort:\t", array)
    print("QuickSort: ", fin - inicio)