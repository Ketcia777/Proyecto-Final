#Ketcia Nicolle Larios de León
# ==============================================================================
# SISTEMA DE GESTIÓN DE PEDIDOS PARA EMPRESA DE VENTA DE VIDEOJUEGOS (SGP-VG)
# ==============================================================================

# LISTAS GLOBALES (Base de Datos en Memoria)
clientes = []
videojuegos = []
pedidos = []
detalles_pedido = []
pagos = []
envios = []

# VARIABLES DE CONTROL
continuar_sistema = True

while continuar_sistema:
    print("\n" + "="*50)
    print("      SISTEMA DE GESTIÓN DE PEDIDOS SGP-VG")
    print("="*50)
    print("1. Gestión de Clientes")
    print("2. Catálogo de Videojuegos")
    print("3. Crear Nuevo Pedido")
    print("4. Ver Detalles de Pedido")
    print("5. Registrar Pago")
    print("6. Gestionar Envío")
    print("7. Reportes de Ventas")
    print("8. Salir")
    print("="*50)
    
    opcion_principal = input("Seleccione una opción: ")
    
    match opcion_principal:
        case "1":
            # Módulo de Clientes
            #Ketcia Nicolle Larios de León
            # MODULO DE CLIENTES
            """
            8. Levantamiento de Requisitos (Módulo Clientes):
            - Requisito Funcional: Captura de datos de cliente, generación de ID único, y CRUD completo
              en lista global 'clientes' (Agregar, Ver, Buscar, Modificar, Eliminar).
            - Requisito No Funcional: Validaciones de ingreso manuales mediante condicionales en consola.
            9. Análisis de Requisitos:
            - Priorización: Must Have. Es vital para la creación de pedidos.
            - Validación: Campos obligatorios, no duplicar NIT/DPI, no eliminar con pedidos activos.
            """
            
            print("\n" + "="*50)
            print("        GESTIÓN DE CLIENTES")
            print("="*50)
            continuar_clientes = True
            while continuar_clientes:
                print("\n1. Registrar Cliente")
                print("2. Ver Clientes")
                print("3. Buscar Cliente")
                print("4. Modificar Cliente")
                print("5. Eliminar Cliente")
                print("6. Regresar al Menú Principal")
            
                opcion_cli = input("\nOpción: ")
                match opcion_cli:
            
                    case "1":
                        # --- AGREGAR / INSERTAR CLIENTE ---
                        print("\n--- NUEVO CLIENTE ---")
                        nit = input("NIT: ").strip()
                        if nit == "":
                            print("[Error] El NIT no puede estar vacío.")
                        else:
                            nombre = input("Nombre: ").strip()
                            if nombre == "":
                                print("[Error] El Nombre no puede estar vacío.")
                            else:
                                apellido = input("Apellido: ").strip()
                                if apellido == "":
                                    print("[Error] El Apellido no puede estar vacío.")
                                else:
                                    dpi = input("DPI: ").strip()
                                    if dpi == "":
                                        print("[Error] El DPI no puede estar vacío.")
                                    else:
                                        # Verificar duplicidad de NIT y DPI
                                        nit_duplicado = False
                                        dpi_duplicado = False
                                        for c in clientes:
                                            if c['Nit'] == nit:
                                                nit_duplicado = True
                                            if c['DPI'] == dpi:
                                                dpi_duplicado = True
                                        if nit_duplicado:
                                            print("[Error] Ya existe un cliente con ese NIT.")
                                        elif dpi_duplicado:
                                            print("[Error] Ya existe un cliente con ese DPI.")
                                        else:
                                            correo = input("Correo Electrónico: ").strip()
                                            if correo == "":
                                                print("[Error] El Correo no puede estar vacío.")
                                            else:
                                                telefono = input("Teléfono: ").strip()
                                                if telefono == "":
                                                    print("[Error] El Teléfono no puede estar vacío.")
                                                else:
                                                    direccion = input("Dirección: ").strip()
                                                    if direccion == "":
                                                        print("[Error] La Dirección no puede estar vacía.")
                                                    else:
                                                        id_cliente = "CLI-" + str(len(clientes) + 1).zfill(3)
                                                        nuevo_cliente = {
                                                            "ID": id_cliente,
                                                            "Nit": nit,
                                                            "Nombre": nombre,
                                                            "Apellido": apellido,
                                                            "DPI": dpi,
                                                            "Correo": correo,
                                                            "Telefono": telefono,
                                                            "Direccion": direccion
                                                        }
                                                        clientes.append(nuevo_cliente)
                                                        print("\n" + "-"*40)
                                                        print("[OK] Cliente registrado exitosamente.")
                                                        print(f"  ID Generado : {id_cliente}")
                                                        print(f"  Nombre      : {nombre} {apellido}")
                                                        print(f"  NIT         : {nit}")
                                                        print("-"*40)
            
                    case "2":
                        # --- VER / MOSTRAR TODOS LOS CLIENTES ---
                        print("\n--- LISTADO DE CLIENTES ---")
                        if not clientes:
                            print("No hay clientes registrados.")
                        else:
                            print(f"{'ID':<10} | {'NIT':<12} | {'Nombre':<20} | {'Apellido':<20} | {'Teléfono':<12}")
                            print("-"*80)
                            for c in clientes:
                                print(f"{c['ID']:<10} | {c['Nit']:<12} | {c['Nombre']:<20} | {c['Apellido']:<20} | {c['Telefono']:<12}")
                        print("")
            
                    case "3":
                        # --- BUSCAR CLIENTE ---
                        print("\n--- BUSCAR CLIENTE ---")
                        busqueda = input("Ingrese NIT o DPI para buscar: ").strip()
                        encontrado = False
                        for c in clientes:
                            if c['Nit'] == busqueda or c['DPI'] == busqueda:
                                print("\n" + "-"*40)
                                print("CLIENTE ENCONTRADO:")
                                print(f"  ID        : {c['ID']}")
                                print(f"  Nombre    : {c['Nombre']} {c['Apellido']}")
                                print(f"  NIT       : {c['Nit']}")
                                print(f"  DPI       : {c['DPI']}")
                                print(f"  Correo    : {c['Correo']}")
                                print(f"  Teléfono  : {c['Telefono']}")
                                print(f"  Dirección : {c['Direccion']}")
                                print("-"*40)
                                encontrado = True
                                break
                        if not encontrado:
                            print("[Error] Cliente no encontrado.")
            
                    case "4":
                        # --- MODIFICAR CLIENTE ---
                        print("\n--- MODIFICAR CLIENTE ---")
                        if not clientes:
                            print("[Error] No hay clientes registrados.")
                        else:
                            busq_mod = input("Ingrese NIT, DPI o ID del cliente a modificar: ").strip()
                            cliente_mod = None
                            for c in clientes:
                                if c['Nit'] == busq_mod or c['DPI'] == busq_mod or c['ID'] == busq_mod:
                                    cliente_mod = c
                                    break
                            if cliente_mod is None:
                                print("[Error] Cliente no encontrado.")
                            else:
                                print(f"\nModificando cliente: {cliente_mod['ID']} - {cliente_mod['Nombre']} {cliente_mod['Apellido']}")
                                print("(Presione Enter para conservar el valor actual)")
            
                                nuevo_nombre = input(f"Nombre [{cliente_mod['Nombre']}]: ").strip()
                                if nuevo_nombre != "":
                                    cliente_mod['Nombre'] = nuevo_nombre
            
                                nuevo_apellido = input(f"Apellido [{cliente_mod['Apellido']}]: ").strip()
                                if nuevo_apellido != "":
                                    cliente_mod['Apellido'] = nuevo_apellido
            
                                nuevo_correo = input(f"Correo [{cliente_mod['Correo']}]: ").strip()
                                if nuevo_correo != "":
                                    cliente_mod['Correo'] = nuevo_correo
            
                                nuevo_telefono = input(f"Teléfono [{cliente_mod['Telefono']}]: ").strip()
                                if nuevo_telefono != "":
                                    cliente_mod['Telefono'] = nuevo_telefono
            
                                nueva_direccion = input(f"Dirección [{cliente_mod['Direccion']}]: ").strip()
                                if nueva_direccion != "":
                                    cliente_mod['Direccion'] = nueva_direccion
            
                                print("\n" + "-"*40)
                                print("[OK] Cliente actualizado correctamente.")
                                print(f"  ID        : {cliente_mod['ID']}")
                                print(f"  Nombre    : {cliente_mod['Nombre']} {cliente_mod['Apellido']}")
                                print(f"  Correo    : {cliente_mod['Correo']}")
                                print(f"  Teléfono  : {cliente_mod['Telefono']}")
                                print(f"  Dirección : {cliente_mod['Direccion']}")
                                print("-"*40)
            
                    case "5":
                        # --- ELIMINAR CLIENTE ---
                        print("\n--- ELIMINAR CLIENTE ---")
                        if not clientes:
                            print("[Error] No hay clientes registrados.")
                        else:
                            busq_eli = input("Ingrese NIT, DPI o ID del cliente a eliminar: ").strip()
                            cliente_eli = None
                            for c in clientes:
                                if c['Nit'] == busq_eli or c['DPI'] == busq_eli or c['ID'] == busq_eli:
                                    cliente_eli = c
                                    break
                            if cliente_eli is None:
                                print("[Error] Cliente no encontrado.")
                            else:
                                # Verificar si tiene pedidos activos
                                tiene_pedidos = False
                                for p in pedidos:
                                    if p['ID_Cliente'] == cliente_eli['ID']:
                                        tiene_pedidos = True
                                        break
                                if tiene_pedidos:
                                    print(f"[Error] No se puede eliminar. El cliente {cliente_eli['ID']} tiene pedidos registrados.")
                                else:
                                    print(f"\nCliente a eliminar: {cliente_eli['ID']} - {cliente_eli['Nombre']} {cliente_eli['Apellido']}")
                                    confirmacion = input("¿Confirma la eliminación? (s/n): ").strip().lower()
                                    if confirmacion == "s":
                                        clientes.remove(cliente_eli)
                                        print("\n" + "-"*40)
                                        print("[OK] Cliente eliminado correctamente.")
                                        print(f"  ID eliminado : {cliente_eli['ID']}")
                                        print(f"  Nombre       : {cliente_eli['Nombre']} {cliente_eli['Apellido']}")
                                        print("-"*40)
                                    else:
                                        print("[Aviso] Eliminación cancelada.")
            
                    case "6":
                        continuar_clientes = False
            
                    case _:
                        print("[Error] Opción no válida.")

        case "2":
            # Módulo de Videojuegos
            #Ketcia Nicolle Larios de León
            # MODULO DE VIDEOJUEGOS
            """
            8. Levantamiento de Requisitos (Módulo Videojuegos):
            - Requisito Funcional: Gestión completa del inventario de videojuegos mediante CRUD.
              (Agregar, Ver, Buscar, Modificar, Eliminar).
            - Requisito No Funcional: Actualizaciones en tiempo real en consola sin latencia.
            9. Análisis de Requisitos:
            - Priorización: Must Have. El inventario es la base de las ventas.
            - Validación: Precio y stock numéricos, no duplicar IDs, no stock negativo, no eliminar
              si hay detalles de pedido relacionados.
            """
            
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

        case "3":
            # Módulo de Pedidos
            #Ketcia Nicolle Larios de León
            # MODULO DE PEDIDOS
            """
            8. Levantamiento de Requisitos (Módulo Pedidos):
            - Requisito Funcional: CRUD completo de pedidos vinculados a clientes y videojuegos.
              (Agregar, Ver, Buscar, Modificar estado, Eliminar).
            - Requisito No Funcional: Validación imperativa de cliente, stock y totales.
            9. Análisis de Requisitos:
            - Priorización: Must Have. Representa el núcleo transaccional del sistema.
            - Validación: Cliente debe existir, stock suficiente, no eliminar si tiene pago o envío.
            """
            
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

        case "4":
            # Módulo de Detalles
            #Ketcia Nicolle Larios de León
            # MODULO DE DETALLES DEL PEDIDO
            """
            8. Levantamiento de Requisitos (Módulo Detalles):
            - Requisito Funcional: Consulta y visualización completa del detalle de pedidos,
              incluyendo los videojuegos asociados y sus cantidades.
            - Requisito No Funcional: Garantizar la integridad de los datos compartidos entre módulos.
            9. Análisis de Requisitos:
            - Priorización: Must Have. Indispensable para auditar el contenido de cada pedido.
            - Validación: Verificar existencia del pedido antes de mostrar detalle.
            """
            
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

        case "5":
            # Módulo de Pagos
            #Ketcia Nicolle Larios de León
            # MODULO DE PAGOS
            """
            8. Levantamiento de Requisitos (Módulo Pagos):
            - Requisito Funcional: CRUD completo de pagos vinculados a pedidos.
              (Agregar, Ver, Buscar, Modificar, Eliminar).
            - Requisito No Funcional: Confirmación transaccional inmediata, no permitir pagos duplicados.
            9. Análisis de Requisitos:
            - Priorización: Must Have. Cierra el ciclo financiero de la venta.
            - Validación: Pedido debe existir, no duplicar pago por pedido, monto positivo.
            """
            
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

        case "6":
            # Módulo de Envíos
            #Ketcia Nicolle Larios de León
            # MODULO DE ENVIOS
            """
            8. Levantamiento de Requisitos (Módulo Envíos):
            - Requisito Funcional: CRUD completo de envíos vinculados a pedidos pagados.
            - Requisito No Funcional: Consistencia de direcciones respecto al cliente registrado.
            9. Análisis de Requisitos:
            - Priorización: Should Have. Complementa la entrega física post-venta.
            - Validación: Pedido debe existir y tener pago, no duplicar envío, secuencia lógica de estados.
            """
            
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

        case "7":
            # Módulo de Reportes
            #Ketcia Nicolle Larios de León
            # MODULO DE REPORTES
            """
            8. Levantamiento de Requisitos (Módulo Reportes):
            - Requisito Funcional: Generación de reportes administrativos y financieros a partir
              de las listas globales: ventas, inventario, pedidos, pagos y envíos.
            - Requisito No Funcional: Presentación limpia, ordenada y organizada en consola.
            9. Análisis de Requisitos:
            - Priorización: Could Have. Permite auditoría visual del estado del negocio.
            - Validación: Verificar existencia de datos antes de generar cada reporte.
            """
            
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

        case "8":
            print("\nGracias por usar SGP-VG. Cerrando sistema...")
            continuar_sistema = False
            
        case _:
            print("[Error] Opción no válida.")