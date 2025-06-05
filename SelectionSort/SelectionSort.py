def selectionSort(array):  # <- Elimina el parámetro size
    size = len(array)      # <- Calcula el tamaño aquí
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[ind], array[min_index] = array[min_index], array[ind]

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
selectionSort(arr)  # <- Llama sin el segundo parámetro
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)