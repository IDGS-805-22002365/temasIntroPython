#Listas

'''
lista1=[10,5,3]
lista2=[1,5,2.66,1.70,89.2]
lista3=["Lunes","Martes","Miercoles"]
lista4=["Juan",45,1.92]

print(type(lista1))
print(len(lista2))

print(lista1[0])

suma=0
x=0
while x < len(lista1):
    suma=suma+lista1[x]
    x+=1
print("La suma de la lista es:{}".format(suma))

print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])

lista5=[]
for x in range(5):
    valor=int(input("Ingrese un valor: "))
    lista5.append(valor)
print(lista5)

#eliminar un elemento de la lista
print(lista1)
lista1.pop()
print(lista1)
'''

'''
crear un programa donde me pida un numero que sera el numero de objetos que se agregara 
la salida sera:
numeros pares de la lista: aaaaa
numeros impares de la lista: bbbbb
'''
lista1=[]
n=int(input("Ingrese el numero de objetos que tendra la lista: "))
numeros = []

for x in range(n):  
    valor=int(input("Ingrese un valor: "))
    numeros.append(valor)
    cantidadImpares=[]
    cantidadPar=[]   
for valor in numeros:
    # lista1.append(valor)
    if valor % 2 == 0:
        cantidadPar.append(valor)
    else:
        cantidadImpares.append(valor)
        
print("numeros pares de la lista: ",cantidadPar)
print("numeros impares de la lista: ",cantidadImpares)

'''
'''
lista1.sort()
print(lista1)
lista1.remove(10)
print(lista1)

lista1.remove(10)
print(lista1)   

lista1.clear()
print(lista1)
'''
'''


