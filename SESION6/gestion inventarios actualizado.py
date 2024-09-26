# Diccionario para almacenar productos y sus cantidades
inventario = {}

# Función para agregar un producto al inventario
def agregar_producto(nombre, cantidad):
    if cantidad < 0:
        print("Error: No se puede agregar una cantidad negativa.")
        return
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad
    print(f'Se ha agregado {cantidad} de {nombre} al inventario.')

# Función para eliminar una cantidad específica de un producto
def eliminar_producto(nombre, cantidad):
    if nombre in inventario:
        if inventario[nombre] >= cantidad:
            inventario[nombre] -= cantidad
            print(f'Se ha eliminado {cantidad} de {nombre} del inventario.')
        else:
            inventario[nombre] = 0
            print(f'Se ha eliminado toda la cantidad de {nombre} del inventario.')
    else:
        print(f"Error: El producto '{nombre}' no está en el inventario.")

# Función para mostrar productos con cantidades bajas
def verificar_bajas(cantidad_minima):
    productos_bajos = {k: v for k, v in inventario.items() if v < cantidad_minima}
    if productos_bajos:
        print(f'Productos con cantidad menor a {cantidad_minima}: {list(productos_bajos.keys())}')
    else:
        print(f'No hay productos con cantidad menor a {cantidad_minima}.')

# Función para mostrar el inventario completo, ordenado alfabéticamente
def mostrar_inventario():
    print("Inventario:")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in sorted(inventario.keys()):
            print(f'{producto}: {inventario[producto]}')

# Función principal del programa que acepta comandos en línea
def gestionar_inventario():
    while True:
        comando = input("\nIngrese un comando (agregar, eliminar, mostrar, productos_bajos, salir): ")  # Captura la entrada del usuario
        partes = comando.split()

        if len(partes) == 0:
            continue

        accion = partes[0].lower()

        try:
            if accion == 'agregar' and len(partes) == 3:
                nombre = partes[1]
                cantidad = int(partes[2])
                agregar_producto(nombre, cantidad)

            elif accion == 'eliminar' and len(partes) == 3:
                nombre = partes[1]
                cantidad = int(partes[2])
                eliminar_producto(nombre, cantidad)

            elif accion == 'mostrar' and len(partes) == 2 and partes[1].lower() == 'inventario':
                mostrar_inventario()

            elif accion == 'productos_bajos' and len(partes) == 2:
                cantidad_minima = int(partes[1])
                verificar_bajas(cantidad_minima)

            elif accion == 'salir':
                print("Saliendo del programa.")
                break

            else:
                print("Comando no reconocido. Intente de nuevo.")
        
        except ValueError:
            print("Error: asegúrate de ingresar cantidades válidas.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    gestionar_inventario()
