class coche():
    "propiedades"
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    "comportamientos o metodos: defs (metodo o funcion especial de la clase)"
    "def es una funcion que no pertenece a la clase"

    def arrancar (self):
        self.enmarcha=True

    def estado (self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        
miCoche=coche()
    
print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene: ",miCoche.ruedas, "ruedas")

miCoche.arrancar()

print(miCoche.estado())

