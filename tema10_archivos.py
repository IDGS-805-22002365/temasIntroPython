#Archivos txt
from io import open

#Se puede especificar el modo de apertura del archivo
#r: lectura
#w: escritura
#a: añadir
#r+: lectura y escritura
# w+: escritura y lectura

texto="Una linea con texto\nOtra linea con texto"
#Se puede poner cualquier tipo de extension (pdf, txt, etc)
fichero=open("fichero.txt","w")
fichero.write(texto)

cadena2="\nEsta es otra linea mas"
fichero.write(cadena2)
fichero.close()

#Esto no funcionara porqqe el archivo ya esta cerrado (linea 18)
cadena3="\nEsta es la cadena 3"
fichero.write(cadena3)


