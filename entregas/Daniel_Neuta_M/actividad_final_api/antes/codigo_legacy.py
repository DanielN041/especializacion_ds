class RestauranteMonolitico:
    def __init__(self):
        self.productos = {
            "hamburguesa": 20000,
            "pizza": 25000,
            "gaseosa": 5000
        }
        self.pedidos = []

    def crear_pedido(self, cliente, tipo_producto, adiciones=None, tipo_descuento=None):
        if tipo_producto not in self.productos:
            return "Producto no disponible"

        precio_base = self.productos[tipo_producto]
        total = precio_base

        # Lógica acoplada de adiciones
        if adiciones:
            if "queso" in adiciones:
                total += 3000
            if "tocineta" in adiciones:
                total += 4000

        # Lógica acoplada de descuentos
        if tipo_descuento == "estudiante":
            total *= 0.90
        elif tipo_descuento == "cupon_10":
            total -= 5000

        pedido = {
            "id": len(self.pedidos) + 1,
            "cliente": cliente,
            "producto": tipo_producto,
            "total": total
        }
        self.pedidos.append(pedido)

        # Notificación acoplada
        print(f"Notificando a {cliente}: Su pedido #{pedido['id']} por ${total} ha sido creado.")
        return pedido