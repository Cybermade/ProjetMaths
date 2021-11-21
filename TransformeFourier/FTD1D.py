import cmath


def usual(tab):
    N = len(tab)
    tab2 = [0] * N

    for n in range(0, N):
        for k in range(0, N):
            tab2[n] = tab2[n] + tab[k] * cmath.exp(-2 * 1j * cmath.pi * n * (k / N))
    return tab2


def inverse(tab):
    N = len(tab)
    tab2 = [0] * N

    for n in range(0, N):
        for k in range(0, N):
            tab2[n] = tab2[n] + (tab[k] * cmath.exp((2 * 1j * cmath.pi * n * (k / N)))) / N
    return tab2
