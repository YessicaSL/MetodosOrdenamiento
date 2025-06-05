def insertionSort(arr):
    n = len(arr) #Se obtiene la longitus del arreglo

    if n <= 1:
        return #si el arreglo tiene 0 ó 1 elemento, este ya fue ordenado y regresa
    
    for i in range(1, n): #Itera sobre el arreglo iniciando a partir del elemento en la posición 1
        key = arr[i] #se almacena el elemento actual como la llave a insertar en la posición correcta
        j = i-1
        while j >= 0 and key < arr[j]: #Mueve los elementos una posición adelante
            arr[j+1] = arr[j] #cambia los elementos a la derecha
            j -= 1
        arr[j + 1] = key #Coloca la llave en la posición correcta

#Se comprobará ordenando el arreglo [6, 18, 23, 4, 59]

arr = [6, 18, 23, 4, 59]

insertionSort(arr)
print(arr)