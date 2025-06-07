def bubble_sort(arr):
    #ciclo externo para iterar en la lista n cantidad de veces
    for n in range(len(arr) -1, 0, -1):
        #se inicializa el cambio para rastrear cualquien cambio que pueda ocurrir
        swapped = False

        #Ciclo interno para comparar elementos adyacentes
        for i in range(n):
            if arr[i] > arr[i + 1]:
                #Se cambian los elementos si están en el orden incorrecto
                arr[i], arr[i + 1] = arr[i + 1], arr[1]

                #Se marca que ocurrió un cambio
                swapped = True

        #Si no hay cambios, la lista ya está ordenada
        if not swapped:
            break

#Ejemplo de lista a ordenar

arr = [6, 10, 52, 23, 6, 5]
print("La lista sin ordenar es: ")
print(arr)

bubble_sort(arr)

print("La lista ordenada es: ")
print(arr)