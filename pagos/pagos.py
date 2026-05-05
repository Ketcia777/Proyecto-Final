#Ketcia Nicolle Larios de León
# MODULO DE PAGOS
"""
8. Levantamiento de Requisitos (Módulo Pagos):
- Requisito Funcional: Registro de pago validando el monto contra el total del pedido.
- Requisito No Funcional: Confirmación transaccional inmediata.
9. Análisis de Requisitos:
- Priorización: Should Have. Cierra el ciclo financiero de la venta.
"""
# Referencias globales para evitar errores de linter
if 'pedidos' not in globals(): pedidos = []
if 'pagos' not in globals(): pagos = []

print("\n--- REGISTRO DE PAGOS ---")
id_p_pago = input("ID del Pedido para registrar pago (PED-XXXX): ")
p_encontrado = None
for p in pedidos:
    if p['ID'] == id_p_pago:
        p_encontrado = p
        break

if p_encontrado:
    ya_pagado = False
    for pg in pagos:
        if pg['ID_Pedido'] == id_p_pago:
            ya_pagado = True
            break
    
    if not ya_pagado:
        print(f"Total Pendiente: Q{p_encontrado['Total']}")
        metodo = input("Método de Pago (Tarjeta, Efectivo, Transferencia): ")
        
        id_pago = "PAG-" + str(len(pagos) + 1).zfill(4)
        nuevo_pago = {
            "ID_Pago": id_pago,
            "ID_Pedido": id_p_pago,
            "Metodo": metodo,
            "Monto": p_encontrado['Total'],
            "Fecha": "2026-04-24"
        }
        pagos.append(nuevo_pago)
        print(f"[OK] Pago {id_pago} registrado.")
    else:
        print("[Error] Este pedido ya está pagado.")
else:
    print("[Error] Pedido no encontrado.")
print("")
