#Ketcia Nicolle Larios de León
# ==============================================================================
# SISTEMA DE GESTIÓN DE PEDIDOS PARA EMPRESA DE VENTA DE VIDEOJUEGOS (SGP-VG)
# ==============================================================================

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
