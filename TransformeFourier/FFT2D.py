import cmath
import TransformeFourier.FFT as FFT

def usual(tab):
    I = len(tab)
    J = len(tab[0])
    #print(tab[0])
    for i in range(I):
        tab[i]=FFT.usual(tab[i])
    
    tab = transpose(tab)
    for i in range(J):
        tab[i]=FFT.usual(tab[i])
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
        tab[i]=FFT.inverse(tab[i])
    tab = transpose(tab)
    for i in range(J):
        tab[i]=FFT.inverse(tab[i])
    tab = transpose(tab)
    return tab