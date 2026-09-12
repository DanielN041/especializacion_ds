from abc import ABC, abstractmethod

class Producto(ABC):
    @abstractmethod
    def obtener_nombre(self) -> str:
        pass

    @abstractmethod
    def obtener_precio(self) -> float:
        pass

class Hamburguesa(Producto):
    def obtener_nombre(self) -> str:
        return "Hamburguesa Artesanal"

    def obtener_precio(self) -> float:
        return 20000.0

class Pizza(Producto):
    def obtener_nombre(self) -> str:
        return "Pizza Personal"

    def obtener_precio(self) -> float:
        return 25000.0

class FabricaProductos:
    @staticmethod
    def crear_producto(tipo: str) -> Producto:
        tipo_lower = tipo.lower()
        if tipo_lower == "hamburguesa":
            return Hamburguesa()
        elif tipo_lower == "pizza":
            return Pizza()
        else:
            raise ValueError(f"Producto '{tipo}' no reconocido en el menú.")