import os

def funcion1():
    os.system("cls")
    print("Hola soy la funcion 1")

def funcion2():
    print("Hola soy la funcion 2")
   
    
# llamar funcion
"""
op=int(input("numero: "))
if op==1:
           funcion1()
else:
        funcion2
"""


        
def funcion3():
    os.system("cls")
    print("Dame dos numeros: ")
    num1= int(input("Primer numero: "))
    num2= int(input("Segundo numero: "))
    res=num1+num2
    print(f"El resultado es:{res}")
    

def run():
    os.system("cls")
    print("Menu de opciones")
    print("1. Suma de dos numeros")
    print("2. Otra opcion")
    print("3. Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1:
        funcion3()
    if opcion==2:
        funcion2()
        
if __name__ == "__main__":
    run()
