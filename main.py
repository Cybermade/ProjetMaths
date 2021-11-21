import TransformeFourier.FTD1D as tfd1d
import TransformeFourier.FTD2D as tfd2d
import TransformeFourier.FFT as FFT
import TransformeFourier.FFT2D as FFT2D
import copy
import matplotlib.image as img
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy

if __name__ == '__main__':
    # Transformé 1D direct
    tab1DD = [12, 45,20,30,42,123,3841,123,43,219,4312,1232,76,24,87,996]  # exemple de tableau 1d
    tab2DD = [[13, 5,980,20,3,23,341,63,78,29,432,932,778,36,70,1000],
    [1, 5,2,3,42,23,31,13,43,19,412,122,7,4,8744,94296]]# exemple de tableau 2d
    tab1DF = tab1DD.copy()
    tab2DF = tab2DD.copy()
    
    tabFTD = tfd1d.inverse(tfd1d.usual(tab1DD)) # transformée de fourier sur un exemple puis inverse pour retomber sur l'exemple
    tabFFT = FFT.inverse(FFT.usual(tab1DF)) # transformée de fourier rapide sur un exemple puis inverse pour retomber sur l'exemple
    
    
    tabFTD2 = tfd2d.inverse(tfd2d.usual(tab2DD))
    tabFFT2 = FFT2D.inverse(FFT2D.usual(tab2DF)) # transform

    for i in range(len(tabFTD)):
        tabFTD[i]=round(tabFTD[i].real,2)+round(tabFTD[i].imag,2)*1j
    
    for i in range(len(tabFFT)):
        tabFFT[i]=round(tabFFT[i].real,2)+round(tabFFT[i].imag,2)*1j
    
    for i in range(len(tabFTD2)):
        for j in range(len(tabFTD2[0])):
            tabFTD2[i][j]=round(tabFTD2[i][j].real,2)+round(tabFTD2[i][j].imag,2)*1j

    for i in range(len(tabFFT2)):
        for j in range(len(tabFFT2[0])):
            tabFFT2[i][j]=round(tabFFT2[i][j].real,2)+round(tabFFT2[i][j].imag,2)*1j
    print("Transformé 2D")
    print(tabFTD2)
    print("Transforme 2D rapide")
    print(tabFFT2)
    print("Transforme 1D")
    print(tabFTD)
    print("Transforme 1D rapide")
    print(tabFFT)
    #Lire image et l'afficher
    img = cv2.imread('calimero.jpg',0)
    cv2.imshow('De Base',img)
    imgArr = img.tolist()

    #Appliquer la transformé de fourier rapide à l'image
    imgArr=FFT2D.usual(imgArr)
    imgArrRealFFTD2 = copy.deepcopy(imgArr)
    
    #Affichage de l'image
    for i in range(len(imgArrRealFFTD2)):
        for j in range(len(imgArrRealFFTD2[0])):
            imgArrRealFFTD2[i][j] = round(imgArrRealFFTD2[i][j].real) 
    
    img = numpy.uint8(numpy.array(imgArrRealFFTD2))
    cv2.imshow('FFT2D',img)

    #Appliquer la transformé de fourier rapide inverse à l'image
    imgArr=FFT2D.inverse(imgArr)  
    imgArrRealFFTD2I = copy.deepcopy(imgArr)

    #Affichage de l'image
    for i in range(len(imgArrRealFFTD2I)):
        for j in range(len(imgArrRealFFTD2I[0])):
            imgArrRealFFTD2I[i][j] = round(imgArrRealFFTD2I[i][j].real)
    
    img = numpy.uint8(numpy.array(imgArrRealFFTD2I))
    cv2.imshow('FFT2D Inverse',img)
    
    
    #Attendre
    cv2.waitKey(0)

    
    


