from random import sample

lista = list(range(100))
vectorcocktail = sample(lista, 8)

def cocktailSort(vectorcocktail):
    print("El vector a ordenar es: ", vectorcocktail)
    
    largo = len(vectorcocktail)  # Simplificado: usa len() en lugar de contador
    
    for i in range(largo // 2):
        cambiar = False
        
        # Pasada de izquierda a derecha (como Bubble Sort normal)
        for j in range(1 + i, largo - i):
            if vectorcocktail[j] < vectorcocktail[j-1]:  # Comparar con elemento anterior
                vectorcocktail[j], vectorcocktail[j-1] = vectorcocktail[j-1], vectorcocktail[j]
                cambiar = True
        
        if not cambiar:
            break
        
        cambiar = False
        
        # Pasada de derecha a izquierda
        for j in range(largo - i - 2, i, -1):  # Corrección en el rango
            if vectorcocktail[j] < vectorcocktail[j-1]:  # Comparación corregida
                vectorcocktail[j], vectorcocktail[j-1] = vectorcocktail[j-1], vectorcocktail[j]
                cambiar = True
        
        if not cambiar:
            break
    
    print("El vector ordenado es: ", vectorcocktail)

cocktailSort(vectorcocktail)