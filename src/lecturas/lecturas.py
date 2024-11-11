'''
Created on 18 oct 2024

@author: User
'''

from typing import Optional

def contador_palabras(fichero, cad):
    try:
        with open(fichero, mode='r', encoding='utf-8') as f:
            contenido=f.read().lower()
            palabras=contenido.split()
            contador=palabras.count(cad)
            return contador
    except IOError as e:
        print(f'Error al intentar leer al archivo: {e}')
    except Exception as e:
        print(f'Ocurrió un error al crear el fichero: {e}')
        

def lineas_con_palabra (fichero, cad):
    try:
        lista_lineas = []
        with open(fichero, mode='r', encoding='utf-8') as f:
            for linea in f:
                linea_limpia=linea.lower()
                if cad.lower() in linea_limpia:
                    lista_lineas.append(linea.strip())
        return lista_lineas
    except IOError as e:
        print(f'Error al intentar leer al archivo: {e}')
    except Exception as e:
        print(f'Ocurrió un error al crear el fichero: {e}')            
        

def palabras_unicas(fichero):
    try:
        with open(fichero, mode='r', encoding='utf-8') as f:
            contenido=f.read()
            palabras=contenido.split()
            palabras_unicas=set(palabras)
            return list(palabras_unicas)
    except IOError as e:
        print(f'Error al intentar leer al archivo: {e}')
    except Exception as e:
        print(f'Ocurrió un error al crear el fichero: {e}')



def longitud_promedio_lineas(file_path: str, sep:str) -> Optional[float]:
    longitud_total = 0
    n_lineas = 0  
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:  # Abre el archivo en modo lectura
            lineas = f.readlines()  # Lee todas las líneas del archivo
            for linea in lineas:  # Por cada línea del archivo:
                # Elimina espacios en blanco al principio y al final y divide usando el separador
                palabras = linea.strip().split(sep)  
                longitud_linea = len(palabras)  # Cuenta el número de palabras en la línea
                longitud_total += longitud_linea  # Suma el número de palabras
                n_lineas += 1  # Incrementa el contador de líneas

        if n_lineas == 0:  # Verifica si hay líneas
            return None

        return longitud_total / n_lineas  # Devuelve la longitud promedio de palabras por línea

    except IOError as e:
        print(f'Error al intentar leer el archivo: {e}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')


