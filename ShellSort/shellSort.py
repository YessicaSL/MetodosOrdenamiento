from random import sample
#Se importa un método desde random para generar listas aleatorias

lista = list(range(100))#Se crea una lista base con números del 1 al 100

#Se crea una lista aleatoria de 8 elementos usando sample
vectorshell = sample(lista,8)

def shellSort(vectorshell): #Función para ordenar el vector aleatorio con el método Shell Sort
    print("El vector a ordenar es: ", vectorshell)
    largo = 0

    for i in vectorshell:
        largo += 1

    distancia = largo // 2

    #Se crea un bucle según las distancias
    while distancia > 0:
        #se usa insertion sort
        for i in range(distancia, largo):
            val = vectorshell[i]
            j = i
            while j >= distancia and vectorshell[j - distancia] > val:
                vectorshell[j] = vectorshell[j - distancia]
                j -= distancia
            vectorshell[j] = val
        distancia //= 2 #Se acota la distancia nuevamente y se continúa el ciclo
    print("El vector ordenado con shell es: ", vectorshell)

shellSort(vectorshell)