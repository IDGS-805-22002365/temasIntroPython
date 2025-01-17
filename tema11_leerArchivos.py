from io import open

#Leer el contenido del archivo
fichero=open("fichero.txt","r")
texto=fichero.readline()
print(texto)


'''
texto=fichero.readlines()
print(texto)
print(type(texto))

for i in texto:
    print(i)
'''

'''
texto=fichero.read()
print(texto)

'''

'''
fichero.seek(0) #Se coloca el puntero al inicio del archivo para volver a leerlo
print(texto)
'''


fichero.close()