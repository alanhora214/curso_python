"""
"""
import csv
import json


class Frase:
    def __init__(self, frase, pelicula):
        self.frase = frase
        self.pelicula = pelicula

    def __str__(self):
        return f'"{self.frase}" - {self.pelicula}'
    
    def __repr__(self):
        return f'Frase(frase="{self.frase}", pelicula="{self.pelicula}")'
    
    def to_dict(self):
        return {
            "frase": self.frase,
            "pelicula": self.pelicula
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
def carga_archivo_csv(nombre_archivo):
    frases = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltar la primera línea (encabezados)
            for linea in lector:
                if len(linea) == 2:
                    frases.append(Frase(linea[0], linea[1]))
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
    return frases

if __name__ == "__main__":
    frases = carga_archivo_csv("frases_consolidadas.csv")
    for frase in frases[0:5]:
        print(frase)