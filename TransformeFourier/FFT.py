
import cmath
from numpy import conjugate


def usual(tab):
    N = len(tab)
    if N <= 1:
        return tab
    even = usual(tab[0::2])
    odd = usual(tab[1::2])

    tab2 = [cmath.exp(-2j * cmath.pi * k  / N) * odd[k%(N//2)] for k in range(N)]
    
    return [even[k%(N//2)]+tab2[k] for k in range(N)]

def inverse(tab):
    N = len(tab)
    if N <= 1:
        return tab
    if not hasattr(inverse, "lenOfFirstTab"):
        inverse.lenOfFirstTab = N
    even = inverse(tab[0::2])
    odd = inverse(tab[1::2])

    tab2 = [cmath.exp(2j * cmath.pi * k  / N) * odd[k%(N//2)] for k in range(N)]
    
    if len(tab) == inverse.lenOfFirstTab:
        delattr(inverse,"lenOfFirstTab")
        return [ ((1 / len(tab)) * (even[k % (N//2) ] + tab2[k])) for k in range(N)]
    else:
        return [ (even[k % (N//2) ] + tab2[k]) for k in range(N)]




