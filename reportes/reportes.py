#Ketcia Nicolle Larios de León
# MODULO DE REPORTES
"""
8. Levantamiento de Requisitos (Módulo Reportes):
- Requisito Funcional: Lectura global de las listas para generar estadísticas (Ej. Juegos más vendidos).
- Requisito No Funcional: Presentación limpia y organizada en consola.
9. Análisis de Requisitos:
- Priorización: Could Have. Permite auditoría visual del estado del negocio.
"""
# Referencias globales para evitar errores de linter
if 'pedidos' not in globals(): pedidos = []
if 'videojuegos' not in globals(): videojuegos = []
if 'detalles_pedido' not in globals(): detalles_pedido = []

print("\n--- REPORTES DE VENTAS ---")
total_ventas = 0.0
total_pedidos = len(pedidos)
if not pedidos:
    print("No hay ventas registradas.")
else:
    print(f"Total de Pedidos Realizados: {total_pedidos}")
    for p in pedidos:
        total_ventas += p['Total']
    print(f"Monto Total Recaudado: Q{total_ventas}")
    print("\nTop 5 Juegos Más Vendidos:")
    
    conteo_ventas = []
    for v in videojuegos:
        cant_vendida = 0
        for d in detalles_pedido:
            if d['ID_Videojuego'] == v['ID']:
                cant_vendida += d['Cantidad']
        if cant_vendida > 0:
            conteo_ventas.append({"Nombre": v['Nombre'], "Vendidos": cant_vendida})
    
    # Ordenamiento burbuja
    for i in range(len(conteo_ventas)):
        for j in range(0, len(conteo_ventas) - i - 1):
            if conteo_ventas[j]['Vendidos'] < conteo_ventas[j+1]['Vendidos']:
                conteo_ventas[j], conteo_ventas[j+1] = conteo_ventas[j+1], conteo_ventas[j]
    
    for item in conteo_ventas[:5]:
        print(f"- {item['Nombre']}: {item['Vendidos']} unidades")
print("")
