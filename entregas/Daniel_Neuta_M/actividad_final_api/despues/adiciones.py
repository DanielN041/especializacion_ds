from despues.productos import Producto

class DecoradorProducto(Producto):
    def __init__(self, producto: Producto):
        self._producto = producto

class ConQuesoExtra(DecoradorProducto):
    def obtener_nombre(self) -> str:
        return f"{self._producto.obtener_nombre()} + Queso Extra"

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio() + 3000.0

class ConTocineta(DecoradorProducto):
    def obtener_nombre(self) -> str:
        return f"{self._producto.obtener_nombre()} + Tocineta"

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio() + 4000.0