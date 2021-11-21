import cmath
import numpy as np
import matplotlib.image as img
import TransformeFourier.FTD1D as tfd1d


def usual(tab):
    I = len(tab)
    J = len(tab[0])
    for i in range(I):
        tab[i]=tfd1d.usual(tab[i])
    tab = transpose(tab)
    for i in range(J):
        tab[i]=tfd1d.usual(tab[i])
    tab = transpose(tab)
    return tab
    
def transpose(tab):
    I = len(tab)
    J = len(tab[0])
    tab2 = [[0 for i in range(I)] for j in range(J)]
    for i in range(I):
        for j in range(J):
            tab2[j][i] = tab[i][j]
    return tab2

def inverse(tab):
    I = len(tab)
    J = len(tab[0])
    for i in range(I):
        tab[i]=tfd1d.inverse(tab[i])
    tab = transpose(tab)
    for i in range(J):
        tab[i]=tfd1d.inverse(tab[i])
    tab = transpose(tab)
    return tab
