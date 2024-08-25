#class Automovil:
    #PROPIEDADES DE LA CLASE AUTOMOVIL
    #ruedas = 4
    #color, modelo 

    #metodos de la clase automovil
    #constructor de clase inicializar
    # def __init__(self, colorAuto, modelAuto):
    #     self.color = colorAuto
    #     self.modelo = modelAuto

    # def CambiaColor(self, nuevoColor):
    #     self.color = nuevoColor

    # def Anguedad(self):
    #     return(2024-self.modelo)
class Estudiante:
    def __init__(self, nombre, nacimineto):
        self.Nombre = nombre
        self.AnoNac = nacimineto

    def CambiarNombre(self, NuevoNombre):
        self.Nombre = NuevoNombre
    
    def CalcularEdad(self):
        return(2024-self.AnoNac)




def run():
    # a1 = Automovil('Rojo', 1998)
    # a2 = Automovil('Azul',2000)

    # print(a1.color)
    # print(a1.modelo)

    # a1.CambiaColor('violeta')
    # print(a1.color)
    # print(f'La antiguedad del automovil es: {a1.Anguedad()}')

    est1 = Estudiante('Alambrito',2004)
    est2 = Estudiante('Lucas',2000)
    print(est1.Nombre)
    print(est1.AnoNac)
    print(f'La edad del estudiante es: {est1.CalcularEdad()}')

if __name__=='__main__':
    run()
    #ESTUDIANTES INICIALIZAR NOMBRE Y AÑO DE NACIMIENTO EN INIT
    #CAMBIAR NOMBRE , CALCULAR LA EDAD PARA DOS ESTUDIANTES 
    #EXAMEN