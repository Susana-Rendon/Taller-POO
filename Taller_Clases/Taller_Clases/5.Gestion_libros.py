class Libro:
    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Se ha aplicado un descuento del {porcentaje}% al libro {self.titulo} y su precio final es: {self.precio:.2f} pesos.")

    def mostrar_detalles(self):
        print(f"El libro '{self.titulo}' escrito por {self.autor}, del género {self.genero}, tiene un valor de {self.precio:.2f} pesos.")

    def es_mas_caro_que(self, otro_libro):
        return self if self.precio > otro_libro.precio else otro_libro


def main():
    # Crear instancias de libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 50000)
    libro2 = Libro("1984", "George Orwell", "Distopía", 30000)
    libro3 = Libro("El Quijote", "Miguel de Cervantes", "Aventura", 45000)

    print("Información de los libros:")
    libro1.mostrar_detalles()
    libro2.mostrar_detalles()
    libro3.mostrar_detalles()

    print("\nAplicar descuento:")
    libro2.aplicar_descuento(10)
    libro3.aplicar_descuento(20)

    print("\nComparar precios:")
    mas_caro = libro1.es_mas_caro_que(libro3)
    print(f"El libro más caro es: '{mas_caro.titulo}' con un precio de {mas_caro.precio} pesos.")


if __name__ == "__main__":
    main()
