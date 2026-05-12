#Ketcia Nicolle Larios de León
# MODULO DE PAGOS

# Referencias globales para evitar errores de linter
if 'pedidos' not in globals(): pedidos = []
if 'pagos' not in globals(): pagos = []
if 'clientes' not in globals(): clientes = []

print("\n" + "="*50)
print("          REGISTRO DE PAGOS")
print("="*50)
continuar_pagos = True
while continuar_pagos:
    print("\n1. Registrar Pago")
    print("2. Ver Todos los Pagos")
    print("3. Buscar Pago")
    print("4. Modificar Pago")
    print("5. Eliminar Pago")
    print("6. Regresar al Menú Principal")

    opcion_pag = input("\nOpción: ")
    match opcion_pag:

        case "1":
            # --- AGREGAR / INSERTAR PAGO ---
            print("\n--- REGISTRAR PAGO ---")
            if not pedidos:
                print("[Error] No hay pedidos registrados.")
            else:
                id_p_pago = input("ID del Pedido (PED-XXXX): ").strip()
                p_encontrado = None
                for p in pedidos:
                    if p['ID'] == id_p_pago:
                        p_encontrado = p
                        break

                if p_encontrado is None:
                    print("[Error] Pedido no encontrado.")
                else:
                    # Verificar si ya tiene pago
                    ya_pagado = False
                    for pg in pagos:
                        if pg['ID_Pedido'] == id_p_pago:
                            ya_pagado = True
                            break
                    if ya_pagado:
                        print(f"[Error] El pedido {id_p_pago} ya tiene un pago registrado.")
                    else:
                        # Buscar nombre del cliente
                        nombre_cli_pag = "Desconocido"
                        for c in clientes:
                            if c['ID'] == p_encontrado['ID_Cliente']:
                                nombre_cli_pag = f"{c['Nombre']} {c['Apellido']}"
                                break
                        print(f"\n  Pedido   : {p_encontrado['ID']}")
                        print(f"  Cliente  : {nombre_cli_pag}")
                        print(f"  Estado   : {p_encontrado['Estado']}")
                        print(f"  Total    : Q{p_encontrado['Total']:.2f}")

                        print("\nMétodos de pago disponibles:")
                        print("  1. Tarjeta de crédito")
                        print("  2. Tarjeta de débito")
                        print("  3. Efectivo")
                        print("  4. Transferencia bancaria")
                        opcion_metodo = input("Seleccione método de pago: ").strip()
                        metodo = ""
                        match opcion_metodo:
                            case "1": metodo = "Tarjeta de crédito"
                            case "2": metodo = "Tarjeta de débito"
                            case "3": metodo = "Efectivo"
                            case "4": metodo = "Transferencia bancaria"
                            case _:   metodo = ""

                        if metodo == "":
                            print("[Error] Método de pago no válido.")
                        else:
                            id_pago = "PAG-" + str(len(pagos) + 1).zfill(4)
                            nuevo_pago = {
                                "ID_Pago": id_pago,
                                "ID_Pedido": id_p_pago,
                                "Metodo": metodo,
                                "Monto": p_encontrado['Total'],
                                "Fecha": "2026-05-07"
                            }
                            pagos.append(nuevo_pago)
                            p_encontrado['Estado'] = "Pagado"
                            print("\n" + "-"*40)
                            print("[OK] Pago registrado exitosamente.")
                            print(f"  ID Pago  : {id_pago}")
                            print(f"  Método   : {metodo}")
                            print(f"  Monto    : Q{p_encontrado['Total']:.2f}")
                            print(f"  Fecha    : 2026-05-07")
                            print("-"*40)

        case "2":
            # --- VER TODOS LOS PAGOS ---
            print("\n--- LISTADO DE PAGOS ---")
            if not pagos:
                print("No hay pagos registrados.")
            else:
                print(f"{'ID Pago':<10} | {'ID Pedido':<12} | {'Método':<22} | {'Monto':>10} | {'Fecha':<12}")
                print("-"*75)
                for pg in pagos:
                    print(f"{pg['ID_Pago']:<10} | {pg['ID_Pedido']:<12} | {pg['Metodo']:<22} | Q{pg['Monto']:>9.2f} | {pg['Fecha']:<12}")
            print("")

        case "3":
            # --- BUSCAR PAGO ---
            print("\n--- BUSCAR PAGO ---")
            busq_pag = input("Ingrese ID del Pago (PAG-XXXX) o ID del Pedido (PED-XXXX): ").strip()
            pago_enc = None
            for pg in pagos:
                if pg['ID_Pago'] == busq_pag or pg['ID_Pedido'] == busq_pag:
                    pago_enc = pg
                    break
            if pago_enc is None:
                print("[Error] Pago no encontrado.")
            else:
                print("\n" + "-"*40)
                print("PAGO ENCONTRADO:")
                print(f"  ID Pago   : {pago_enc['ID_Pago']}")
                print(f"  ID Pedido : {pago_enc['ID_Pedido']}")
                print(f"  Método    : {pago_enc['Metodo']}")
                print(f"  Monto     : Q{pago_enc['Monto']:.2f}")
                print(f"  Fecha     : {pago_enc['Fecha']}")
                print("-"*40)

        case "4":
            # --- MODIFICAR PAGO ---
            print("\n--- MODIFICAR PAGO ---")
            if not pagos:
                print("[Error] No hay pagos registrados.")
            else:
                busq_mod_pag = input("Ingrese ID del Pago (PAG-XXXX): ").strip()
                pago_mod = None
                for pg in pagos:
                    if pg['ID_Pago'] == busq_mod_pag:
                        pago_mod = pg
                        break
                if pago_mod is None:
                    print("[Error] Pago no encontrado.")
                else:
                    print(f"\nModificando pago: {pago_mod['ID_Pago']} | Pedido: {pago_mod['ID_Pedido']}")
                    print(f"Método actual: {pago_mod['Metodo']}")
                    print("\nMétodos de pago disponibles:")
                    print("  1. Tarjeta de crédito")
                    print("  2. Tarjeta de débito")
                    print("  3. Efectivo")
                    print("  4. Transferencia bancaria")
                    print("  5. Conservar método actual")
                    opcion_met_mod = input("Seleccione nuevo método: ").strip()
                    metodo_anterior = pago_mod['Metodo']
                    match opcion_met_mod:
                        case "1": pago_mod['Metodo'] = "Tarjeta de crédito"
                        case "2": pago_mod['Metodo'] = "Tarjeta de débito"
                        case "3": pago_mod['Metodo'] = "Efectivo"
                        case "4": pago_mod['Metodo'] = "Transferencia bancaria"
                        case "5": pass
                        case _: print("[Error] Opción no válida. Se conserva el método actual.")

                    print("\n" + "-"*40)
                    print("[OK] Pago actualizado correctamente.")
                    print(f"  Método anterior : {metodo_anterior}")
                    print(f"  Método nuevo    : {pago_mod['Metodo']}")
                    print(f"  Monto           : Q{pago_mod['Monto']:.2f}")
                    print("-"*40)

        case "5":
            # --- ELIMINAR PAGO ---
            print("\n--- ELIMINAR PAGO ---")
            if not pagos:
                print("[Error] No hay pagos registrados.")
            else:
                busq_eli_pag = input("Ingrese ID del Pago (PAG-XXXX): ").strip()
                pago_eli = None
                for pg in pagos:
                    if pg['ID_Pago'] == busq_eli_pag:
                        pago_eli = pg
                        break
                if pago_eli is None:
                    print("[Error] Pago no encontrado.")
                else:
                    # Verificar que el pedido asociado no esté en estado final
                    pedido_asoc = None
                    for p in pedidos:
                        if p['ID'] == pago_eli['ID_Pedido']:
                            pedido_asoc = p
                            break
                    if pedido_asoc is not None and pedido_asoc['Estado'] in ["Enviado", "Entregado"]:
                        print(f"[Error] No se puede eliminar. El pedido {pago_eli['ID_Pedido']} ya está en estado '{pedido_asoc['Estado']}'.")
                    else:
                        print(f"\nPago a eliminar: {pago_eli['ID_Pago']} | Pedido: {pago_eli['ID_Pedido']} | Monto: Q{pago_eli['Monto']:.2f}")
                        confirmacion_pag = input("¿Confirma la eliminación? (s/n): ").strip().lower()
                        if confirmacion_pag == "s":
                            pagos.remove(pago_eli)
                            # Revertir estado del pedido
                            if pedido_asoc is not None:
                                pedido_asoc['Estado'] = "Pendiente"
                            print("\n" + "-"*40)
                            print("[OK] Pago eliminado correctamente.")
                            print(f"  ID eliminado     : {pago_eli['ID_Pago']}")
                            print(f"  Pedido asociado  : {pago_eli['ID_Pedido']}")
                            print(f"  Estado pedido    : Revertido a 'Pendiente'")
                            print("-"*40)
                        else:
                            print("[Aviso] Eliminación cancelada.")

        case "6":
            continuar_pagos = False

        case _:
            print("[Error] Opción no válida.")
