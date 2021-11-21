import cmath
import numpy as np
import matplotlib.image as img
import TransformeFourier.FTD1D as tfd1d


def usual2(input_img):
    img_out = img.imread(input_img)
    shape = np.array(img_out).shape

    M = shape[0]
    N = shape[1]

    for u in range(0, M):
        for v in range(0, M):
            res = np.zeros((M, N, 3), dtype=np.complex128)
            for x in range(0, M):
                for y in range(0, N):
                    n1 = x * u
                    n2 = y * v
                    coeff = n1 / M + n2 / N
                    res = res + img_out[y + M * x] * cmath.exp((-2 * cmath.pi * 1j * coeff))
    return img_out

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