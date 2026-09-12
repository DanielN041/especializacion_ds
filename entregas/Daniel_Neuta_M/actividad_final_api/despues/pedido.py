from despues.productos import Producto
from despues.estrategias_descuentos import EstrategiaDescuento
from despues.sistema_notificacion import SujetoNotificaciones, ClienteNotificable
from despues.base_datos import BaseDatosRestaurante

class GestorPedidos:
    def __init__(self):
        self.db = BaseDatosRestaurante()

    def procesar_pedido(self, cliente_nombre: str, producto: Producto, estrategia_descuento: EstrategiaDescuento):
        precio_original = producto.obtener_precio()
        precio_final = estrategia_descuento.calcular(precio_original)

        # Observer
        notificador = SujetoNotificaciones()
        cliente_obs = ClienteNotificable(cliente_nombre)
        notificador.suscribir(cliente_obs)

        # Datos del pedido
        datos_pedido = {
            "cliente": cliente_nombre,
            "descripcion": producto.obtener_nombre(),
            "precio_original": precio_original,
            "precio_final": precio_final
        }

        # Singleton DB
        pedido_guardado = self.db.guardar_pedido(datos_pedido)

        # Notificar
        notificador.notificar(f"Su pedido #{pedido_guardado['id']} ({producto.obtener_nombre()}) fue procesado por ${precio_final}.")

        return pedido_guardado