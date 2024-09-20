class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        if producto.cantidad >= cantidad:
            self.productos.append((producto, cantidad))
            producto.cantidad -= cantidad
            print(f'Agregado {cantidad} de {producto.nombre} al carrito.')
        else:
            print(f"No hay suficiente stock de {producto.nombre}")

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío")
        else:
            print("Carrito de compras:")
            for producto, cantidad in self.productos:
                print(f'{producto.nombre} - {cantidad} unidades - Total: ${producto.precio * cantidad}')

    def total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.productos)


