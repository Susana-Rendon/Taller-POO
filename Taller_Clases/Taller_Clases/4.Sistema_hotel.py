class Habitacion:
    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def reservar(self):
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada exitosamente.")
        else:
            print(f"Error: La habitación {self.numero} ya está reservada.")

    def liberar(self):
        if not self.disponible:
            self.disponible = True
            print(f"Habitación {self.numero} liberada exitosamente.")
        else:
            print(f"Error: La habitación {self.numero} ya está disponible.")

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Habitación {self.numero} - Tipo: {self.tipo} - Precio: ${self.precio:.2f} - Estado: {estado}")


def main():
    habitacion1 = Habitacion(101, "Simple", 50.00)
    habitacion2 = Habitacion(102, "Doble", 75.00)
    habitacion3 = Habitacion(103, "Suite", 120.00)

    print("Información inicial de las habitaciones:")
    habitacion1.mostrar_informacion()
    habitacion2.mostrar_informacion()
    habitacion3.mostrar_informacion()

    print("\nRealizando operaciones:")
    habitacion1.reservar()
    habitacion1.reservar()
    habitacion2.reservar()
    habitacion1.liberar()
    habitacion1.liberar()

    print("\nInformación final de las habitaciones:")
    habitacion1.mostrar_informacion()
    habitacion2.mostrar_informacion()
    habitacion3.mostrar_informacion()


if __name__ == "__main__":
    main()
