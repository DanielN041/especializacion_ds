from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str):
        pass

class ClienteNotificable(Observador):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.ultimas_notificaciones = []

    def actualizar(self, mensaje: str):
        texto = f"Notificación para {self.nombre}: {mensaje}"
        self.ultimas_notificaciones.append(texto)
        print(texto)

class SujetoNotificaciones:
    def __init__(self):
        self._observadores = []

    def suscribir(self, observador: Observador):
        self._observadores.append(observador)

    def notificar(self, mensaje: str):
        for obs in self._observadores:
            obs.actualizar(mensaje)