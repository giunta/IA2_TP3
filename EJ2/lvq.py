#
# 12/06/19
#
#
#
#
#

import math
import numpy as np
from matplotlib.pyplot import imshow
from dataset_abc import genera_data
from dataset_abc import dataset_size


NEURONAS_ENTRADA = 28*28
MAPA_X = 10
MAPA_Y = 10
MAPA_Z = NEURONAS_ENTRADA
NEURONAS_MAPA = MAPA_X*MAPA_Y
PORC_EJ_TEST = 0.1
EPOCHS = 1
ALFA = 0.05

Wijk = np.zeros([MAPA_X, MAPA_Y, MAPA_Z])
Wentrada  = np.zeros(MAPA_Z)
Wmapa = np.zeros(MAPA_Z)
mapa = np. zeros([MAPA_X, MAPA_X])

labels, dataset = genera_data()

CANT_EJ = dataset_size()
CANT_EJ_TEST = int(CANT_EJ * PORC_EJ_TEST)
CANT_EJ_TRAINING = CANT_EJ - CANT_EJ_TEST

def calculo_metrica(Wentrada, Wmapa):
    # Calcula la distancia euclideana entre 2 vectores de pesos

    d_euclideana = 0
    dist = 0
    for k in range(0, MAPA_Z):
        dist += pow(Wentrada[k] - Wmapa[k], 2)
    d_euclideana = pow(dist, 0.5)
    return d_euclideana

def comparacion(Wentrada, Wijk):
    # Obtiene la neurona más próxima a la entrada

    min_x = 0
    min_y = 0
    distancias = np.zeros([MAPA_X, MAPA_Y])
    for i in range(0, MAPA_X):
        for j in range(0, MAPA_Y):
            Wmapa = Wijk[i][j][:]
            distancias[i][j] = calculo_metrica(Wentrada, Wmapa)
    min_distance = distancias[min_x][min_y]
    for i in range(0, MAPA_X):
        for j in range(0, MAPA_Y):
            if distancias[i][j] < min_distance:
                min_distance = distancias[i][j]
                min_x = i
                min_y = j
    return min_x, min_y

def aprendizaje(Wentrada, Wijk):
    # Modifica los pesos de la neurona más adecuada a la entrada y los de las neuronas
    # inmediatas a ella

    min_x, min_y = comparacion(Wentrada, Wijk)
    for i in range(min_x - 1, min_x + 2):
        for j in range(min_y - 1, min_y + 2):
            if i>=0 and i<MAPA_X and j>=0 and j<MAPA_Y:
                for k in range(0, NEURONAS_ENTRADA):
                    Wijk[i][j][k] += ALFA*pow(pow(Wentrada[k] - Wijk[i][j][k], 2), 0.5)
    return Wijk, min_x, min_y

#MAIN--------------------------------------------------------------------------------

for e in range(0, EPOCHS):
    for mu in range(0, CANT_EJ_TRAINING):
        Wentrada = dataset[mu][:]
        Wijk, min_x, min_y = aprendizaje(Wentrada, Wijk)
        mapa[min_x, min_y] += 1
        


imshow(mapa)