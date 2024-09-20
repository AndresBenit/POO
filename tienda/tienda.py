class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos_disponibles = []

    def agregar_producto(self, producto):
        self.productos_disponibles.append(producto)

    def mostrar_productos(self):
        print(f'Productos disponibles en {self.nombre}:')
        for idx, producto in enumerate(self.productos_disponibles):
            print(f"{idx + 1}. {producto}")

    def procesar_compra(self, cliente):
        total = cliente.carrito.total()
        if total > 0:
            print(f'El total de la compra de {cliente.nombre} es: ${total}')
            cliente.carrito.mostrar_carrito()
        else:
            print("El carrito está vacío. No se puede procesar la compra.")
