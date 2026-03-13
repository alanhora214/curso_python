import csv

class Animal:
    def __init__(self,datos):
        self.atributos = {k: (init(v) if v.isdigit() else v) for k, v in datos.items()}
        self.nombre = self.atributos.get('nombre', 'Desconocido')
        self.clase_id = self.atributos.get('clase', 0)

    def __str__(self):
        return f"Animal: {self.nombre.capitalize()} (Clase: {self.clase_id})"
    
    def __repr__(self):
        return f"Animal(nombre='{self.nombre}', clase={self.clase_id})"
    
class Zoologico:
    def __init__(self):
        self.animales = []
        self.clases = {}
        self.campos = []

    def cargar_datos(self, archivo_zoo, archivo_clases):
        try:
            with open(archivo_clases, mode='r', encoding='utf-8') as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    self.clases[fila['Clase_id']] = fila['Clase_tipo']

            with open(archivo_zoo, mode='r', encoding='utf-8') as f:
                lector = csv.DictReader(f)
                self.campos = lector.fieldnames
                for fila in lector:
                    self.animales.append(Animal(fila))
            print("Datos cargados correctamente.")
        except Exception as e:
            print(f"Error al cargar archivos: {e}")

    def guardar_datos(self, archivo_zoo):
        try:
            with open(archivo_zoo, mode='w', encoding='utf-8', newline='') as f:
                escritor = csv.DictWriter(f, fieldnames=self.campos)
                escitor.writeheader()
                for animal in self.animales:
                    escritor.writerow(animal.atributos)
            print("Datos guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar archivo: {e}")
        
    def listar_por_clase(self, id_clase):
        print(f"\n--- Listado de {self.clases.get(str(id_clase), 'Desconocidos')} ---")
        encontrados = [a for a in self.animales if str(a.clase_id) == str(id_clase)]
        return encontrados
    
    def listar_por_caracteristica(self, carar):
        print(f"\n--- Listado de animales con: {carac} ---")
        encontrados = [a for a in self.animales if a.atributos.get(carac) == 1]
        return encontrados
    
    def afregar_animal(self, nombre, id_clase, dict_caracteristicas):
        nuevo_data = {c: 0 for c in self.campos}
        nuevo_data.update(dict_caracteristicas)
        nuevo_data['nombre_animal'] = nombre
        nuevo_data['clase'] = id_clase
        self.animales.append(Animal(nuevo_data))
        print(f"Animal '{nombre}' agregado correctamente.")