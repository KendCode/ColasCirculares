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
    while(inicio != marca):
        inicio,fin,dato = eliColaCircular(cola, maxCola, inicio, fin, dato)
        print(f"{dato}")
        inicio,fin = adiColaCircular(cola,maxCola,inicio,fin,dato)
    print(cola[marca-1])
    return inicio,fin

def run():
    cola=[]
    inicio= None
    fin=None
    maxCola=int(input('max cola: '))
    #INICIALIZAMOS LA COLA
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
    #LISTAR COLAS
    inicio,fin = listarColaCircular(cola,maxCola,inicio,fin,dato)
    print (cola)
    

if __name__=='__main__':
    run()