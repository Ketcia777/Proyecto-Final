#Ketcia Nicolle Larios de León
# MODULO DE DETALLES DEL PEDIDO

# Referencias globales para evitar errores de linter
if 'pedidos' not in globals(): pedidos = []
if 'detalles_pedido' not in globals(): detalles_pedido = []
if 'videojuegos' not in globals(): videojuegos = []
if 'clientes' not in globals(): clientes = []

print("\n" + "="*50)
print("       DETALLES DE PEDIDOS")
print("="*50)
continuar_detalles = True
while continuar_detalles:
    print("\n1. Consultar Detalle de un Pedido")
    print("2. Ver Todos los Detalles")
    print("3. Regresar al Menú Principal")

    opcion_det = input("\nOpción: ")
    match opcion_det:

        case "1":
            # --- CONSULTAR DETALLE DE UN PEDIDO ESPECÍFICO ---
            print("\n--- DETALLE DE PEDIDO ---")
            if not pedidos:
                print("[Error] No hay pedidos registrados.")
            else:
                id_p_consulta = input("Ingrese ID del Pedido (PED-XXXX): ").strip()
                pedido_det = None
                for p in pedidos:
                    if p['ID'] == id_p_consulta:
                        pedido_det = p
                        break
                if pedido_det is None:
                    print("[Error] Pedido no encontrado.")
                else:
                    # Buscar nombre del cliente
                    nombre_cli_det = "Desconocido"
                    for c in clientes:
                        if c['ID'] == pedido_det['ID_Cliente']:
                            nombre_cli_det = f"{c['Nombre']} {c['Apellido']}"
                            break

                    print("\n" + "="*55)
                    print(f"  PEDIDO    : {pedido_det['ID']}")
                    print(f"  Cliente   : {nombre_cli_det} ({pedido_det['ID_Cliente']})")
                    print(f"  Fecha     : {pedido_det['Fecha']}")
                    print(f"  Estado    : {pedido_det['Estado']}")
                    print(f"  Total     : Q{pedido_det['Total']:.2f}")
                    print("="*55)
                    print(f"  {'ID Det.':<10} | {'Videojuego':<25} | {'Cant.':<6} | {'P.Unit.':>9} | {'Subtotal':>10}")
                    print("  " + "-"*68)

                    hay_detalles = False
                    for d in detalles_pedido:
                        if d['ID_Pedido'] == id_p_consulta:
                            nombre_juego = "Desconocido"
                            for v in videojuegos:
                                if v['ID'] == d['ID_Videojuego']:
                                    nombre_juego = v['Nombre']
                                    break
                            subtotal_det = d['Cantidad'] * d['Precio_Unitario']
                            print(f"  {d['ID_Detalle']:<10} | {nombre_juego:<25} | {d['Cantidad']:<6} | Q{d['Precio_Unitario']:>8.2f} | Q{subtotal_det:>9.2f}")
                            hay_detalles = True
                    print("  " + "-"*68)
                    print(f"  {'TOTAL A PAGAR':>50}   Q{pedido_det['Total']:>9.2f}")
                    print("="*55)
                    if not hay_detalles:
                        print("  [Aviso] Este pedido no tiene productos registrados.")

        case "2":
            # --- VER TODOS LOS DETALLES REGISTRADOS ---
            print("\n--- TODOS LOS DETALLES DE PEDIDOS ---")
            if not detalles_pedido:
                print("No hay detalles registrados.")
            else:
                print(f"{'ID Det.':<10} | {'ID Pedido':<12} | {'Videojuego':<22} | {'Cant.':<6} | {'P.Unit.':>9}")
                print("-"*70)
                for d in detalles_pedido:
                    nombre_vj_det = "Desconocido"
                    for v in videojuegos:
                        if v['ID'] == d['ID_Videojuego']:
                            nombre_vj_det = v['Nombre']
                            break
                    print(f"{d['ID_Detalle']:<10} | {d['ID_Pedido']:<12} | {nombre_vj_det:<22} | {d['Cantidad']:<6} | Q{d['Precio_Unitario']:>8.2f}")
            print("")

        case "3":
            continuar_detalles = False

        case _:
            print("[Error] Opción no válida.")
