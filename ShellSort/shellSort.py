from random import sample
#Se importa un método desde random para generar listas aleatorias

lista = list(range(100))#Se crea una lista base con números del 1 al 100

#Se crea una lista aleatoria de 8 elementos usando sample
vectorshell = sample(lista,8)

def shellSort(vectorshell):