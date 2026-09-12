from abc import ABC, abstractmethod

class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular(self, monto: float) -> float:
        pass

class SinDescuento(EstrategiaDescuento):
    def calcular(self, monto: float) -> float:
        return monto

class DescuentoEstudiante(EstrategiaDescuento):
    def calcular(self, monto: float) -> float:
        return monto * 0.90  # 10% de descuento

class DescuentoFijoCincoMil(EstrategiaDescuento):
    def calcular(self, monto: float) -> float:
        return max(0.0, monto - 5000.0)