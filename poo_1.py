

class coche():

    "Constructor"
    def __init__ (self): 
        "propiedades"
        self.__largoChasis=250
        self.__anchoChasis=120
        "encapsular variable o propiedad"
        self.__ruedas=4
        self.__enmarcha=False
    
    "comportamientos o metodos: defs (metodo o funcion especial de la clase)"
    "def es una funcion que no pertenece a la clase"

    def arrancar (self, arrancamos):
        self.__enmarcha=arrancamos

        if (self.__enmarcha):
            chequeo=self.__chequeo_interno() 

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche esta parado"

    def estado (self):
        print("El largo del coche es: ",self.__largoChasis,"El ancho del coche es: ", self.__anchoChasis,
         "El coche tiene: ", self.__ruedas, "ruedas")

    "Encapsular metodo"
    "Encapsular metodos para acceder solo desde la propia clase"
    def __chequeo_interno(self):
        print ("realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else: 
            return False 

miCoche=coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("---------- A continuación creamos el segundo objeto ----------")

cocheDaniel=coche()

print(cocheDaniel.arrancar(False))

cocheDaniel.estado()


