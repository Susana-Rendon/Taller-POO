class Estudiante:
    def __init__(self, nombre, edad, grado, materia_inicial=None):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materia = materia_inicial

    def inscribir_materia(self, materia):
        if self.materia is None:
            self.materia = materia
            print(f"Materia '{materia}' inscrita exitosamente para {self.nombre}.")
        else:
            print(f"{self.nombre} ya tiene inscrita la materia '{self.materia}'. Inscripción no permitida.")

    def mostrar_materia(self):
        if self.materia:
            print(f"{self.nombre} tiene inscrita la materia: {self.materia}.")
        else:
            print(f"{self.nombre} no tiene materias inscritas actualmente.")

    def actualizar_grado(self, nuevo_grado):
        print(f"Actualizando el grado de {self.nombre} de {self.grado} a {nuevo_grado}.")
        self.grado = nuevo_grado

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}, Materia: {self.materia or 'Ninguna'}")

def main():
    estudiante1 = Estudiante("Eduardo Rivera", 14, "9°", "Matemáticas")
    estudiante2 = Estudiante("Ana García", 15, "10°", "Ciencias")
    estudiante3 = Estudiante("Mia Marulanda", 13, "8°")

    estudiante1.mostrar_materia()
    estudiante1.inscribir_materia("Historia")
    estudiante1.actualizar_grado("10°")

    estudiante2.mostrar_materia()
    estudiante2.inscribir_materia("Física")
    estudiante2.actualizar_grado("11°")

    estudiante3.mostrar_materia()
    estudiante3.inscribir_materia("Arte")
    estudiante3.actualizar_grado("9°")

    print("\nInformación final del registro de los estudiantes:")
    estudiante1.mostrar_informacion()
    estudiante2.mostrar_informacion()
    estudiante3.mostrar_informacion()

if __name__ == "__main__":
    main()
