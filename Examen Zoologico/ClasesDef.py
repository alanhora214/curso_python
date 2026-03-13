import csv

class Animal:
    def __init__(self, datos):
        self.atributos = {}
        for k, v in datos.items():
            if k:
                val = v.strip().replace('"', '')
                if val.replace('-', '').isdigit():
                    self.atributos[k.strip()] = int(val)
                else:
                    self.atributos[k.strip()] = val
        
        self.nombre = self.atributos.get('nombre_animal', 'Desconocido')
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
            with open(archivo_clases, mode='r', encoding='utf-8-sig') as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    cid = fila['Clase_id'].strip()
                    ctipo = fila['Clase_tipo'].strip()
                    self.clases[cid] = ctipo

            with open(archivo_zoo, mode='r', encoding='utf-8-sig') as f:
                lector = csv.DictReader(f)
                self.campos = [c.strip() for c in lector.fieldnames if c]
                for fila in lector:
                    fila_limpia = {k.strip(): v for k, v in fila.items() if k}
                    self.animales.append(Animal(fila_limpia))
            print("Datos cargados correctamente.")
        except Exception as e:
            print(f"Error: {e}")

    def guardar_datos(self, archivo_zoo):
        try:
            with open(archivo_zoo, mode='w', encoding='utf-8', newline='') as f:
                escritor = csv.DictWriter(f, fieldnames=self.campos)
                escritor.writeheader()
                for animal in self.animales:
                    d = animal.atributos.copy()
                    if not str(d['nombre_animal']).startswith('"'):
                        d['nombre_animal'] = f'"{d["nombre_animal"]}"'
                    escritor.writerow(d)
            print("Datos guardados.")
        except Exception as e:
            print(f"Error: {e}")
        
    def listar_por_clase(self, id_clase):
        ids = str(id_clase).strip()
        print(f"\n--- {self.clases.get(ids, 'Desconocida')} ---")
        encontrados = [a for a in self.animales if str(a.clase_id) == ids]
        return encontrados
    
    def listar_por_caracteristica(self, carac):
        c = carac.lower().strip()
        if c not in self.campos:
            print(f"No existe la característica: {c}")
            return []
        print(f"\n--- Animales con {c} ---")
        return [a for a in self.animales if a.atributos.get(c) == 1]

    def agregar_animal(self, nombre, id_clase, caracs_usuario):
        nueva_fila = {c: 0 for c in self.campos}
        nueva_fila.update(caracs_usuario)
        nueva_fila['nombre_animal'] = nombre
        nueva_fila['clase'] = int(id_clase)
        self.animales.append(Animal(nueva_fila))