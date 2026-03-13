from ClasesDef import Zoologico

def mostrar_menu():
    zoo = Zoologico()
    zoo.cargar_datos('zoo.csv', 'clases.csv')

    while True:
        print("\n" + "="*20)
        print(" MENU ZOOLOGICO")
        print("="*20)
        print("1. Listar por Clase")
        print("2. Listar por Característica")
        print("3. Agregar Animal")
        print("4. Guardar y Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            for id_c, nombre_c in zoo.clases.items():
                print(f"{id_c}. {nombre_c}")
            id_sel = input("ID de la clase")
            res = zoo.listar_por_clase(id_sel)
            for a in res: print(f" - {a.nombre}")

        elif opcion == '2':
            print("Características disponibles: pelo, plumas, huevos, leche, vuela, acuatico, etc.")
            c = input("¿Qué característica desea buscar?: ").lower()
            res = zoo.listar_por_caracteristica(c)
            for a in res: print(f" - {a.nombre}")

        elif opcion == "3":
            nom = input("Nombre del nuevo animal: ")
            print("Clases: 1:Mam, 2:Ave, 3:Rep, 4:Pez, 5:Anf, 6:Ins, 7:Inv")
            cla = input("ID de clase: ")
            
            # Lógica simplificada para agregar características
            pelo = int(input("¿Tiene pelo? (1=Si, 0=No): "))
            vuela = int(input("¿Vuela? (1=Si, 0=No): "))
            caracs = {'pelo': pelo, 'vuela': vuela}
            
            zoo.agregar_animal(nom, cla, caracs)

        elif opcion == "4":
            zoo.guardar_datos('zoo.csv')
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    mostrar_menu()