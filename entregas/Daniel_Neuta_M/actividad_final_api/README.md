# Sistema de gestión de restaurantes FastAPI

Sistema de gestión de pedidos para un restaurante desarrollado en **FastAPI**, diseñado con un enfoque modular y aplicando **5 patrones de diseño** para garantizar escalabilidad, bajo acoplamiento y mantenibilidad.

## Patrones de Diseño Implementados

- **Singleton (`despues/base_datos.py`)**: Garantiza un único punto de acceso al almacenamiento central de datos en memoria durante el ciclo de vida de la aplicación.
- **Factory Method (`despues/productos.py`)**: Encapsula la lógica de creación de los productos base (ej. Hamburguesas, Pizzas) asignando sus propiedades iniciales de forma limpia.
- **Decorator (`despues/adiciones.py`)**: Permite agregar adiciones e ingredientes extras dinámicamente a los platillos recalculando el costo total.
- **Estrategia (`despues/estrategias_descuentos.py`)**: Define algoritmos intercambiables para la aplicación de descuentos en tiempo de ejecución.
- **Observer (`despues/sistema_notificacion.py`)**: Sistema de suscripción y eventos que notifica de forma automática a la cocina y caja cuando el estado de un pedido cambia.

## Estructura del Proyecto

- `main.py`: Punto de entrada de la aplicación FastAPI y definición de rutas.
- `antes/codigo_legacy.py`: Código original sin refactorizar (para comparación y contraste).
- `despues/`: Módulos refactorizados que contienen la implementación limpia de los patrones y la lógica de negocio.

## Ejecución del Proyecto

Para iniciar el servidor de desarrollo local con Uvicorn:

```bash
uvicorn main:app --reload
