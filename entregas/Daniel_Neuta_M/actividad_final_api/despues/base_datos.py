class BaseDatosRestaurante:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(BaseDatosRestaurante, cls).__new__(cls)
            cls._instancia.pedidos = []
            cls._instancia.contador_id = 1
        return cls._instancia

    def guardar_pedido(self, pedido_dict):
        pedido_dict["id"] = self.contador_id
        self.pedidos.append(pedido_dict)
        self.contador_id += 1
        return pedido_dict

    def obtener_pedidos(self):
        return self.pedidos