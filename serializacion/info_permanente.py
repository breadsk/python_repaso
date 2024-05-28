import pickle

class Persona:

    def __init__(self,nombre,genero,edad):
        
        self.__nombre = nombre
        self.__genero = genero
        self.__edad = edad
        print("Se ha creado una persona nueva con el nombre de: ", self.__nombre)

    def __str__(self):
        return "{} {} {}".format(self.__nombre,self.__genero,self.__edad)
    
class ListaPersonas:

    personas = []

    def __init__(self):
        #                                        agregar informacion binaria = ab+
        lista_de_personas = open("ficheroExterno","ab+")
        lista_de_personas.seek(0)

        try:
            self.personas = pickle.load(lista_de_personas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío , se procede a crear")
        finally:
            lista_de_personas.close()
            del(lista_de_personas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)

    def guardarPersonasEnFicheroExterno(self):
        #Lo lee y lo envia aqui
        lista_de_personas = open("ficheroExterno","wb")
        pickle.dump(self.personas, lista_de_personas)
        lista_de_personas.close()
        del(lista_de_personas)

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()
persona=Persona("Hernan","Masculino",88)
#persona2=Persona("Katherine","Femenino",35)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()

