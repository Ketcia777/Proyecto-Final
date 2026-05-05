#Ketcia Nicolle Larios de León
# MODULO DE CLIENTES
"""
8. Levantamiento de Requisitos (Módulo Clientes):
- Requisito Funcional: Captura de datos de cliente, generación de ID único, y CRUD en lista global 'clientes'.
- Requisito No Funcional: Validaciones de ingreso manuales mediante condicionales en consola.
9. Análisis de Requisitos:
- Priorización: Must Have. Es vital para la creación de pedidos.
"""
# Referencias globales para evitar errores de linter
if 'clientes' not in globals(): 
    clientes = []

print("\n--- GESTIÓN DE CLIENTES ---")
continuar_clientes = True
while continuar_clientes:
    print("1. Registrar Cliente")
    print("2. Ver Clientes")
    print("3. Buscar Cliente")
    print("4. Regresar al Menú Principal")
    
    opcion_cli = input("Opción: ")
    match opcion_cli:
        case "1":
            print("\nNUEVO CLIENTE")
            nit = input("NIT: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dpi = input("DPI: ")
            correo = input("Correo Electrónico: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            
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
            print(f"\n[OK] Cliente {id_cliente} registrado exitosamente.\n")
            
        case "2":
            print("\nLISTADO DE CLIENTES")
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for c in clientes:
                    print(f"ID: {c['ID']} | NIT: {c['Nit']} | {c['Nombre']} {c['Apellido']} | Tel: {c['Telefono']}")
            print("")
                    
        case "3":
            busqueda = input("\nIngrese NIT o DPI para buscar: ")
            encontrado = False
            for c in clientes:
                if c['Nit'] == busqueda or c['DPI'] == busqueda:
                    print("\nCLIENTE ENCONTRADO:")
                    print(f"ID: {c['ID']}")
                    print(f"Nombre: {c['Nombre']} {c['Apellido']}")
                    print(f"NIT: {c['Nit']} | DPI: {c['DPI']}")
                    print(f"Correo: {c['Correo']} | Tel: {c['Telefono']}")
                    print(f"Dirección: {c['Direccion']}")
                    encontrado = True
                    break
            if not encontrado:
                print("[Error] Cliente no encontrado.")
            print("")
                
        case "4":
            continuar_clientes = False
