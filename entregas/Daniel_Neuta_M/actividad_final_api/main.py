from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from despues.productos import FabricaProductos
from despues.adiciones import ConQuesoExtra, ConTocineta
from despues.estrategias_descuentos import SinDescuento, DescuentoEstudiante, DescuentoFijoCincoMil
from despues.pedido import GestorPedidos
from despues.base_datos import BaseDatosRestaurante

app = FastAPI(
    title="API Restaurante - Refactorización con Patrones GoF",
    version="1.0.0"
)

gestor = GestorPedidos()
db = BaseDatosRestaurante()

class SolicitudPedido(BaseModel):
    cliente: str
    producto: str  # "hamburguesa" o "pizza"
    adiciones: Optional[List[str]] = []  # ["queso", "tocino"]
    descuento: Optional[str] = "ninguno"  # "estudiante", "cupon_5k", "ninguno"

@app.get("/")
def inicio():
    return {"mensaje": "API de Gestión de Pedidos lista. Ve a /docs para interactuar."}

@app.post("/pedidos/", status_code=201)
def crear_pedido(solicitud: SolicitudPedido):
    try:
        # Factory
        prod = FabricaProductos.crear_producto(solicitud.producto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Decorator
    if solicitud.adiciones:
        for adic in solicitud.adiciones:
            adic_lower = adic.lower()
            if adic_lower in ["queso", "queso extra"]:
                prod = ConQuesoExtra(prod)
            elif adic_lower in ["tocino", "tocineta"]:
                prod = ConTocineta(prod)

    # Strategy
    desc_type = solicitud.descuento.lower() if solicitud.descuento else "ninguno"
    if desc_type == "estudiante":
        estrategia = DescuentoEstudiante()
    elif desc_type in ["cupon_5k", "cupon"]:
        estrategia = DescuentoFijoCincoMil()
    else:
        estrategia = SinDescuento()

    pedido_creado = gestor.procesar_pedido(solicitud.cliente, prod, estrategia)
    return pedido_creado

@app.get("/pedidos/")
def listar_pedidos():
    return db.obtener_pedidos()