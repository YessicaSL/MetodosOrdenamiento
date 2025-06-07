from random import sample

lista = list(range(100))
vectorquick = sample(lista, 8)

def quickSort(vectorquick, start=0, end=None):
    if end is None:
        end = len(vectorquick) - 1
    
    print("EL vector a ordenar es: ", vectorquick)
    
    def particion(arr, start, end):
        pivot = arr[start]  # El pivote debe ser un valor, no la lista completa
        menor = start + 1
        mayor = end
        
        while True:
            # Mover el índice menor hacia la derecha
            while menor <= mayor and arr[menor] <= pivot:
                menor += 1
            
            # Mover el índice mayor hacia la izquierda
            while menor <= mayor and arr[mayor] >= pivot:
                mayor -= 1
            
            if menor <= mayor:
                # Intercambiar elementos
                arr[menor], arr[mayor] = arr[mayor], arr[menor]
            else:
                break
        
        # Colocar el pivote en su posición correcta
        arr[start], arr[mayor] = arr[mayor], arr[start]
        return mayor

    def quick(arr, start, end):
        if start >= end:
            return
        
        # Realizar la partición
        p = particion(arr, start, end)
        
        # Ordenar recursivamente las dos mitades
        quick(arr, start, p - 1)
        quick(arr, p + 1, end)

    # Llamar a la función interna quick con los parámetros correctos
    quick(vectorquick, start, end)
    print("El vector ordenado es: ", vectorquick)

quickSort(vectorquick)