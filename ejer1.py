#Ejercicio 1: Eliminar el primer elemento impar de una cola circular
def iniCola(cola,maxCola,inicio,fin):
    for i in range(maxCola):
        cola.append(None)
    inicio=0
    fin=0
    return inicio,fin
def adiColaCircular(cola, maxCola, inicio, fin, dato):
    if((fin==maxCola and inicio==1)or((fin+1)==inicio)):
        print('Cola llena')
    else:
        fin+=1
    cola[fin-1]=dato
    if(inicio==0):
        inicio=1
    return inicio,fin
def eliColaCircular(cola, maxCola, inicio, fin, dato):
    if(fin == 0):
        print('Cola Vacia')
    else:
        dato=cola[inicio-1]
        cola[inicio-1]=None
        if(inicio==fin):
            inicio = 1
            fin = 1
        else: 
            if(inicio==maxCola):
                inicio=1
            else:
                inicio+=1
    return inicio,fin
def listarColaCircular(cola, maxCola, inicio, fin,dato):
    marca = fin
    while(inicio != marca):
        inicio,fin,dato= eliColaCircular(cola, inicio, fin, dato)
        print(f"dato")
        inicio,fin=adiColaCircular(cola,fin,maxCola,dato)
    print(cola[marca-1])
    return inicio,fin


def eliPrimerImpar(cola, maxCola, inicio, fin):
    marca = fin
    encontrado = False
    
    while(inicio != marca and not encontrado):
        dato = cola[inicio - 1]
        if dato % 2 != 0:
            inicio, fin, _ = eliColaCircular(cola, maxCola, inicio, fin, dato)
            encontrado = True
        else:
            inicio, fin = adiColaCircular(cola, maxCola, inicio, fin, dato)
    
    if not encontrado and cola[marca - 1] % 2 != 0:
        inicio, fin, _ = eliColaCircular(cola, maxCola, inicio, fin, cola[marca - 1])
    
    return inicio, fin

# Función principal para probar el ejercicio
def runEjercicio1():
    cola = []
    inicio, fin = iniCola(cola, 10, 0, 0)
    datos = [2, 3, 4, 5, 6]
    
    for dato in datos:
        inicio, fin = adiColaCircular(cola, 10, inicio, fin, dato)
    
    inicio, fin = eliPrimerImpar(cola, 10, inicio, fin)
    inicio, fin = listarColaCircular(cola, 10, inicio, fin, None)

runEjercicio1()