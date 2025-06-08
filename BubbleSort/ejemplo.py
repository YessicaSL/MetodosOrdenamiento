niños = [
    {"nombre": "Juan", "estatura": 1.25},
    {"nombre": "María", "estatura": 1.32},
    {"nombre": "Pedro", "estatura": 1.28},
    {"nombre": "Ana", "estatura": 1.30},
    {"nombre": "Luis", "estatura": 1.22},
    {"nombre": "Sofía", "estatura": 1.35},
    {"nombre": "Carlos", "estatura": 1.27},
    {"nombre": "Laura", "estatura": 1.29},
    {"nombre": "Diego", "estatura": 1.33},
    {"nombre": "Valeria", "estatura": 1.26},
    {"nombre": "Miguel", "estatura": 1.31},
    {"nombre": "Isabella", "estatura": 1.24},
    {"nombre": "Javier", "estatura": 1.34},
    {"nombre": "Camila", "estatura": 1.23},
    {"nombre": "Andrés", "estatura": 1.36}
] #Lista de niños con nombres y estatura

#función para ordenar
def ordenar_por_estatura(grupo):
    n = len(grupo)

    #copia de la lista original
    ordenados = grupo.copy()
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if ordenados[j]["estatura"] > ordenados[j + 1]["estatura"]:
                ordenados[j], ordenados[j+1] = ordenados[j+1], ordenados[j]
                swapped = True
        
        #si no hay cambios es porque ya está ordenada
        if not swapped:
            break

    return ordenados
niños_ordenados = ordenar_por_estatura(niños)

#Lista de niños sin ordenar
print("Niños de cuarto grado: ")
for i, niño in enumerate(niños, 1):
    print(f"{i}. {niño['nombre']}: {niño['estatura']} m")

print("-" * 50)
# Mostramos resultados
print("Niños ordenados por estatura (del más bajito al más alto):")
for i, niño in enumerate(niños_ordenados, 1):
    print(f"{i}. {niño['nombre']}: {niño['estatura']} m")
