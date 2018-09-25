class coche():

    "Constructor"
    def __init__ (self): 
        "propiedades"
        self.largoChasis=250
        self.anchoChasis=120
        "encapsular variable o propiedad"
        self.__ruedas=4
        self.enmarcha=False
    
    "comportamientos o metodos: defs (metodo o funcion especial de la clase)"
    "def es una funcion que no pertenece a la clase"

    def arrancar (self, arrancamos):
        self.enmarcha=arrancamos

        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado (self):
        print("El largo del coche es: ",self.largoChasis,"El ancho del coche es: ", self.anchoChasis,
         "El coche tiene: ", self.ruedas, "ruedas")

miCoche=coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("---------- A continuación creamos el segundo objeto ----------")

cocheDaniel=coche()
print(cocheDaniel.arrancar(False))

cocheDaniel.ruedas=2

cocheDaniel.estado()

