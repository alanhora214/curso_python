"""
"""
import csv
import json
import levenshtein

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

def crea_diccionario_titulos(lista_frases)-> dict:
    diccionario_titulos = {}
    for frase in lista_frases:
        if frase.pelicula in diccionario_titulos:
            diccionario_titulos[frase.pelicula].append(frase)
        else:
            diccionario_titulos[frase.pelicula] = [frase]
        palabras = frase.frase.split()
        for palabra in palabras:
            if palabra in diccionario_titulos:
                diccionario_titulos[palabra].append(frase)
            else:
                diccionario_titulos[palabra] = [frase]
    return diccionario_titulos

def buscar_palabras(frases:list, frase_a_buscar:str)-> list:
    frases_encontradas = []
    frase_a_buscar = frase_a_buscar.lower()
    for frase in frases:
        frase_lower = frase.frase.lower()
        ratio = levenshtein.ratio(frase_lower, frase_a_buscar)
        if ratio >=0.80:
            frase.ratio = ratio
            frases_encontradas.append(frase)
    return frases_encontradas

if __name__ == "__main__":
    frases = carga_archivo_csv("frases_consolidadas.csv")
    for frase in frases[0:5]:
        print(frase)
    diccionario_titulos = crea_diccionario_titulos(frases)
    lista_frase_amor = diccionario_titulos.get("amor")
    for frase in lista_frase_amor:
        print(frase)