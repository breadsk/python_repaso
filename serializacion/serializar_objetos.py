import pickle

class Vehiculo():

    def __init__(self,marca,modelo):

        self.__marca = marca
        self.__modelo = modelo
        self.__enmarcha = False
        self.__acelera = False
        self.__frena = False

    def arrancar(self):
        self.__enmarcha = True
        
    def acelerar(self):
        self.__acelera = True

    def frenar(self):
        self.__frena = True

    def estado(self):
        print("Marca: ", self.__marca, "\nModelo: ", self.__modelo, "\nEn marcha: ",self.__enmarcha,"\nAcelerando: ",self.__acelera,"\nFrenando: ", self.__frena)
        

auto1 = Vehiculo('Chevrolet','Spark')

auto2 = Vehiculo('Chery','Beat')

auto3 = Vehiculo('Suzuki','Ignis')

autos = [auto1,auto2,auto3]

fichero = open("los_autos","wb")

pickle.dump(autos,fichero)

fichero.close()

del (fichero) #Borrar fichero de la memoria

ficheroApertura = open("los_autos","rb")

mis_autos = pickle.load(ficheroApertura)

ficheroApertura.close()

for auto in mis_autos:
    print(auto.estado())






