# FastAPI Restaurant Management System

Sistema de gestión de pedidos para un restaurante desarrollado en **FastAPI**, diseñado con un enfoque modular y aplicando **5 patrones de diseño** para garantizar escalabilidad, bajo acoplamiento y mantenibilidad.


#  Patrones de Diseño Implementados

* **Singleton (base_datos.py):** Garantiza un único punto de acceso al almacenamiento central de datos en memoria durante el ciclo de vida de la aplicación.
* **Factory Method (factories.py):** Encapsula la lógica de creación de los productos base (ej. Hamburguesas, Pizzas) asignando sus propiedades iniciales de forma limpia.
* **Decorator (decoradores.py):** Permite añadir adiciones e ingredientes extras (ej. Queso, Tocineta) dinámicamente a los platillos recalculando el costo total.
* **Strategy (estrategias.py):** Define algoritmos intercambiables para la aplicación de descuentos (ej. Descuento Estudiante, Tarifa Normal) en tiempo de ejecución.
* **Observer (observadores.py):** Sistema de suscripción y eventos que notifica de forma automática a la cocina y caja cuando el estado de un pedido cambia.


# Ejecución del Proyecto

Para iniciar el servidor de desarrollo local con Uvicorn:

uvicorn main:app --reload

El servidor quedará disponible en `http://127.0.0.1:8000`.


# Documentación Interactiva (Swagger UI)

Prueba de endpoints y flujo de patrones en tiempo de ejecución:

 **URL:** `http://127.0.0.1:8000/docs`


#  Arquitectura y Evolución
Actualmente, la persistencia utiliza un almacén en memoria RAM respaldado por **Singleton** para fines del laboratorio. La estructura está totalmente desacoplada y lista para integrar persistencia relacional (PostgreSQL / SQLite) mediante **Adapter / Repository Factory** sin modificar la lógica de negocio ni los patrones existentes.