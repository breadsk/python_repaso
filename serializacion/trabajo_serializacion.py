import pickle

#lista_nombres=["Pedro","Ana","Maria","Carolina"]

#wb escritura binaria
#fichero_binario = open("lista_nombres","wb")

#Volcado
#pickle.dump(lista_nombres,fichero_binario)

#fichero_binario.close()

#del (fichero_binario)

#read binary
fichero = open("lista_nombres","rb")

lista=pickle.load(fichero)

print(lista)