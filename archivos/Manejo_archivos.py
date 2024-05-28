

from io import open

#w de write
#archivo_texto = open("archivo.txt","w");
#ahora solo leer , read
#archivo_texto = open("archivo.txt","r");
#archivo_texto = open("archivo.txt","a");

archivo_texto = open("archivo.txt","r+")#Lectura y escritura

#archivo_texto.seek(11)#Solo posiciona el puntero en el lugar en el que le especificamos

#print(archivo_texto.read(11))#Hace lectura hasta la posicion del puntero que le indiquemos
#EL primero lo dejo hasta el 11, el otro lee desde donde quedo el puntero
#print(archivo_texto.read())

#Para estar en la mitad del archivo
#archivo_texto.seek(len(archivo_texto.read())/2)

#Al final de la primera linea
#archivo_texto.seek(len(archivo_texto.readline()))

#print(archivo_texto.read())

#Puntero en la posicion 0
#archivo_texto.write("Comienzo del texto")
lista_texto = archivo_texto.readlines()

lista_texto[2]=" Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()

#texto=archivo_texto.read()
#lineas_texto = archivo_texto.readlines()

#archivo_texto.close()

#print(lineas_texto[0])



#print(texto)

#frase="Estupendo día para estudiar python \n el Lunes"

#archivo_texto.write(frase)

#archivo_texto.close()