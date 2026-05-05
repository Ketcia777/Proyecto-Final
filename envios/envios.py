#Ketcia Nicolle Larios de León
# MODULO DE ENVIOS
"""
8. Levantamiento de Requisitos (Módulo Envíos):
- Requisito Funcional: Seguimiento logístico actualizando el estado de envío.
- Requisito No Funcional: Consistencia de las direcciones respecto al cliente.
9. Análisis de Requisitos:
- Priorización: Should Have. Complementa la entrega física post-venta.
"""
# Referencias globales para evitar errores de linter
if 'pedidos' not in globals(): pedidos = []
if 'envios' not in globals(): envios = []
if 'clientes' not in globals(): clientes = []

print("\n--- GESTIÓN DE ENVÍOS ---")
id_p_envio = input("ID del Pedido para gestionar envío (PED-XXXX): ")
p_encontrado = None
for p in pedidos:
    if p['ID'] == id_p_envio:
        p_encontrado = p
        break

if p_encontrado:
    envio_existente = None
    for e in envios:
        if e['ID_Pedido'] == id_p_envio:
            envio_existente = e
            break
    
    if not envio_existente:
        print("Iniciando proceso de envío...")
        dir_entrega = input("Dirección de Entrega (o Enter para usar la del cliente): ")
        if dir_entrega == "":
            for c in clientes:
                if c['ID'] == p_encontrado['ID_Cliente']:
                    dir_entrega = c['Direccion']
                    break
        
        id_envio = "ENV-" + str(len(envios) + 1).zfill(4)
        nuevo_envio = {
            "ID_Envio": id_envio,
            "ID_Pedido": id_p_envio,
            "Direccion": dir_entrega,
            "Fecha_Envio": "2026-04-24",
            "Fecha_Entrega": "Pendiente",
            "Estado_Envio": "Enviado"
        }
        envios.append(nuevo_envio)
        p_encontrado['Estado'] = "Enviado"
        print(f"[OK] Envío {id_envio} registrado y estado actualizado a 'Enviado'.")
    else:
        print(f"Estado Actual: {envio_existente['Estado_Envio']}")
        nuevo_st = input("Nuevo Estado (Enviado / Entregado): ")
        envio_existente['Estado_Envio'] = nuevo_st
        if nuevo_st.lower() == 'entregado':
            envio_existente['Fecha_Entrega'] = "2026-04-24"
            p_encontrado['Estado'] = "Entregado"
        print("[OK] Estado de envío actualizado.")
else:
    print("[Error] Pedido no encontrado.")
print("")
