#Ketcia Nicolle Larios de León
# MODULO DE DETALLES DEL PEDIDO
"""
8. Levantamiento de Requisitos (Módulo Detalles):
- Requisito Funcional: Registro de items de pedido y actualización lineal del inventario.
- Requisito No Funcional: Garantizar la integridad de los datos compartidos.
9. Análisis de Requisitos:
- Priorización: Must Have. Es indispensable para la simulación ACID (descuento de stock en memoria).
"""
# Referencias globales para evitar errores de linter
if 'pedidos' not in globals(): pedidos = []
if 'detalles_pedido' not in globals(): detalles_pedido = []
if 'videojuegos' not in globals(): videojuegos = []

print("\n--- CONSULTAR DETALLES DE PEDIDO ---")
id_p_consulta = input("Ingrese ID del Pedido (PED-XXXX): ")
encontrado_p = False
for p in pedidos:
    if p['ID'] == id_p_consulta:
        encontrado_p = True
        print(f"\nDETALLES DEL PEDIDO: {p['ID']}")
        print(f"Cliente: {p['ID_Cliente']} | Fecha: {p['Fecha']} | Total: Q{p['Total']}")
        print("-" * 40)
        print(f"{'ID Detalle':<12} | {'Producto':<20} | {'Cant':<5} | {'Precio':<10}")
        print("-" * 40)
        for d in detalles_pedido:
            if d['ID_Pedido'] == id_p_consulta:
                # Buscar nombre del juego
                nombre_juego = "Desconocido"
                for v in videojuegos:
                    if v['ID'] == d['ID_Videojuego']:
                        nombre_juego = v['Nombre']
                        break
                print(f"{d['ID_Detalle']:<12} | {nombre_juego:<20} | {d['Cantidad']:<5} | Q{d['Precio_Unitario']:<10}")
        break

if not encontrado_p:
    print("[Error] Pedido no encontrado.")
print("")
