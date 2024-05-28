class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

#                          aqui pasa el polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo)
