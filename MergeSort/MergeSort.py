def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    #Se crean los arreglos temporales
    L = [0] * (n1)
    R = [0] * (n2)

    #Se copian los datos a los arreglos temporales
    for i in range(0, n1):
        L[i] = arr[l + i]
    
    for j in range (0, n2):
        R[j] = arr[m + 1 + j]

    #Se combinan los arreglos temporales en arr[l..r]
    i = 0 #índice inicial del primer subarreglo
    j = 0 #índice inicial del segundo subarreglo
    k = l #índice inicial del subarreglo combinado

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    #Se copian lo elementos sobrantes de L[] en caso de que todavía haya
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    #se copian los elemntos sobrantes de R[] en caso de haber
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l< r:
        #equivale aq (l+r//2), pero evita el exceso en l y r
        m = l+(r-l)//2

        #Se ordenan la primera y segunda mitad
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


#Se prueba el algoritmo
arr = [7, 27, 9, 5, 4, 1, 1, 2, 3]
n = len(arr)
print("El arreglo es: ")
for i in range(n):
    print("%d" % arr[i], end=(""))

mergeSort(arr, 0, n-1)
print("\n\nEl arreglo ordenado es: ")
for i in range(n):
    print("%d" % arr[i], end=(""))
