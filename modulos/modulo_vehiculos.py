
class Vehiculos():

    def __init__(self,marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__enmarcha = False
        self.__acelera = False
        self.__frena = False

    def getMarca(self):
        return self.__marca

    def arrancar (self):
        self.__enmarcha = True

    def acelerar(self):
        self.__acelera = True

    def frenar(self):
        self.__frena = True

    def estado(self):
        print("----------------------")
        print("Marca: ", self.getMarca(), "\nModelo: ", self.__modelo , "\nEn Marcha: ",
              self.__enmarcha, "\nAcelerando: ", self.__acelera, "\nFrenando: ", self.__frena)


class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.__cargado = cargar
        if(self.__cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

        
class Moto(Vehiculos):
    
    def __init__(self,marca, modelo):

        super().__init__(marca, modelo)
        self.__hcaballito = ""
        self.marcaP = marca
        self.modeloP = modelo
             

    def caballito(self):        
        self.__hcaballito="Voy haciendo el caballito"
    
    #@override
    def estado(self):
        super().estado()
        print(f"Caballito: {self.__hcaballito}")
        
moto = Moto("Suzuki","Kawasaki")
moto.caballito()
moto.estado()


class VElectricos(Vehiculos):

    def __init__(self,marca,modelo):

        super().__init__(marca,modelo)

        self.__autonomia = 100

    def cargarEnergia(self):
        self.__cargando = True

    def estado(self):

        super().estado()
        print(f"La autonomia es: {self.__autonomia}")
        print(f"La carga de energia se hizo? {self.__cargando}")


