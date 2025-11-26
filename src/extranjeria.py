from typing import List
import csv 
from typing import NamedTuple
from collections import defaultdict

RegistroExtranjeria = NamedTuple(
    "RegistroExtranjeria", 
            [("distrito",str),
             ("seccion", str),
             ("barrio", str),
             ("pais",str),
             ("hombres", int),
             ("mujeres", int)
            ]
)

def lee_extranjeria(archivo: str) -> List[RegistroExtranjeria]:
    lista_extranjeria = []
    with open(archivo, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)  # saltamos cabecera
        for campos in lector:
            distrito = campos[0]
            seccion = campos[1]
            barrio = campos[2]
            pais = campos[3]
            hombres = int(campos[4])
            mujeres = int(campos[5])
            registro = RegistroExtranjeria(
                distrito, seccion, barrio,
                pais, hombres, mujeres
            )
            lista_extranjeria.append(registro)

    return lista_extranjeria


    """
    2. **numero_nacionalidades_distintas(registros)**: recibe una lista de tuplas 
    de tipo RegistroExtranjeria y devuelve el número de nacionalidades
    distintas  presentes en los registros de la lista recibida como parámetro.  
    
    """
    
def numero_nacionalidades_distintas(registros: List[RegistroExtranjeria]) -> int:
    nacionalidades = set()
    for registro in registros:
        nacionalidades.add(registro.pais)
        
    return len(nacionalidades)

    """
    3. **secciones_distritos_con_extranjeros_nacionalidades(registros,  paises)**: 
    recibe una lista de tuplas de tipo RegistroExtranjeria y un conjunto de cadenas
    con nombres de países, y devuelve  una lista  de  tuplas  (distrito,  seccion) 
    con  los distritos y secciones en los que  hay  extranjeros del conjunto de paises 
    dado como parámetro.
    La lista de tuplas devuelta estará ordenada por distrito.  
    """
    
def secciones_distritos_con_extranjeros_nacionalidades(
        registros: List[RegistroExtranjeria],
        paises: set[str]
    ) -> List[tuple[str, str]]:
    
    resultado = set()
    for registro in registros:
        if registro.pais not in paises:
            resultado.add((registro.distrito, registro.seccion))
    
    return sorted(resultado, key=lambda x: x[0])

   
    """
    4. **total_extranjeros_por_pais(registros)**: recibe una lista de tuplas
    de tipo RegistroExtranjeria y devuelve un diccionario de tipo `{str:int}` 
    en el que las claves son los países y los valores 
    son el número total de extranjeros (tanto hombres como mujeres) de cada país.
    
    """
    
def total_extranjeros_por_pais(registros: List[RegistroExtranjeria]) -> dict[str, int]:
    diccionario_paises = defaultdict(int)
    for registro in registros:
        diccionario_paises[registro.pais] += registro.hombres + registro.mujeres
    
        
    return diccionario_paises

"""
5. **top_n_extranjeria(registros,  n=3)**: recibe una lista de tuplas de tipo
RegistroExtranjeria y devuelve  una  lista  de  tuplas (pais,  numero_extranjeros) 
con los n países 
de los que hay más población extranjera en los registros pasados como parámetros. 

"""
def top_n_extranjeria(registros:List[RegistroExtranjeria], n:int=3) -> List[tuple[str, int]]:
    diccionario_paises = total_extranjeros_por_pais(registros)
    ordenado = sorted(diccionario_paises.items(), key=lambda x: x[1], reverse=True)
    return ordenado[:n]

        