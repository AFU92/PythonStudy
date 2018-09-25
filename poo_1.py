class coche():

    "Constructor"
    def __init__ (self):
        "encapsular viariables o propiedades"
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    "comportamientos o metodos: defs (metodo o funcion especial de la clase)"
    "def es una funcion que no pertenece a la clase"

    def arrancar (self, arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado (self):
        print("El largo del coche es: ",self.__largoChasis,"El ancho del coche es: ", self.__anchoChasis,
         "El coche tiene: ", self.__ruedas, "ruedas")

miCoche=coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("---------- A continuación creamos el segundo objeto ----------")

cocheDaniel=coche()
print(cocheDaniel.arrancar(False))

cocheDaniel.__ruedas=2

cocheDaniel.estado()

