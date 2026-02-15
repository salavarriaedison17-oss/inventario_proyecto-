[main.py](https://github.com/user-attachments/files/25327907/main.py)
from modelos.producto import Producto
from servicios.inventario import Inventario

def mostrar_menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")

def pedir_datos_producto():
    id_producto = input("Ingrese ID del producto: ").strip()
    nombre = input("Ingrese nombre del producto: ").strip()
    
    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad < 0:
                raise ValueError
            break
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero mayor o igual a 0.")

    while True:
        try:
            precio = float(input("Ingrese precio: "))
            if precio < 0:
                raise ValueError
            break
        except ValueError:
            print("Precio inválido. Debe ser un número positivo.")

    return Producto(id_producto, nombre, cantidad, precio)

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            print("\nAñadir producto:")
            producto = pedir_datos_producto()
            if inventario.agregar_producto(producto):
                print("Producto añadido exitosamente.")
            else:
                print("Error: Ya existe un producto con ese ID.")

        elif opcion == '2':
            id_eliminar = input("Ingrese ID del producto a eliminar: ").strip()
            if inventario.eliminar_producto(id_eliminar):
                print("Producto eliminado exitosamente.")
            else:
                print("No se encontró el producto con ese ID.")

        elif opcion == '3':
            id_actualizar = input("Ingrese ID del producto a actualizar: ").strip()
            if any(p.id == id_actualizar for p in inventario.listar_productos()):
                # Pedir qué actualizar
                actualizar_cantidad = input("¿Desea actualizar la cantidad? (s/n): ").lower() == 's'
                cantidad = None
                if actualizar_cantidad:
                    while True:
                        try:
                            cantidad = int(input("Ingrese nueva cantidad: "))
                            if cantidad < 0:
                                raise ValueError
                            break
                        except ValueError:
                            print("Cantidad inválida. Debe ser un número entero mayor o igual a 0.")

                actualizar_precio = input("¿Desea actualizar el precio? (s/n): ").lower() == 's'
                precio = None
                if actualizar_precio:
                    while True:
                        try:
                            precio = float(input("Ingrese nuevo precio: "))
                            if precio < 0:
                                raise ValueError
                            break
                        except ValueError:
                            print("Precio inválido. Debe ser un número positivo.")

                exito = inventario.actualizar_producto(id_actualizar, cantidad, precio)
                if exito:
                    print("Producto actualizado exitosamente.")
                else:
                    print("Error al actualizar producto.")
            else:
                print("No se encontró el producto con ese ID.")

        elif opcion == '4':
            termino_busqueda = input("Ingrese nombre o parte del nombre a buscar: ").strip()
            resultados = inventario.buscar_productos(termino_busqueda)
            if resultados:
                print(f"\nProductos encontrados ({len(resultados)}):")
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos que coincidan con la búsqueda.")

        elif opcion == '5':
            productos = inventario.listar_productos()
            if productos:
                print("\nInventario completo:")
                for p in productos:
                    print(p)
            else:
                print("El inventario está vacío.")

        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
