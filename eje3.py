def iniCola(cola, maxCola):
    for i in range(maxCola):
        cola.append(None)
    inicio = 0
    fin = 0
    return inicio, fin

def adiColaCircular(cola, maxCola, inicio, fin, dato):
    if ((fin == maxCola and inicio == 1) or ((fin + 1) == inicio)):
        print('Cola llena')
    else:
        if fin == maxCola:
            fin = 1
        else:
            fin = fin + 1 
        cola[fin-1] = dato
        if inicio == 0:
            inicio = 1
    return inicio, fin

def eliColaCircular(cola, maxCola, inicio, fin):
    dato = None
    if inicio == 0:
        print('Cola vacía')
    else:
        dato = cola[inicio-1]
        cola[inicio-1] = None
        if inicio == fin:
            inicio = 0
            fin = 0
        else: 
            if inicio == maxCola:
                inicio = 1
            else:
                inicio = inicio + 1
    return inicio, fin, dato

def listarColaCircular(cola, maxCola, inicio, fin):
    if inicio == 0:
        print('Cola vacía')
        return inicio, fin

    i = inicio
    while True:
        print(cola[i-1])
        if i == fin:
            break
        i = (i % maxCola) + 1
    return inicio, fin

def ordenarCola(cola, maxCola, inicio, fin):
    if inicio == 0:
        print('Cola vacía')
        return cola

    elementos = []
    i = inicio
    while True:
        elementos.append(cola[i - 1])
        if i == fin:
            break
        i = (i % maxCola) + 1

    elementos.sort()

    for j in range(len(elementos)):
        cola[j] = elementos[j]

    for k in range(len(elementos), maxCola):
        cola[k] = None

    inicio = 1
    fin = len(elementos)

    return cola, inicio, fin

def run():
    cola = []
    maxCola = int(input('Max cola: '))
    
    # Inicializamos la cola
    inicio, fin = iniCola(cola, maxCola)
    
    for i in range(1, maxCola + 1):
        dato = int(input('Dato: '))
        inicio, fin = adiColaCircular(cola, maxCola, inicio, fin, dato)
        if i < maxCola:
            nuevoDato = input('Desea seguir insertando datos si o no?: ')
            if nuevoDato.lower() not in ['si', 's']:
                break
    
    # Ordenar cola
    cola, inicio, fin = ordenarCola(cola, maxCola, inicio, fin)
    
    # Listar cola
    inicio, fin = listarColaCircular(cola, maxCola, inicio, fin)
    print(cola)

if __name__ == '__main__':
    run()
