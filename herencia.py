class vehiculo():

    def __init__(self, marca, modelo):

        self.marca=marca

        self.modelo=modelo

        self.enmarcha=False 

        self.acelera=False

        self.frena=False 

    def arrancar (self):
        self.enmarcha=True

    def acelerar (self):        
        self.acelerar=True 

    def frenar (self):
        self.frena=True 

    def estado(self):
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha,
        "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)

class Furgoneta (vehiculo):
    
    def cargar(self, cargar):

        self.cargado=cargar

        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class vehi_electricos(vehiculo):

    def __init__(self, marca, modelo):

        super().__init__(marca,modelo)

        self.autonomia=100

    def cargarEnergia(self):

        self.cargando=True 

class Moto (vehiculo):
    
    hacer_caballito=''

    def caballito (self):
        self.hacer_caballito="Voy haciendo el caballito"
    
    def estado(self):
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha,
        "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena,"\nHacer Caballito: ",
         self.hacer_caballito)

miMoto=Moto("Honda","CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.cargar(True))

class BicicletaElectrica (vehi_electricos, vehiculo):

    pass 

miBiciElectrica=BicicletaElectrica("abc", "123")