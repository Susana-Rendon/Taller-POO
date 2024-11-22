class Factura:
    def __init__(self, numero, cliente, fecha):
        self.numero = numero
        self.cliente = cliente
        self.fecha = fecha
        self.monto_total = 0
        self.items = []

    def agregar_item(self, descripcion, cantidad, precio_unitario):
        subtotal = cantidad * precio_unitario
        self.items.append({"descripcion": descripcion, "cantidad": cantidad, "precio_unitario": precio_unitario, "subtotal": subtotal})
        self.monto_total += subtotal
        print(f"Se ha añadido el item '{descripcion}' con cantidad {cantidad} y subtotal {subtotal:.2f}.")

    def mostrar_detalles(self):
        print(f"Factura con número: {self.numero} por el Cliente: {self.cliente} de la fecha: {self.fecha}")

        print("Detalles de los items:")
        for item in self.items:
            print(f"{item['descripcion']}: {item['cantidad']} x {item['precio_unitario']:.2f} = {item['subtotal']:.2f}")
        print(f"\nMonto Total: {self.monto_total:.2f}")

    def aplicar_descuento(self, porcentaje):
        descuento = self.monto_total * (porcentaje / 100)
        self.monto_total -= descuento
        print(f"Se ha aplicado un descuento del {porcentaje}%. Monto final: {self.monto_total:.2f}")


def main():
    factura1 = Factura("001", "Juan Pérez", "2024-11-22")

    print("Agregando items a la factura:")
    factura1.agregar_item("Monitor", 2, 250.00)
    factura1.agregar_item("Teclado", 1, 45.00)
    factura1.agregar_item("Ratón", 1, 25.00)

    print("Detalles de la factura:")
    factura1.mostrar_detalles()

    print("Aplicar descuento:")
    factura1.aplicar_descuento(10)

    print("Detalles finales de la factura:")
    factura1.mostrar_detalles()


if __name__ == "__main__":
    main()
