#Ketcia Nicolle Larios de León
# MODULO DE VIDEOJUEGOS

# Referencias globales para evitar errores de linter
if 'videojuegos' not in globals():
    videojuegos = []
if 'detalles_pedido' not in globals():
    detalles_pedido = []

print("\n" + "="*50)
print("       CATÁLOGO DE VIDEOJUEGOS")
print("="*50)
continuar_juegos = True
while continuar_juegos:
    print("\n1. Agregar Videojuego")
    print("2. Ver Inventario")
    print("3. Buscar Videojuego")
    print("4. Modificar Videojuego")
    print("5. Eliminar Videojuego")
    print("6. Regresar al Menú Principal")

    opcion_juego = input("\nOpción: ")
    match opcion_juego:

        case "1":
            # --- AGREGAR / INSERTAR VIDEOJUEGO ---
            print("\n--- NUEVO VIDEOJUEGO ---")
            nombre_v = input("Nombre: ").strip()
            if nombre_v == "":
                print("[Error] El Nombre no puede estar vacío.")
            else:
                # Verificar duplicidad de nombre
                nombre_duplicado = False
                for vj in videojuegos:
                    if vj['Nombre'].lower() == nombre_v.lower():
                        nombre_duplicado = True
                        break
                if nombre_duplicado:
                    print("[Error] Ya existe un videojuego con ese nombre.")
                else:
                    genero = input("Género (Acción, RPG, Deportes, etc.): ").strip()
                    if genero == "":
                        print("[Error] El Género no puede estar vacío.")
                    else:
                        plataforma = input("Plataforma (PS5, Xbox, PC, Switch, etc.): ").strip()
                        if plataforma == "":
                            print("[Error] La Plataforma no puede estar vacía.")
                        else:
                            tipo = input("Tipo (Digital / Físico): ").strip()
                            if tipo == "":
                                print("[Error] El Tipo no puede estar vacío.")
                            else:
                                precio_valido = False
                                precio = 0.0
                                precio_str = input("Precio (Q): ").strip()
                                try:
                                    precio = float(precio_str)
                                    if precio < 0:
                                        print("[Error] El precio no puede ser negativo.")
                                    else:
                                        precio_valido = True
                                except ValueError:
                                    print("[Error] El precio debe ser un número válido.")

                                if precio_valido:
                                    stock_valido = False
                                    stock = 0
                                    stock_str = input("Stock Inicial: ").strip()
                                    try:
                                        stock = int(stock_str)
                                        if stock < 0:
                                            print("[Error] El stock no puede ser negativo.")
                                        else:
                                            stock_valido = True
                                    except ValueError:
                                        print("[Error] El stock debe ser un número entero.")

                                    if stock_valido:
                                        clasif = input("Clasificación (E, T, M, AO, RP): ").strip()
                                        if clasif == "":
                                            print("[Error] La Clasificación no puede estar vacía.")
                                        else:
                                            id_v = "VG-" + str(len(videojuegos) + 1).zfill(3)
                                            nuevo_v = {
                                                "ID": id_v,
                                                "Nombre": nombre_v,
                                                "Genero": genero,
                                                "Plataforma": plataforma,
                                                "Tipo": tipo,
                                                "Precio": precio,
                                                "Stock": stock,
                                                "Clasificacion": clasif
                                            }
                                            videojuegos.append(nuevo_v)
                                            print("\n" + "-"*40)
                                            print("[OK] Videojuego registrado exitosamente.")
                                            print(f"  ID          : {id_v}")
                                            print(f"  Nombre      : {nombre_v}")
                                            print(f"  Plataforma  : {plataforma}")
                                            print(f"  Precio      : Q{precio:.2f}")
                                            print(f"  Stock       : {stock} unidades")
                                            print("-"*40)

        case "2":
            # --- VER / MOSTRAR INVENTARIO ---
            print("\n--- INVENTARIO DE VIDEOJUEGOS ---")
            if not videojuegos:
                print("Catálogo vacío. No hay videojuegos registrados.")
            else:
                print(f"{'ID':<8} | {'Nombre':<25} | {'Plataforma':<10} | {'Tipo':<8} | {'Precio':>8} | {'Stock':>6} | {'Clasif.':<6}")
                print("-"*90)
                for v in videojuegos:
                    print(f"{v['ID']:<8} | {v['Nombre']:<25} | {v['Plataforma']:<10} | {v['Tipo']:<8} | Q{v['Precio']:>7.2f} | {v['Stock']:>6} | {v['Clasificacion']:<6}")
            print("")

        case "3":
            # --- BUSCAR VIDEOJUEGO ---
            print("\n--- BUSCAR VIDEOJUEGO ---")
            busq_v = input("Ingrese ID o Nombre del videojuego: ").strip()
            encontrado_v = False
            for v in videojuegos:
                if v['ID'] == busq_v or v['Nombre'].lower() == busq_v.lower():
                    print("\n" + "-"*40)
                    print("VIDEOJUEGO ENCONTRADO:")
                    print(f"  ID            : {v['ID']}")
                    print(f"  Nombre        : {v['Nombre']}")
                    print(f"  Género        : {v['Genero']}")
                    print(f"  Plataforma    : {v['Plataforma']}")
                    print(f"  Tipo          : {v['Tipo']}")
                    print(f"  Precio        : Q{v['Precio']:.2f}")
                    print(f"  Stock         : {v['Stock']} unidades")
                    print(f"  Clasificación : {v['Clasificacion']}")
                    print("-"*40)
                    encontrado_v = True
                    break
            if not encontrado_v:
                print("[Error] Videojuego no encontrado.")

        case "4":
            # --- MODIFICAR VIDEOJUEGO ---
            print("\n--- MODIFICAR VIDEOJUEGO ---")
            if not videojuegos:
                print("[Error] No hay videojuegos registrados.")
            else:
                busq_mod_v = input("Ingrese ID o Nombre del videojuego a modificar: ").strip()
                vj_mod = None
                for v in videojuegos:
                    if v['ID'] == busq_mod_v or v['Nombre'].lower() == busq_mod_v.lower():
                        vj_mod = v
                        break
                if vj_mod is None:
                    print("[Error] Videojuego no encontrado.")
                else:
                    print(f"\nModificando: {vj_mod['ID']} - {vj_mod['Nombre']}")
                    print("(Presione Enter para conservar el valor actual)")

                    nuevo_nombre_v = input(f"Nombre [{vj_mod['Nombre']}]: ").strip()
                    if nuevo_nombre_v != "":
                        vj_mod['Nombre'] = nuevo_nombre_v

                    nuevo_genero = input(f"Género [{vj_mod['Genero']}]: ").strip()
                    if nuevo_genero != "":
                        vj_mod['Genero'] = nuevo_genero

                    nueva_plataforma = input(f"Plataforma [{vj_mod['Plataforma']}]: ").strip()
                    if nueva_plataforma != "":
                        vj_mod['Plataforma'] = nueva_plataforma

                    nuevo_tipo = input(f"Tipo [{vj_mod['Tipo']}]: ").strip()
                    if nuevo_tipo != "":
                        vj_mod['Tipo'] = nuevo_tipo

                    nuevo_precio_str = input(f"Precio [Q{vj_mod['Precio']:.2f}]: ").strip()
                    if nuevo_precio_str != "":
                        try:
                            nuevo_precio = float(nuevo_precio_str)
                            if nuevo_precio < 0:
                                print("[Aviso] Precio negativo no válido. Se conserva el anterior.")
                            else:
                                vj_mod['Precio'] = nuevo_precio
                        except ValueError:
                            print("[Aviso] Valor inválido. Se conserva el precio anterior.")

                    nuevo_stock_str = input(f"Stock [{vj_mod['Stock']}]: ").strip()
                    if nuevo_stock_str != "":
                        try:
                            nuevo_stock = int(nuevo_stock_str)
                            if nuevo_stock < 0:
                                print("[Aviso] Stock negativo no válido. Se conserva el anterior.")
                            else:
                                vj_mod['Stock'] = nuevo_stock
                        except ValueError:
                            print("[Aviso] Valor inválido. Se conserva el stock anterior.")

                    nueva_clasif = input(f"Clasificación [{vj_mod['Clasificacion']}]: ").strip()
                    if nueva_clasif != "":
                        vj_mod['Clasificacion'] = nueva_clasif

                    print("\n" + "-"*40)
                    print("[OK] Videojuego actualizado correctamente.")
                    print(f"  ID          : {vj_mod['ID']}")
                    print(f"  Nombre      : {vj_mod['Nombre']}")
                    print(f"  Precio      : Q{vj_mod['Precio']:.2f}")
                    print(f"  Stock       : {vj_mod['Stock']} unidades")
                    print("-"*40)

        case "5":
            # --- ELIMINAR VIDEOJUEGO ---
            print("\n--- ELIMINAR VIDEOJUEGO ---")
            if not videojuegos:
                print("[Error] No hay videojuegos registrados.")
            else:
                busq_eli_v = input("Ingrese ID o Nombre del videojuego a eliminar: ").strip()
                vj_eli = None
                for v in videojuegos:
                    if v['ID'] == busq_eli_v or v['Nombre'].lower() == busq_eli_v.lower():
                        vj_eli = v
                        break
                if vj_eli is None:
                    print("[Error] Videojuego no encontrado.")
                else:
                    # Verificar si tiene detalles de pedido activos
                    en_pedido = False
                    for d in detalles_pedido:
                        if d['ID_Videojuego'] == vj_eli['ID']:
                            en_pedido = True
                            break
                    if en_pedido:
                        print(f"[Error] No se puede eliminar. El videojuego {vj_eli['ID']} está asociado a pedidos existentes.")
                    else:
                        print(f"\nVideojuego a eliminar: {vj_eli['ID']} - {vj_eli['Nombre']}")
                        confirmacion_v = input("¿Confirma la eliminación? (s/n): ").strip().lower()
                        if confirmacion_v == "s":
                            videojuegos.remove(vj_eli)
                            print("\n" + "-"*40)
                            print("[OK] Videojuego eliminado correctamente.")
                            print(f"  ID eliminado : {vj_eli['ID']}")
                            print(f"  Nombre       : {vj_eli['Nombre']}")
                            print("-"*40)
                        else:
                            print("[Aviso] Eliminación cancelada.")

        case "6":
            continuar_juegos = False

        case _:
            print("[Error] Opción no válida.")
