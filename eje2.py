#Ejercicio 2: Adicionar un elemento "x" 
#después del primer elemento par de una cola circular, si es posible
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

def adicionar_despues_par(cola, maxCola, inicio, fin, x):
    if inicio == 0:
        print("Cola vacía")
        return inicio, fin
    
    marca = fin
    encontrado = False
    
    while inicio != marca and not encontrado:
        dato = cola[inicio - 1]
        if dato % 2 == 0:  # Si el número es par
            inicio, fin = adiColaCircular(cola, maxCola, inicio, fin, x)
            encontrado = True
        else:
            inicio, fin = adiColaCircular(cola, maxCola, inicio, fin, dato)
        
        inicio += 1
    
    return inicio, fin

# Ejemplo de uso:
# cola = [2, 3, 5, 8, 9]
# maxCola = 6
# x = 10
# inicio, fin = adicionar_despues_par(cola, maxCola, inicio, fin, x)

def run():
    cola = []
    inicio = None
    fin = None
    maxCola = int(input('Max cola: '))
    
    # Inicializamos la cola
    inicio, fin = iniCola(cola, maxCola, inicio, fin)
    
    for i in range(1, maxCola + 1):
        dato = int(input('Dato: '))
        inicio, fin = adiColaCircular(cola, maxCola, inicio, fin, dato)
        
        if i < maxCola:
            nuevoDato = input('¿Desea seguir insertando datos (si o no)?: ')
            if nuevoDato.lower() != 'si' and nuevoDato.lower() != 's':
                break
    
    # Preguntar el valor x a añadir después del primer elemento par
    x = int(input('Ingrese el valor x a añadir después del primer número par: '))
    
    # Adicionar después del primer elemento par
    inicio, fin = adicionar_despues_par(cola, maxCola, inicio, fin, x)
    
    # Listar colas
    inicio, fin = listarColaCircular(cola, maxCola, inicio, fin, None)
    
    print('Cola final:', cola)

if __name__ == '__main__':
    run()
