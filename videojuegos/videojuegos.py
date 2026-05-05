#Ketcia Nicolle Larios de León
# MODULO DE VIDEOJUEGOS
"""
8. Levantamiento de Requisitos (Módulo Videojuegos):
- Requisito Funcional: Gestión de inventario, incluyendo stock y precios.
- Requisito No Funcional: Actualizaciones en tiempo real en consola sin latencia.
9. Análisis de Requisitos:
- Priorización: Must Have. El inventario es la base de las ventas.
- Validación: Comprobación de que el stock descontado persista en la lista global.
"""
# Referencias globales para evitar errores de linter
if 'videojuegos' not in globals(): 
    videojuegos = []

print("\n--- CATÁLOGO DE VIDEOJUEGOS ---")
continuar_juegos = True
while continuar_juegos:
    print("1. Agregar Videojuego")
    print("2. Ver Inventario")
    print("3. Actualizar Stock")
    print("4. Regresar al Menú Principal")
    
    opcion_juego = input("Opción: ")
    match opcion_juego:
        case "1":
            print("\nNUEVO VIDEOJUEGO")
            nombre_v = input("Nombre: ")
            genero = input("Género: ")
            plataforma = input("Plataforma (PS5, Xbox, PC, etc.): ")
            tipo = input("Digital o Físico: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock Inicial: "))
            clasif = input("Clasificación (E, T, M, etc.): ")
            
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
            print(f"\n[OK] Videojuego {id_v} agregado al catálogo.\n")
            
        case "2":
            print("\nINVENTARIO DE VIDEOJUEGOS")
            if not videojuegos:
                print("Catálogo vacío.")
            else:
                for v in videojuegos:
                    print(f"ID: {v['ID']} | {v['Nombre']} ({v['Plataforma']}) | {v['Tipo']} | Precio: Q{v['Precio']} | Stock: {v['Stock']}")
            print("")
                    
        case "3":
            id_buscado = input("\nIngrese ID del Videojuego (VG-XXX): ")
            encontrado = False
            for v in videojuegos:
                if v['ID'] == id_buscado:
                    nuevo_stock = int(input(f"Stock actual de {v['Nombre']} es {v['Stock']}. Nuevo stock: "))
                    v['Stock'] = nuevo_stock
                    print("[OK] Stock actualizado.")
                    encontrado = True
                    break
            if not encontrado:
                print("[Error] Videojuego no encontrado.")
            print("")
                
        case "4":
            continuar_juegos = False
