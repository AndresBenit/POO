from tienda.producto import Producto
from tienda.cliente import Cliente
from tienda.tienda import Tienda

p1 = Producto('Laptop', 1500, 5)
p2 = Producto('Smartphone', 800, 10)
p3 = Producto('Audífonos', 100, 15)


mi_tienda = Tienda('Tech Store')


mi_tienda.agregar_producto(p1)
mi_tienda.agregar_producto(p2)
mi_tienda.agregar_producto(p3)


cliente1 = Cliente(input("Introduce tu nombre: "))


def mostrar_menu():
    print("-------------------------------------")
    print("-----BIENVENIDO A TECHDONBENITO------")
    print("-------------------------------------")
    print("1. Ver productos disponibles")
    print("2. Ver carrito")
    print("3. Procesar compra")
    print("4. Salir")


def ver_productos_y_opcion():
    mi_tienda.mostrar_productos()
    agregar = input("¿Deseas agregar un producto al carrito? (s/n): ").lower()
    if agregar == 's':
        agregar_al_carrito()

def agregar_al_carrito():
    producto_num = int(input("Selecciona el número del producto que deseas agregar: ")) - 1
    cantidad = int(input("Introduce la cantidad: "))
    if 0 <= producto_num < len(mi_tienda.productos_disponibles):
        producto_seleccionado = mi_tienda.productos_disponibles[producto_num]
        cliente1.carrito.agregar_producto(producto_seleccionado, cantidad)
    else:
        print("-------------------")
        print("Producto no válido.")
        print("-------------------")

def ver_carrito():
    cliente1.carrito.mostrar_carrito()

def procesar_compra():
    mi_tienda.procesar_compra(cliente1)


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == '1':
        ver_productos_y_opcion()
    elif opcion == '2':
        ver_carrito()
    elif opcion == '3':
        procesar_compra()
    elif opcion == '4':
        print("Gracias por visitar la tienda. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

