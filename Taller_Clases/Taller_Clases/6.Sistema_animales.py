class Animal:
    def __init__(self, nombre, especie, edad, habitat):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def cumplir_años(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años.")

    def cambiar_habitat(self, nuevo_habitat):
        print(f"{self.nombre} ha sido trasladado del hábitat '{self.habitat}' al hábitat '{nuevo_habitat}'.")
        self.habitat = nuevo_habitat

    def mostrar_detalles(self):
        print(f"Su nombre es: {self.nombre} pertenece a la especie: {self.especie} tiene: {self.edad} años  y su hábitat natural es: {self.habitat}")


def main():
    animal1 = Animal("Leo", "León", 5, "Sabana")
    animal2 = Animal("Paco", "Loro", 2, "Selva")
    animal3 = Animal("Luna", "Oso polar", 8, "Ártico")

    print("Detalles iniciales de los animales:")
    animal1.mostrar_detalles()
    animal2.mostrar_detalles()
    animal3.mostrar_detalles()

    print("\nCumpliendo años:")
    animal1.cumplir_años()
    animal3.cumplir_años()

    print("\nCambiar hábitat:")
    animal2.cambiar_habitat("Aviario tropical")

    print("\nDetalles finales de los animales:")
    animal1.mostrar_detalles()
    animal2.mostrar_detalles()
    animal3.mostrar_detalles()


if __name__ == "__main__":
    main()
