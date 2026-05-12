#Ketcia Nicolle Larios de León
# MODULO DE REPORTES

if 'pedidos' not in globals(): pedidos = []
if 'videojuegos' not in globals(): videojuegos = []
if 'detalles_pedido' not in globals(): detalles_pedido = []
if 'clientes' not in globals(): clientes = []
if 'pagos' not in globals(): pagos = []
if 'envios' not in globals(): envios = []

print("\n" + "="*50)
print("         REPORTES DEL SISTEMA")
print("="*50)
continuar_reportes = True
while continuar_reportes:
    print("\n1. Reporte de Ventas y Pedidos")
    print("2. Reporte de Inventario de Videojuegos")
    print("3. Reporte de Pagos")
    print("4. Reporte de Envíos")
    print("5. Reporte General del Sistema")
    print("6. Regresar al Menú Principal")

    opcion_rep = input("\nOpción: ")
    match opcion_rep:

        case "1":
            # --- REPORTE DE VENTAS Y PEDIDOS ---
            print("\n" + "="*55)
            print("         REPORTE DE VENTAS Y PEDIDOS")
            print("="*55)
            if not pedidos:
                print("No hay pedidos registrados.")
            else:
                total_ventas = 0.0
                total_pedidos = len(pedidos)
                pendientes = 0
                pagados = 0
                enviados = 0
                entregados = 0
                cancelados = 0

                for p in pedidos:
                    total_ventas += p['Total']
                    if p['Estado'] == "Pendiente":
                        pendientes += 1
                    elif p['Estado'] == "Pagado":
                        pagados += 1
                    elif p['Estado'] in ["Enviado", "En proceso", "En camino"]:
                        enviados += 1
                    elif p['Estado'] == "Entregado":
                        entregados += 1
                    elif p['Estado'] == "Cancelado":
                        cancelados += 1

                print(f"\n  Total de Pedidos Registrados : {total_pedidos}")
                print(f"  Monto Total Recaudado        : Q{total_ventas:.2f}")
                print(f"\n  Desglose por Estado:")
                print(f"    Pendientes  : {pendientes}")
                print(f"    Pagados     : {pagados}")
                print(f"    En proceso  : {enviados}")
                print(f"    Entregados  : {entregados}")
                print(f"    Cancelados  : {cancelados}")

                print(f"\n  {'ID Pedido':<12} | {'ID Cliente':<10} | {'Fecha':<12} | {'Total':>10} | {'Estado':<12}")
                print("  " + "-"*65)
                for p in pedidos:
                    print(f"  {p['ID']:<12} | {p['ID_Cliente']:<10} | {p['Fecha']:<12} | Q{p['Total']:>9.2f} | {p['Estado']:<12}")

                # Top 5 videojuegos más vendidos (ordenamiento burbuja)
                print(f"\n  TOP 5 VIDEOJUEGOS MÁS VENDIDOS:")
                print("  " + "-"*35)
                conteo_ventas = []
                for v in videojuegos:
                    cant_vendida = 0
                    for d in detalles_pedido:
                        if d['ID_Videojuego'] == v['ID']:
                            cant_vendida += d['Cantidad']
                    if cant_vendida > 0:
                        conteo_ventas.append({"Nombre": v['Nombre'], "Vendidos": cant_vendida})

                for i in range(len(conteo_ventas)):
                    for j in range(0, len(conteo_ventas) - i - 1):
                        if conteo_ventas[j]['Vendidos'] < conteo_ventas[j+1]['Vendidos']:
                            conteo_ventas[j], conteo_ventas[j+1] = conteo_ventas[j+1], conteo_ventas[j]

                if not conteo_ventas:
                    print("  No hay ventas de videojuegos registradas.")
                else:
                    pos = 1
                    for item in conteo_ventas[:5]:
                        print(f"  {pos}. {item['Nombre']}: {item['Vendidos']} unidades")
                        pos += 1
            print("="*55)

        case "2":
            # --- REPORTE DE INVENTARIO ---
            print("\n" + "="*55)
            print("       REPORTE DE INVENTARIO DE VIDEOJUEGOS")
            print("="*55)
            if not videojuegos:
                print("No hay videojuegos registrados.")
            else:
                total_productos = len(videojuegos)
                stock_total = 0
                sin_stock = 0
                valor_inventario = 0.0

                for v in videojuegos:
                    stock_total += v['Stock']
                    valor_inventario += v['Stock'] * v['Precio']
                    if v['Stock'] == 0:
                        sin_stock += 1

                print(f"\n  Total de Productos en Catálogo : {total_productos}")
                print(f"  Unidades en Stock Total        : {stock_total}")
                print(f"  Productos Agotados             : {sin_stock}")
                print(f"  Valor Total del Inventario     : Q{valor_inventario:.2f}")

                print(f"\n  {'ID':<8} | {'Nombre':<25} | {'Plataforma':<10} | {'Precio':>8} | {'Stock':>6} | {'Valor':>10}")
                print("  " + "-"*80)
                for v in videojuegos:
                    valor_v = v['Stock'] * v['Precio']
                    estado_stock = "" if v['Stock'] > 0 else " [AGOTADO]"
                    print(f"  {v['ID']:<8} | {v['Nombre']:<25} | {v['Plataforma']:<10} | Q{v['Precio']:>7.2f} | {v['Stock']:>6} | Q{valor_v:>9.2f}{estado_stock}")
            print("="*55)

        case "3":
            # --- REPORTE DE PAGOS ---
            print("\n" + "="*55)
            print("            REPORTE DE PAGOS")
            print("="*55)
            if not pagos:
                print("No hay pagos registrados.")
            else:
                total_pagos = len(pagos)
                monto_total_pag = 0.0
                conteo_metodos = {}

                for pg in pagos:
                    monto_total_pag += pg['Monto']
                    met = pg['Metodo']
                    if met not in conteo_metodos:
                        conteo_metodos[met] = 0
                    conteo_metodos[met] += 1

                print(f"\n  Total de Pagos Registrados : {total_pagos}")
                print(f"  Monto Total Recaudado      : Q{monto_total_pag:.2f}")
                print(f"\n  Pagos por Método:")
                for met, cnt in conteo_metodos.items():
                    print(f"    {met:<25} : {cnt} pago(s)")

                print(f"\n  {'ID Pago':<10} | {'ID Pedido':<12} | {'Método':<22} | {'Monto':>10} | {'Fecha':<12}")
                print("  " + "-"*75)
                for pg in pagos:
                    print(f"  {pg['ID_Pago']:<10} | {pg['ID_Pedido']:<12} | {pg['Metodo']:<22} | Q{pg['Monto']:>9.2f} | {pg['Fecha']:<12}")
            print("="*55)

        case "4":
            # --- REPORTE DE ENVÍOS ---
            print("\n" + "="*55)
            print("            REPORTE DE ENVÍOS")
            print("="*55)
            if not envios:
                print("No hay envíos registrados.")
            else:
                total_envios = len(envios)
                preparando = 0
                en_camino = 0
                entregados_env = 0

                for e in envios:
                    if e['Estado_Envio'] in ["Preparando", "Enviado"]:
                        preparando += 1
                    elif e['Estado_Envio'] == "En camino":
                        en_camino += 1
                    elif e['Estado_Envio'] == "Entregado":
                        entregados_env += 1

                print(f"\n  Total de Envíos Registrados : {total_envios}")
                print(f"\n  Desglose por Estado:")
                print(f"    Preparando/Enviado : {preparando}")
                print(f"    En camino          : {en_camino}")
                print(f"    Entregados         : {entregados_env}")

                print(f"\n  {'ID Envío':<10} | {'ID Pedido':<12} | {'F. Envío':<12} | {'F. Entrega':<12} | {'Estado':<12}")
                print("  " + "-"*68)
                for e in envios:
                    print(f"  {e['ID_Envio']:<10} | {e['ID_Pedido']:<12} | {e['Fecha_Envio']:<12} | {e['Fecha_Entrega']:<12} | {e['Estado_Envio']:<12}")
            print("="*55)

        case "5":
            # --- REPORTE GENERAL DEL SISTEMA ---
            print("\n" + "="*55)
            print("         REPORTE GENERAL DEL SISTEMA")
            print("="*55)
            total_ventas_gen = 0.0
            for p in pedidos:
                total_ventas_gen += p['Total']

            total_monto_pagado = 0.0
            for pg in pagos:
                total_monto_pagado += pg['Monto']

            print(f"\n  RESUMEN GENERAL:")
            print(f"  {'Clientes registrados':<30} : {len(clientes)}")
            print(f"  {'Videojuegos en catálogo':<30} : {len(videojuegos)}")
            print(f"  {'Pedidos realizados':<30} : {len(pedidos)}")
            print(f"  {'Líneas de detalle':<30} : {len(detalles_pedido)}")
            print(f"  {'Pagos registrados':<30} : {len(pagos)}")
            print(f"  {'Envíos gestionados':<30} : {len(envios)}")
            print(f"\n  FINANCIERO:")
            print(f"  {'Ventas totales (pedidos)':<30} : Q{total_ventas_gen:.2f}")
            print(f"  {'Monto total cobrado':<30} : Q{total_monto_pagado:.2f}")
            pendiente_cobro = total_ventas_gen - total_monto_pagado
            print(f"  {'Pendiente por cobrar':<30} : Q{pendiente_cobro:.2f}")
            print("="*55)

        case "6":
            continuar_reportes = False

        case _:
            print("[Error] Opción no válida.")
