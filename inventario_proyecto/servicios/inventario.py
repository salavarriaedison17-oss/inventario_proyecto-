from modelos.producto import Producto

class Inventario:
    """
    Clase que gestiona el inventario de productos.
    """
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Añade un producto si el ID no está repetido.
        Retorna True si se agregó, False si ya existía.
        """
        if any(p.id == producto.id for p in self._productos):
            return False
        self._productos.append(producto)
        return True

    def eliminar_producto(self, id_producto: str) -> bool:
        """
        Elimina un producto por ID. Retorna True si se eliminó, False si no se encontró.
        """
        for i, p in enumerate(self._productos):
            if p.id == id_producto:
                del self._productos[i]
                return True
        return False

    def actualizar_producto(self, id_producto: str, cantidad: int = None, precio: float = None) -> bool:
        """
        Actualiza cantidad y/o precio de un producto por ID.
        Retorna True si se actualizó, False si no se encontró.
        """
        for producto in self._productos:
            if producto.id == id_producto:
                if cantidad is not None:
                    try:
                        producto.cantidad = cantidad
                    except ValueError as e:
                        print(f"Error al actualizar cantidad: {e}")
                        return False
                if precio is not None:
                    try:
                        producto.precio = precio
                    except ValueError as e:
                        print(f"Error al actualizar precio: {e}")
                        return False
                return True
        return False

    def buscar_productos(self, nombre_parcial: str):
        """
        Busca productos cuyo nombre contenga el texto parcial (case insensitive).
        Retorna una lista de productos que coinciden.
        """
        nombre_parcial = nombre_parcial.lower()
        return [p for p in self._productos if nombre_parcial in p.nombre.lower()]

    def listar_productos(self):
        """
        Retorna la lista completa de productos en el inventario.
        """
        return self._productos