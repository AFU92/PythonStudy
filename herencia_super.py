class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        
        self.nombre=nombre

        self.edad=edad

        self.lugar_residencia=lugar_residencia

    def descripcion(self):

        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugar_residencia)

class Empleado(Persona):

    def __init__(self, nombre, edad, lugar_residencia, salario, antiguedad):
        super().__init__(nombre, edad, lugar_residencia)
        self.salario=salario
        self.antiguedad=antiguedad 

    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario," Antiguedad: ", self.antiguedad)


Empleado1=Empleado("Ana", 34, "Bogota", 800000, "8 Años")

Empleado1.descripcion()

print(isinstance(Empleado1, Persona))

