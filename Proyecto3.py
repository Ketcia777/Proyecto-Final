#Ketcia Nicolle Larios de León
# ==============================================================================
# SISTEMA DE GESTIÓN DE PEDIDOS PARA EMPRESA DE VENTA DE VIDEOJUEGOS (SGP-VG)
# ==============================================================================

"""
4) DIAGRAMA ENTIDAD RELACIÓN (Descripción)
- CLIENTE (1) -- (*) PEDIDO
- VIDEOJUEGO (1) -- (*) DETALLE_PEDIDO
- PEDIDO (1) -- (*) DETALLE_PEDIDO
- PEDIDO (1) -- (1) PAGO
- PEDIDO (1) -- (1) ENVÍO

5) FASES DEL PROYECTO
1. Análisis y Estructura
2. Módulo de Clientes (Carpeta: clientes)
3. Módulo de Inventario (Carpeta: videojuegos)
4. Módulo de Pedidos (Carpeta: pedidos)
5. Módulo de Detalles (Carpeta: detalles)
6. Módulo de Pagos (Carpeta: pagos)
7. Módulo de Logística (Carpeta: envios)
8. Reportes y Cierre (Carpeta: reportes)

6) OBJETIVOS DEL PROYECTO
- Gestionar eficientemente clientes y stock de videojuegos mediante modularización.
- Automatizar el procesamiento de pedidos y facturación.
- Seguimiento modular de estados de pedido y envío.

7) ALCANCE DEL PROYECTO
- Sistema modular separado por carpetas para cada entidad.
- CRUD de Clientes y Videojuegos.
- Creación de pedidos con detalle y cálculo de total.
- Registro de pagos y gestión de estados de envío.

8) LEVANTAMIENTO DE REQUISITOS
- Requisitos Funcionales: Gestión CRUD completa y en memoria de Clientes, Videojuegos, Pedidos, Detalles (con validación de inventario/ACID manual), Pagos, Envíos y Reportes.
- Restricción Transversal: Prohibido el uso de funciones ('def') o clases. Todo operado mediante ámbito global ('globals()').
- Requisitos No Funcionales: Ejecución 100% consola, navegación por menú numérico y variables mantenibles.

9) ANÁLISIS DE REQUISITOS
- Priorización: Integración imperativa de módulos y transaccionalidad de stock en memoria son "Must Have".
- Validación: Reversión y resta lineal del inventario evaluada de forma iterativa y estrictamente procedimental.
"""

# LISTAS GLOBALES (Base de Datos en Memoria)
clientes = []
videojuegos = []
pedidos = []
detalles_pedido = []
pagos = []
envios = []

# VARIABLES DE CONTROL
continuar_sistema = True

while continuar_sistema:
    print("\n" + "="*50)
    print("      SISTEMA DE GESTIÓN DE PEDIDOS SGP-VG")
    print("="*50)
    print("1. Gestión de Clientes")
    print("2. Catálogo de Videojuegos")
    print("3. Crear Nuevo Pedido")
    print("4. Ver Detalles de Pedido")
    print("5. Registrar Pago")
    print("6. Gestionar Envío")
    print("7. Reportes de Ventas")
    print("8. Salir")
    print("="*50)
    
    opcion_principal = input("Seleccione una opción: ")
    
    match opcion_principal:
        case "1":
            # Llamar al módulo de clientes
            exec(open('clientes/clientes.py', encoding='utf-8').read(), globals())
            
        case "2":
            # Llamar al módulo de videojuegos
            exec(open('videojuegos/videojuegos.py', encoding='utf-8').read(), globals())
            
        case "3":
            # Llamar al módulo de pedidos
            exec(open('pedidos/pedidos.py', encoding='utf-8').read(), globals())
            
        case "4":
            # Llamar al módulo de detalles
            exec(open('detalles/detalles.py', encoding='utf-8').read(), globals())
            
        case "5":
            # Llamar al módulo de pagos
            exec(open('pagos/pagos.py', encoding='utf-8').read(), globals())
            
        case "6":
            # Llamar al módulo de envíos
            exec(open('envios/envios.py', encoding='utf-8').read(), globals())
            
        case "7":
            # Llamar al módulo de reportes
            exec(open('reportes/reportes.py', encoding='utf-8').read(), globals())

        case "8":
            print("\nGracias por usar SGP-VG. Cerrando sistema...")
            continuar_sistema = False
            
        case _:
            print("[Error] Opción no válida.")
