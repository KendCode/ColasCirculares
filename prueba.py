def iniCola(cola,maxCola,inicio,fin):
    for i in range(maxCola):
        cola.append(None)
    inicio=0
    fin=0
    return inicio,fin


def adiColaCircular(cola, maxCola, inicio, fin, dato):
    if ((fin == maxCola and inicio == 1) or ((fin + 1)== inicio)):
        print('Cola llena')
    else:
        if(fin == maxCola):
            fin = 1
        else:
            fin = fin + 1 
        cola[fin-1] = dato
        if(inicio == 0):
            inicio = 1
    return inicio, fin


def eliColaCircular(cola, maxCola, inicio, fin, dato):
    if(fin == 0):
        print('Cola Vacia')
    else:
        dato = cola[inicio-1]
        cola[inicio-1]=None
        if(inicio==fin):
            inicio = 1
            fin = 1
        else: 
            if(inicio==maxCola):
                inicio=1
            else:
                inicio =inicio + 1
    return inicio,fin,dato


def listarColaCircular(cola, maxCola, inicio, fin,dato):
    marca = fin
    sw = 0
    while(sw == 0):
        if(inicio == marca):
            sw = 1
        inicio,fin,dato = eliColaCircular(cola, maxCola, inicio, fin, dato)
        print(f"{dato}")
        inicio,fin = adiColaCircular(cola,maxCola,inicio,fin,dato)
    return inicio,fin

# EJERCICIO 1
def eliPrimerEleImpar(cola, maxCola, inicio, fin,dato):
    marca = fin
    primerImpar = 0
    sw = 0
    while(sw == marca):
        if(inicio != marca):
            sw = 1
        inicio,fin,dato = eliColaCircular(cola, maxCola, inicio, fin, dato)
        if dato %2== 0:
            inicio,fin = adiColaCircular(cola,maxCola,inicio,fin,dato)
        else:
            if primerImpar == 0:
                primerImpar = 1
            else:
                inicio,fin = adiColaCircular(cola,maxCola,inicio,fin,dato)
    return inicio,fin

#EJERCICIO 2
# def adicionarDespuesPrimerPar(cola, maxCola, inicio, fin, x):
#     pos = inicio
#     encontrado = False
#     while pos != fin:
#         if cola[pos - 1] % 2 == 0:
#             encontrado = True
#             break
#         pos = (pos % maxCola) + 1
    
#     if encontrado:
#         fin = (fin % maxCola) + 1
#         for i in range(fin-1, pos, -1):
#             cola[i % maxCola] = cola[(i - 1) % maxCola]
#         cola[pos % maxCola] = x
#     else:
#         print("No hay ningún elemento par en la cola.")
    
#     return inicio, fin

#EJERCICIO3
# def ordenarColaCircular(cola, maxCola, inicio, fin):
#     elementos = []
#     pos = inicio
    
#     while pos != fin:
#         elementos.append(cola[pos - 1])
#         pos = (pos % maxCola) + 1
    
#     elementos.sort()
    
#     pos = inicio
#     for elem in elementos:
#         cola[pos - 1] = elem
#         pos = (pos % maxCola) + 1
    
#     return inicio, fin

#EJERCICIO 4
# def paresAlPrincipio(cola, maxCola, inicio, fin):
#     pares = []
#     impares = []
#     pos = inicio
    
#     while pos != fin:
#         if cola[pos - 1] % 2 == 0:
#             pares.append(cola[pos - 1])
#         else:
#             impares.append(cola[pos - 1])
#         pos = (pos % maxCola) + 1
    
#     nuevaCola = pares + impares
#     for i in range(len(nuevaCola)):
#         cola[i] = nuevaCola[i]
    
#     fin = len(pares) + len(impares)
#     return inicio, fin

#EJERCICIO 5
# def eliminarMultiplosDeN(cola, maxCola, inicio, fin, n):
#     nueva_cola = []

#     while inicio != fin:
#         dato = cola[inicio - 1]
#         if dato % n != 0:
#             nueva_cola.append(dato)
#         inicio = (inicio % maxCola) + 1

#     return nueva_cola

def run():
    cola=[]
    inicio= None
    fin=None
    maxCola=int(input('max cola: '))

    #inicializamos la cola
    inicio,fin=iniCola(cola,maxCola,inicio,fin)

    #print(cola)
    #print(f'inicio: {inicio}, fin {fin}')
    for i in range(1, maxCola+1):
        dato=int(input('dato: '))
        inicio,fin=adiColaCircular(cola,maxCola,inicio,fin,dato)
        if i<maxCola:
            nuevoDato=input('Desea seguir insertando datos si o no?: ')
        if(nuevoDato=='si'or nuevoDato == 's'):
            continue
        else:
            break

    #listar cola
    inicio,fin = listarColaCircular(cola,maxCola,inicio,fin,dato)
    print (cola)
    
    print(f'Cola{cola}')
    print(f'inicio:{inicio}; fin:{fin}\n')
    # 1
    inicio,fin = eliPrimerEleImpar(cola, maxCola, inicio, fin,dato)
    # 2
    # x = int(input("Introduce el valor a insertar después del primer par: "))
    # inicio, fin = adicionarDespuesPrimerPar(cola, maxCola, inicio, fin, x)
    #3
    #inicio, fin = ordenarColaCircular(cola, maxCola, inicio, fin)
    #4  
    #inicio, fin = paresAlPrincipio(cola, maxCola, inicio, fin)
    # 5
    # n = int(input('Ingrese el valor de n para eliminar múltiplos de n: '))
    # cola = eliminarMultiplosDeN(cola, maxCola, inicio, fin, n)
    # print("Cola después de eliminar múltiplos de n:", cola)

    print (cola)

if __name__=='__main__':
    run()