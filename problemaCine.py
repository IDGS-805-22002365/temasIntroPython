import os

class Persona:
    def __init__(self, nombre, total):
        self.nombre = nombre
        self.total = total

class Boleto:
    def __init__(self):
        self.boletosPorPersona = 7
        self.precioBoleto = 12.00
        
    def ComprarBoletos(self):
        nombre = input("Ingresa tu nombre: ")
        while True:
            grupoPersonas = int(input("¿Cuántas personas van a comprar boletos? "))
            numBoletos = int(input("¿Cuántos boletos deseas comprar? "))

            # Validación de boletos y personas
            while not self.validacionPersonasBoleto(grupoPersonas, numBoletos):
                print("Datos inválidos. Por favor, ingresa una cantidad de boletos/personas adecuada.")
                print("¿Deseas cambiar el número de personas?")
                if input("Si/No: ").strip().lower() == "si":
                    grupoPersonas = int(input("¿Cuántas personas van a comprar boletos? "))
                print("¿Deseas cambiar el número de boletos?")
                if input("Si/No: ").strip().lower() == "si":
                    numBoletos = int(input("¿Cuántos boletos deseas comprar? "))

            total = numBoletos * self.precioBoleto
            total = self.descuentos(numBoletos, total)

            # Descuento adicional por tarjeta CIENCO
            print("¿Desea pagar con tarjeta CIENCO?")
            if input("Si/No: ").strip().lower() == "si":
                total = self.desCuentoTarjetaCinco(total)
            else:
                print("No se aplicó descuento.")

            print(f"Total a pagar: {total}")
            return Persona(nombre, total)

    def validacionPersonasBoleto(self, grupoPersonas, numBoletos):
        if numBoletos > grupoPersonas * self.boletosPorPersona:
            print(f"No se pueden comprar más de {self.boletosPorPersona} boletos por persona.")
            return False
        return True

    def descuentos(self, numBoletos, total):
        if numBoletos > 5:
            descuento = total * 0.15
            total -= descuento
            print("Se aplicó un descuento del 15%.")
        elif 3 <= numBoletos <= 5:
            descuento = total * 0.10
            total -= descuento
            print("Se aplicó un descuento del 10%.")
        return total

    def desCuentoTarjetaCinco(self, total):
        descuento = total * 0.10
        total -= descuento
        print("Se aplicó un descuento del 10% por pagar con tarjeta CIENCO.")
        return total

def ticket(listaPersonas):
    totalGeneral = 0
    with open("ticket.txt", "w") as fichero:
        fichero.write("----- Ticket de Compras -----\n")
        for persona in listaPersonas:
            fichero.write(f"Nombre: {persona.nombre}\n")
            fichero.write(f"Total a pagar: {persona.total}\n")
            fichero.write("\n")
            totalGeneral += persona.total
        fichero.write(f"Total general: {totalGeneral}\n")
    print("\nTicket generado con éxito.")
    print("----- Ticket de Compras -----")
    for persona in listaPersonas:
        print(f"Nombre: {persona.nombre}")
        print(f"Total: {persona.total}")
    print(f"Total general: {totalGeneral}")
    print("\n")

def run():
    sistema = Boleto()
    while True:
        print("Menú de opciones")
        print("1. Comprar boletos")
        print("2. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            listaPersonas = []
            while True:
                datosPersona = sistema.ComprarBoletos()
                listaPersonas.append(datosPersona)
                if input("¿Desea hacer otra compra? Si/No: ").strip().lower() != "si":
                    ticket(listaPersonas)
                    break
        elif opcion == 2:
            break
        else:
            print("Opción no válida, intente de nuevo")

if __name__ == "__main__":
    run()
