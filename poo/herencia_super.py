###################################################################################################
class Persona():

    def __init__(self,nombre,edad,direccion):
        
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion

    def descripcion(self):

        print(f"Nombre : { self.__nombre } , Edad: {self.__edad} , Direccion: {self.__direccion}")
###################################################################################################
class Empleado(Persona):

    def __init__(self , salario , antiguedad , nombre , edad , direccion):
        
        super().__init__(nombre,edad,direccion)

        self.__salario = salario
        self.__antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(f"Salario : { self.__salario } , Antiguedad: {self.__antiguedad}")

#nicolas = Persona("Nicolas",40,"Benito Rebolledo 3036")
#nicolas.descripcion()
        
#nicolas = Empleado("Nicolas",40,"Chile",1500000,15)
nicolas = Persona("Nicolas",40,"Chile")
nicolas.descripcion()

print(isinstance(nicolas,Empleado))
print(isinstance(nicolas,Persona))

###################################################################################################


