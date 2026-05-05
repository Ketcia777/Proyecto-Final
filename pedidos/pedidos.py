#Ketcia Nicolle Larios de León
# MODULO DE PEDIDOS
"""
8. Levantamiento de Requisitos (Módulo Pedidos):
- Requisito Funcional: Vinculación de un cliente a múltiples videojuegos, con total calculado.
- Requisito No Funcional: Validación de datos de forma imperativa.
9. Análisis de Requisitos:
- Priorización: Must Have. Representa el núcleo transaccional del sistema.
"""
# Referencias globales para evitar errores de linter
if 'clientes' not in globals(): clientes = []
if 'videojuegos' not in globals(): videojuegos = []
if 'pedidos' not in globals(): pedidos = []
if 'detalles_pedido' not in globals(): detalles_pedido = []

print("\n--- CREAR NUEVO PEDIDO ---")
if not clientes or not videojuegos:
    print("[Error] Se requieren clientes y videojuegos registrados para crear un pedido.")
else:
    nit_cliente = input("NIT del Cliente: ")
    cliente_actual = None
    for c in clientes:
        if c['Nit'] == nit_cliente:
            cliente_actual = c
            break
    
    if cliente_actual:
        print(f"Cliente: {cliente_actual['Nombre']} {cliente_actual['Apellido']}")
        id_pedido = "PED-" + str(len(pedidos) + 1).zfill(4)
        detalles_actuales = []
        total_pedido = 0.0
        
        agregando_items = True
        while agregando_items:
            id_v_pedido = input("\nID del Videojuego a comprar (o 'fin' para terminar): ")
            if id_v_pedido.lower() == 'fin':
                agregando_items = False
            else:
                v_encontrado = None
                for v in videojuegos:
                    if v['ID'] == id_v_pedido:
                        v_encontrado = v
                        break
                
                if v_encontrado:
                    if v_encontrado['Stock'] > 0:
                        cantidad = int(input(f"Cantidad ({v_encontrado['Stock']} disponibles): "))
                        if cantidad <= v_encontrado['Stock']:
                            precio_unit = v_encontrado['Precio']
                            subtotal = precio_unit * cantidad
                            
                            detalle = {
                                "ID_Detalle": "DET-" + str(len(detalles_pedido) + len(detalles_actuales) + 1).zfill(5),
                                "ID_Pedido": id_pedido,
                                "ID_Videojuego": v_encontrado['ID'],
                                "Cantidad": cantidad,
                                "Precio_Unitario": precio_unit
                            }
                            detalles_actuales.append(detalle)
                            v_encontrado['Stock'] -= cantidad
                            total_pedido += subtotal
                            print(f"Agregado: {v_encontrado['Nombre']} x{cantidad} = Q{subtotal}")
                        else:
                            print("[Error] Stock insuficiente.")
                    else:
                        print("[Error] Agotado.")
                else:
                    print("[Error] Videojuego no encontrado.")
        
        if detalles_actuales:
            nuevo_pedido = {
                "ID": id_pedido,
                "Fecha": "2026-04-24",
                "Estado": "Pendiente",
                "ID_Cliente": cliente_actual['ID'],
                "Total": total_pedido
            }
            pedidos.append(nuevo_pedido)
            for d in detalles_actuales:
                detalles_pedido.append(d)
            
            print("\n" + "-"*30)
            print(f"PEDIDO {id_pedido} CREADO")
            print(f"Total a Pagar: Q{total_pedido}")
            print("-" * 30)
        else:
            print("[Aviso] Pedido cancelado (sin items).")
    else:
        print("[Error] Cliente no encontrado.")
