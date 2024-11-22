class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print (f"El precio de {self.nombre} ha sido actualizado a {self.precio}.")

    def ajustar_inventario(self, cambio_cantidad):
        self.cantidad += cambio_cantidad
        print(f"La cantidad del producto '{self.nombre}' ahora es {self.cantidad}.")

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")

def main():
    # Crear objetos de la clase Producto
    producto1 = Producto("Camisas", 15000, 10)
    producto2 = Producto("Jean", 50000, 30)
    producto3 = Producto("Zapatos", 70000, 15)

    producto1.mostrar_informacion()
    producto1.actualizar_precio(20000)
    producto1.ajustar_inventario(-2)

    producto2.mostrar_informacion()
    producto2.actualizar_precio(45000)
    producto2.ajustar_inventario(10)

    producto3.mostrar_informacion()
    producto3.actualizar_precio(65000)
    producto3.ajustar_inventario(5)

    print("\nInformación final de los productos:")
    producto1.mostrar_informacion()
    producto2.mostrar_informacion()
    producto3.mostrar_informacion()


# Ejecutar el programa principal
if __name__ == "__main__":
    main()

