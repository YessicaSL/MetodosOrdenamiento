def heapify(arr, n, i):
    largest = i #Se inicializa el elemento más grande como raíz
    l = 2 * i + 1 #"left" = 2*i+1
    r = 2 * i + 2 # right = 2*i +2

    #Se revisa si el hijo izqierdo de la raíz existe y si es más grande que la raíz
    if l < n and arr[i] < arr[l]:
        largest = l

    #Se revisa si el hijo derecho de la raíz existe y si es mayor a la raiz
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    #Se cambia la raíz de se rnecesario
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) #se hace el cambio

         #Se le hace heap a la raíz
        heapify(arr, n, largest)

# Funsión proncipal para ordenar cualquier arreglo de un tamaño determinado

def heapSort(arr):
    n = len(arr)

 # se agrupa.
 # Como el último padre se posiciona en (n/2) se puede comenzar en esa posición.

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

 # Se extraen los elementos uno por uno

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # cambio
        heapify(arr, i, 0)


# Comprobamos

arr = [12, 11, 13, 5, 6, 7, ]
print("El arreglo es: ")
heapSort(arr)
n = len(arr)
print("El arreglo ordenado es: ")
for i in range(n):
    print(arr[i])