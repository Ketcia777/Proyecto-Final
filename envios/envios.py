#Ketcia Nicolle Larios de León
# MODULO DE ENVIOS

if 'pedidos' not in globals(): pedidos = []
if 'envios' not in globals(): envios = []
if 'clientes' not in globals(): clientes = []
if 'pagos' not in globals(): pagos = []

print("\n" + "="*50)
print("          GESTIÓN DE ENVÍOS")
print("="*50)
continuar_envios = True
while continuar_envios:
    print("\n1. Registrar Envío")
    print("2. Ver Todos los Envíos")
    print("3. Buscar Envío")
    print("4. Modificar Estado de Envío")
    print("5. Eliminar Envío")
    print("6. Regresar al Menú Principal")

    opcion_env = input("\nOpción: ")
    match opcion_env:

        case "1":
            print("\n--- REGISTRAR ENVÍO ---")
            if not pedidos:
                print("[Error] No hay pedidos registrados.")
            else:
                id_p_envio = input("ID del Pedido (PED-XXXX): ").strip()
                p_env = None
                for p in pedidos:
                    if p['ID'] == id_p_envio:
                        p_env = p
                        break

                if p_env is None:
                    print("[Error] Pedido no encontrado.")
                else:
                    tiene_pago_env = False
                    for pg in pagos:
                        if pg['ID_Pedido'] == id_p_envio:
                            tiene_pago_env = True
                            break
                    if not tiene_pago_env:
                        print(f"[Error] El pedido {id_p_envio} no tiene pago registrado. Registre el pago primero.")
                    else:
                        envio_dup = False
                        for e in envios:
                            if e['ID_Pedido'] == id_p_envio:
                                envio_dup = True
                                break
                        if envio_dup:
                            print(f"[Error] El pedido {id_p_envio} ya tiene un envío registrado.")
                        else:
                            dir_cliente = ""
                            nombre_cli_env = "Desconocido"
                            for c in clientes:
                                if c['ID'] == p_env['ID_Cliente']:
                                    dir_cliente = c['Direccion']
                                    nombre_cli_env = f"{c['Nombre']} {c['Apellido']}"
                                    break

                            print(f"\n  Pedido   : {p_env['ID']}")
                            print(f"  Cliente  : {nombre_cli_env}")
                            print(f"  Dir.reg. : {dir_cliente}")

                            dir_entrega = input("\nDirección de Entrega (Enter para usar la del cliente): ").strip()
                            if dir_entrega == "":
                                dir_entrega = dir_cliente

                            if dir_entrega == "":
                                print("[Error] La dirección de entrega no puede estar vacía.")
                            else:
                                fecha_envio_str = input("Fecha de Envío (AAAA-MM-DD) o Enter para hoy: ").strip()
                                if fecha_envio_str == "":
                                    fecha_envio_str = "2026-05-07"

                                fecha_entrega_est = input("Fecha Estimada de Entrega (AAAA-MM-DD) o Enter si es Pendiente: ").strip()
                                if fecha_entrega_est == "":
                                    fecha_entrega_est = "Pendiente"

                                id_envio = "ENV-" + str(len(envios) + 1).zfill(4)
                                nuevo_envio = {
                                    "ID_Envio": id_envio,
                                    "ID_Pedido": id_p_envio,
                                    "Direccion": dir_entrega,
                                    "Fecha_Envio": fecha_envio_str,
                                    "Fecha_Entrega": fecha_entrega_est,
                                    "Estado_Envio": "Preparando"
                                }
                                envios.append(nuevo_envio)
                                p_env['Estado'] = "En proceso"
                                print("\n" + "-"*40)
                                print("[OK] Envío registrado exitosamente.")
                                print(f"  ID Envío   : {id_envio}")
                                print(f"  ID Pedido  : {id_p_envio}")
                                print(f"  Dirección  : {dir_entrega}")
                                print(f"  F. Envío   : {fecha_envio_str}")
                                print(f"  F. Entrega : {fecha_entrega_est}")
                                print(f"  Estado     : Preparando")
                                print("-"*40)

        case "2":
            print("\n--- LISTADO DE ENVÍOS ---")
            if not envios:
                print("No hay envíos registrados.")
            else:
                print(f"{'ID Envío':<10} | {'ID Pedido':<12} | {'F. Envío':<12} | {'F. Entrega':<12} | {'Estado':<12}")
                print("-"*68)
                for e in envios:
                    print(f"{e['ID_Envio']:<10} | {e['ID_Pedido']:<12} | {e['Fecha_Envio']:<12} | {e['Fecha_Entrega']:<12} | {e['Estado_Envio']:<12}")
            print("")

        case "3":
            print("\n--- BUSCAR ENVÍO ---")
            busq_env = input("ID del Envío (ENV-XXXX) o ID del Pedido (PED-XXXX): ").strip()
            envio_enc = None
            for e in envios:
                if e['ID_Envio'] == busq_env or e['ID_Pedido'] == busq_env:
                    envio_enc = e
                    break
            if envio_enc is None:
                print("[Error] Envío no encontrado.")
            else:
                print("\n" + "-"*40)
                print("ENVÍO ENCONTRADO:")
                print(f"  ID Envío    : {envio_enc['ID_Envio']}")
                print(f"  ID Pedido   : {envio_enc['ID_Pedido']}")
                print(f"  Dirección   : {envio_enc['Direccion']}")
                print(f"  F. Envío    : {envio_enc['Fecha_Envio']}")
                print(f"  F. Entrega  : {envio_enc['Fecha_Entrega']}")
                print(f"  Estado      : {envio_enc['Estado_Envio']}")
                print("-"*40)

        case "4":
            print("\n--- MODIFICAR ESTADO DE ENVÍO ---")
            if not envios:
                print("[Error] No hay envíos registrados.")
            else:
                busq_mod_env = input("ID del Envío (ENV-XXXX): ").strip()
                envio_mod = None
                for e in envios:
                    if e['ID_Envio'] == busq_mod_env:
                        envio_mod = e
                        break
                if envio_mod is None:
                    print("[Error] Envío no encontrado.")
                else:
                    print(f"\nEnvío: {envio_mod['ID_Envio']} | Estado actual: {envio_mod['Estado_Envio']}")
                    print("  1. Preparando")
                    print("  2. Enviado")
                    print("  3. En camino")
                    print("  4. Entregado")
                    opcion_st_env = input("Nuevo estado: ").strip()
                    estado_ant_env = envio_mod['Estado_Envio']
                    estado_valido_env = True
                    match opcion_st_env:
                        case "1": envio_mod['Estado_Envio'] = "Preparando"
                        case "2": envio_mod['Estado_Envio'] = "Enviado"
                        case "3": envio_mod['Estado_Envio'] = "En camino"
                        case "4":
                            envio_mod['Estado_Envio'] = "Entregado"
                            envio_mod['Fecha_Entrega'] = "2026-05-07"
                            for p in pedidos:
                                if p['ID'] == envio_mod['ID_Pedido']:
                                    p['Estado'] = "Entregado"
                                    break
                        case _:
                            print("[Error] Opción no válida.")
                            estado_valido_env = False
                    if estado_valido_env:
                        print("\n" + "-"*40)
                        print("[OK] Estado del envío actualizado.")
                        print(f"  Estado anterior : {estado_ant_env}")
                        print(f"  Estado nuevo    : {envio_mod['Estado_Envio']}")
                        print("-"*40)

        case "5":
            print("\n--- ELIMINAR ENVÍO ---")
            if not envios:
                print("[Error] No hay envíos registrados.")
            else:
                busq_eli_env = input("ID del Envío (ENV-XXXX): ").strip()
                envio_eli = None
                for e in envios:
                    if e['ID_Envio'] == busq_eli_env:
                        envio_eli = e
                        break
                if envio_eli is None:
                    print("[Error] Envío no encontrado.")
                elif envio_eli['Estado_Envio'] == "Entregado":
                    print(f"[Error] No se puede eliminar un envío ya entregado.")
                else:
                    print(f"\nEnvío a eliminar: {envio_eli['ID_Envio']} | Pedido: {envio_eli['ID_Pedido']} | Estado: {envio_eli['Estado_Envio']}")
                    confirmacion_env = input("¿Confirma la eliminación? (s/n): ").strip().lower()
                    if confirmacion_env == "s":
                        envios.remove(envio_eli)
                        for p in pedidos:
                            if p['ID'] == envio_eli['ID_Pedido']:
                                p['Estado'] = "Pagado"
                                break
                        print("\n" + "-"*40)
                        print("[OK] Envío eliminado correctamente.")
                        print(f"  ID eliminado    : {envio_eli['ID_Envio']}")
                        print(f"  Pedido asociado : {envio_eli['ID_Pedido']}")
                        print(f"  Estado pedido   : Revertido a 'Pagado'")
                        print("-"*40)
                    else:
                        print("[Aviso] Eliminación cancelada.")

        case "6":
            continuar_envios = False

        case _:
            print("[Error] Opción no válida.")
