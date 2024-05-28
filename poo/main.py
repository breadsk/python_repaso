class Auto():    

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha=False

    def arrancar(self,arrancamos):

        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El auto esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El auto esta detenido"

    def estado(self):
        print(f"El auto tiene { self.__ruedas } ruedas")
        print(f"El auto tiene { self.__anchoChasis } de ancho")
        print(f"El auto tiene { self.__largoChasis } de largo")

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False

miAuto = Auto()#Instanciar una clase
print(miAuto.arrancar(True))
