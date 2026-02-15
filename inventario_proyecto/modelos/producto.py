class Producto:
    """
    Clase que representa un producto en el inventario.
    """
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio(self):
        return self._precio

    # Setters
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre

    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa.")

    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo.")

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"