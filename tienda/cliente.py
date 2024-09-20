from tienda.carrito import Carrito

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = Carrito()

    def __str__(self):
        return f'Cliente: {self.nombre}'
