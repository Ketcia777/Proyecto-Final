#Ketcia Nicolle Larios de León
# MODULO DE PEDIDOS

# Referencias globales para evitar errores de linter
if 'clientes' not in globals(): clientes = []
if 'videojuegos' not in globals(): videojuegos = []
if 'pedidos' not in globals(): pedidos = []
if 'detalles_pedido' not in globals(): detalles_pedido = []
if 'pagos' not in globals(): pagos = []
if 'envios' not in globals(): envios = []

print("\n" + "="*50)
print("          GESTIÓN DE PEDIDOS")
print("="*50)
continuar_pedidos = True
while continuar_pedidos:
    print("\n1. Crear Nuevo Pedido")
    print("2. Ver Todos los Pedidos")
    print("3. Buscar Pedido")
    print("4. Modificar Estado de Pedido")
    print("5. Eliminar Pedido")
    print("6. Regresar al Menú Principal")

    opcion_ped = input("\nOpción: ")
    match opcion_ped:

        case "1":
            # --- AGREGAR / INSERTAR PEDIDO ---
            print("\n--- CREAR NUEVO PEDIDO ---")
            if not clientes:
                print("[Error] No hay clientes registrados. Registre un cliente primero.")
            elif not videojuegos:
                print("[Error] No hay videojuegos en el catálogo. Agregue videojuegos primero.")
            else:
                nit_cliente = input("NIT del Cliente: ").strip()
                cliente_actual = None
                for c in clientes:
                    if c['Nit'] == nit_cliente:
                        cliente_actual = c
                        break

                if cliente_actual is None:
                    print("[Error] Cliente no encontrado. Verifique el NIT ingresado.")
                else:
                    print(f"[OK] Cliente: {cliente_actual['Nombre']} {cliente_actual['Apellido']} ({cliente_actual['ID']})")
                    id_pedido = "PED-" + str(len(pedidos) + 1).zfill(4)
                    detalles_actuales = []
                    total_pedido = 0.0

                    print("\nAgregue los videojuegos al pedido (escriba 'fin' para terminar):")
                    agregando_items = True
                    while agregando_items:
                        print("\n--- Videojuegos disponibles ---")
                        hay_stock = False
                        for v in videojuegos:
                            if v['Stock'] > 0:
                                print(f"  {v['ID']} | {v['Nombre']} ({v['Plataforma']}) | Q{v['Precio']:.2f} | Stock: {v['Stock']}")
                                hay_stock = True
                        if not hay_stock:
                            print("[Aviso] No hay videojuegos con stock disponible.")
                            agregando_items = False
                        else:
                            id_v_pedido = input("\nID del Videojuego (o 'fin' para terminar): ").strip()
                            if id_v_pedido.lower() == 'fin':
                                agregando_items = False
                            else:
                                v_encontrado = None
                                for v in videojuegos:
                                    if v['ID'] == id_v_pedido:
                                        v_encontrado = v
                                        break

                                if v_encontrado is None:
                                    print("[Error] Videojuego no encontrado.")
                                elif v_encontrado['Stock'] <= 0:
                                    print(f"[Error] '{v_encontrado['Nombre']}' está agotado.")
                                else:
                                    cantidad_valida = False
                                    cantidad_str = input(f"Cantidad (máx. {v_encontrado['Stock']} disponibles): ").strip()
                                    try:
                                        cantidad = int(cantidad_str)
                                        if cantidad <= 0:
                                            print("[Error] La cantidad debe ser mayor a cero.")
                                        elif cantidad > v_encontrado['Stock']:
                                            print(f"[Error] Stock insuficiente. Solo hay {v_encontrado['Stock']} unidades.")
                                        else:
                                            cantidad_valida = True
                                    except ValueError:
                                        print("[Error] La cantidad debe ser un número entero.")

                                    if cantidad_valida:
                                        precio_unit = v_encontrado['Precio']
                                        subtotal = precio_unit * cantidad
                                        id_detalle = "DET-" + str(len(detalles_pedido) + len(detalles_actuales) + 1).zfill(5)
                                        detalle = {
                                            "ID_Detalle": id_detalle,
                                            "ID_Pedido": id_pedido,
                                            "ID_Videojuego": v_encontrado['ID'],
                                            "Cantidad": cantidad,
                                            "Precio_Unitario": precio_unit
                                        }
                                        detalles_actuales.append(detalle)
                                        v_encontrado['Stock'] -= cantidad
                                        total_pedido += subtotal
                                        print(f"  [+] {v_encontrado['Nombre']} x{cantidad} = Q{subtotal:.2f}")

                    if not detalles_actuales:
                        print("[Aviso] Pedido cancelado. No se agregaron videojuegos.")
                    else:
                        nuevo_pedido = {
                            "ID": id_pedido,
                            "ID_Cliente": cliente_actual['ID'],
                            "Fecha": "2026-05-07",
                            "Total": total_pedido,
                            "Estado": "Pendiente"
                        }
                        pedidos.append(nuevo_pedido)
                        for d in detalles_actuales:
                            detalles_pedido.append(d)
                        print("\n" + "="*40)
                        print(f"  PEDIDO {id_pedido} CREADO EXITOSAMENTE")
                        print(f"  Cliente     : {cliente_actual['Nombre']} {cliente_actual['Apellido']}")
                        print(f"  Fecha       : 2026-05-07")
                        print(f"  Total       : Q{total_pedido:.2f}")
                        print(f"  Estado      : Pendiente")
                        print("="*40)

        case "2":
            # --- VER TODOS LOS PEDIDOS ---
            print("\n--- LISTADO DE PEDIDOS ---")
            if not pedidos:
                print("No hay pedidos registrados.")
            else:
                print(f"{'ID Pedido':<12} | {'ID Cliente':<10} | {'Fecha':<12} | {'Total':>10} | {'Estado':<12}")
                print("-"*65)
                for p in pedidos:
                    print(f"{p['ID']:<12} | {p['ID_Cliente']:<10} | {p['Fecha']:<12} | Q{p['Total']:>9.2f} | {p['Estado']:<12}")
            print("")

        case "3":
            # --- BUSCAR PEDIDO ---
            print("\n--- BUSCAR PEDIDO ---")
            busq_p = input("Ingrese ID del Pedido (PED-XXXX): ").strip()
            pedido_encontrado = None
            for p in pedidos:
                if p['ID'] == busq_p:
                    pedido_encontrado = p
                    break
            if pedido_encontrado is None:
                print("[Error] Pedido no encontrado.")
            else:
                # Buscar nombre del cliente
                nombre_cli_ped = "Desconocido"
                for c in clientes:
                    if c['ID'] == pedido_encontrado['ID_Cliente']:
                        nombre_cli_ped = f"{c['Nombre']} {c['Apellido']}"
                        break
                print("\n" + "-"*40)
                print(f"  ID Pedido  : {pedido_encontrado['ID']}")
                print(f"  Cliente    : {nombre_cli_ped} ({pedido_encontrado['ID_Cliente']})")
                print(f"  Fecha      : {pedido_encontrado['Fecha']}")
                print(f"  Total      : Q{pedido_encontrado['Total']:.2f}")
                print(f"  Estado     : {pedido_encontrado['Estado']}")
                print("\n  Detalle de productos:")
                print(f"  {'ID Det.':<10} | {'Videojuego':<22} | {'Cant.':<6} | {'P.Unit.':>8}")
                print("  " + "-"*55)
                for d in detalles_pedido:
                    if d['ID_Pedido'] == busq_p:
                        nombre_vj = "Desconocido"
                        for v in videojuegos:
                            if v['ID'] == d['ID_Videojuego']:
                                nombre_vj = v['Nombre']
                                break
                        print(f"  {d['ID_Detalle']:<10} | {nombre_vj:<22} | {d['Cantidad']:<6} | Q{d['Precio_Unitario']:>7.2f}")
                print("-"*40)

        case "4":
            # --- MODIFICAR ESTADO DEL PEDIDO ---
            print("\n--- MODIFICAR ESTADO DE PEDIDO ---")
            if not pedidos:
                print("[Error] No hay pedidos registrados.")
            else:
                busq_mod_p = input("Ingrese ID del Pedido a modificar (PED-XXXX): ").strip()
                pedido_mod = None
                for p in pedidos:
                    if p['ID'] == busq_mod_p:
                        pedido_mod = p
                        break
                if pedido_mod is None:
                    print("[Error] Pedido no encontrado.")
                else:
                    print(f"\nPedido: {pedido_mod['ID']} | Estado actual: {pedido_mod['Estado']}")
                    print("Estados disponibles:")
                    print("  1. Pendiente")
                    print("  2. En proceso")
                    print("  3. Enviado")
                    print("  4. Entregado")
                    print("  5. Cancelado")
                    opcion_estado = input("Seleccione nuevo estado: ").strip()
                    estado_anterior = pedido_mod['Estado']
                    match opcion_estado:
                        case "1":
                            pedido_mod['Estado'] = "Pendiente"
                        case "2":
                            pedido_mod['Estado'] = "En proceso"
                        case "3":
                            pedido_mod['Estado'] = "Enviado"
                        case "4":
                            pedido_mod['Estado'] = "Entregado"
                        case "5":
                            pedido_mod['Estado'] = "Cancelado"
                        case _:
                            print("[Error] Opción de estado no válida.")
                            estado_anterior = None
                    if estado_anterior is not None:
                        print("\n" + "-"*40)
                        print("[OK] Estado del pedido actualizado.")
                        print(f"  Estado anterior : {estado_anterior}")
                        print(f"  Estado nuevo    : {pedido_mod['Estado']}")
                        print("-"*40)

        case "5":
            # --- ELIMINAR PEDIDO ---
            print("\n--- ELIMINAR PEDIDO ---")
            if not pedidos:
                print("[Error] No hay pedidos registrados.")
            else:
                busq_eli_p = input("Ingrese ID del Pedido a eliminar (PED-XXXX): ").strip()
                pedido_eli = None
                for p in pedidos:
                    if p['ID'] == busq_eli_p:
                        pedido_eli = p
                        break
                if pedido_eli is None:
                    print("[Error] Pedido no encontrado.")
                else:
                    # Verificar si tiene pago asociado
                    tiene_pago = False
                    for pg in pagos:
                        if pg['ID_Pedido'] == busq_eli_p:
                            tiene_pago = True
                            break
                    # Verificar si tiene envío asociado
                    tiene_envio = False
                    for e in envios:
                        if e['ID_Pedido'] == busq_eli_p:
                            tiene_envio = True
                            break
                    if tiene_pago:
                        print(f"[Error] No se puede eliminar. El pedido {busq_eli_p} ya tiene un pago registrado.")
                    elif tiene_envio:
                        print(f"[Error] No se puede eliminar. El pedido {busq_eli_p} ya tiene un envío registrado.")
                    else:
                        nombre_cli_eli = "Desconocido"
                        for c in clientes:
                            if c['ID'] == pedido_eli['ID_Cliente']:
                                nombre_cli_eli = f"{c['Nombre']} {c['Apellido']}"
                                break
                        print(f"\nPedido a eliminar: {pedido_eli['ID']} | Cliente: {nombre_cli_eli} | Total: Q{pedido_eli['Total']:.2f}")
                        confirmacion_p = input("¿Confirma la eliminación? (s/n): ").strip().lower()
                        if confirmacion_p == "s":
                            # Restaurar stock de los videojuegos del pedido
                            for d in detalles_pedido:
                                if d['ID_Pedido'] == busq_eli_p:
                                    for v in videojuegos:
                                        if v['ID'] == d['ID_Videojuego']:
                                            v['Stock'] += d['Cantidad']
                                            break
                            # Eliminar detalles del pedido
                            i = 0
                            while i < len(detalles_pedido):
                                if detalles_pedido[i]['ID_Pedido'] == busq_eli_p:
                                    detalles_pedido.pop(i)
                                else:
                                    i += 1
                            pedidos.remove(pedido_eli)
                            print("\n" + "-"*40)
                            print("[OK] Pedido eliminado correctamente.")
                            print(f"  ID eliminado : {busq_eli_p}")
                            print(f"  Cliente      : {nombre_cli_eli}")
                            print("  Stock de videojuegos restaurado.")
                            print("-"*40)
                        else:
                            print("[Aviso] Eliminación cancelada.")

        case "6":
            continuar_pedidos = False

        case _:
            print("[Error] Opción no válida.")
