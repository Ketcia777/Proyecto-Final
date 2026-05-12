#Ketcia Nicolle Larios de León
# MODULO DE CLIENTES

# Referencias globales para evitar errores de linter
if 'clientes' not in globals():
    clientes = []
if 'pedidos' not in globals():
    pedidos = []

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
