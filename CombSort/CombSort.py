from random import sample

lista = list(range(100))

vectorcomb = sample(lista, 8)

def combSort(vectorcomb):
    print("El vector a ordenar es: ", vectorcomb)
    
    largo = 0 # contador del vector

    for _ in vectorcomb:
        largo +=1

    diferencia = largo #Al inicio la diferencia es igual a largo

    #Variable para definir si es necesario o no intercambiar los números que se están comparando
    cambiar = True

    while diferencia > 1 or cambiar:
        diferencia = max(1, int(diferencia / 1.25))
        #la diferencia mínimae s 1 y en cada iteración la diferencia disminuye

        cambiar = False
        for i in range(largo - diferencia):
            j = i+ diferencia
            #se ubica el número que está a la distancia x de 1
            if vectorcomb[i] > vectorcomb[j]:
                vectorcomb[i], vectorcomb[j] = vectorcomb[j], vectorcomb[i]
                #se intercambian los npumeros
                cambiar = True
    print("El vector ordenado es: ", vectorcomb)

combSort(vectorcomb)