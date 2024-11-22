class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def conducir(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            print(f"Se han añadido {kilometros} km al vehículo {self.marca} {self.modelo}.")
        else:
            print("Los kilómetros deben ser valores positivos.")

    def mostrar_detalles(self):
        print(f"El vehículo de marca {self.marca} y modelo {self.modelo}, fabricado en el año {self.año}, tiene un kilometraje de: {self.kilometraje} km.")

    def es_vehiculo_antiguo(self):
        from datetime import datetime
        año_actual = datetime.now().year
        return (año_actual - self.año) > 20

def main():
    # Crear instancias de Vehiculo
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2021, 150000)
    vehiculo2 = Vehiculo("Ford", "Focus", 2015, 60000)
    vehiculo3 = Vehiculo("Chevrolet", "Spark", 1995, 180000)

    print("Detalles iniciales de los vehículos:")
    vehiculo1.mostrar_detalles()
    vehiculo2.mostrar_detalles()
    vehiculo3.mostrar_detalles()

    vehiculo1.conducir(500)
    vehiculo2.conducir(300)
    vehiculo3.conducir(50)

    print("\nDetalles después de conducir:")
    vehiculo1.mostrar_detalles()
    vehiculo2.mostrar_detalles()
    vehiculo3.mostrar_detalles()

    print("\n¿Son vehículos antiguos?")
    print(f"{vehiculo1.marca} {vehiculo1.modelo}: {'Sí' if vehiculo1.es_vehiculo_antiguo() else 'No'}")
    print(f"{vehiculo2.marca} {vehiculo2.modelo}: {'Sí' if vehiculo2.es_vehiculo_antiguo() else 'No'}")
    print(f"{vehiculo3.marca} {vehiculo3.modelo}: {'Sí' if vehiculo3.es_vehiculo_antiguo() else 'No'}")

if __name__ == "__main__":
    main()

