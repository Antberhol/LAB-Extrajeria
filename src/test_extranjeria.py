from extranjeria import *

def test_lee_extranjeria():
    ruta_fichero = "data/extranjeriaSevilla.csv"
    registros = lee_extranjeria(ruta_fichero)
    print("los 3 primeros registros son ", registros[:3])  # Muestra los primeros 3 registros para verificar
    

def test_secciones_distritos_con_extranjeros_nacionalidades():
    ruta_fichero = "data/extranjeriaSevilla.csv"
    registros = lee_extranjeria(ruta_fichero)
    paises = {"ITALIA", "ALEMANIA"}
    resultado = secciones_distritos_con_extranjeros_nacionalidades(registros, paises)
    print("Secciones y distritos con extranjeros de ALEMANIA y ITALIA:", resultado[:3])
    
def test_total_extranjeros_por_pais():
    ruta_fichero = "data/extranjeriaSevilla.csv"
    registros = lee_extranjeria(ruta_fichero)
    resultado = total_extranjeros_por_pais(registros)
    print("Total de extranjeros por país:", resultado)

def test_top_n_extranjeria():
    ruta_fichero = "data/extranjeriaSevilla.csv"
    registros = lee_extranjeria(ruta_fichero)
    resultado = top_n_extranjeria(registros, n=5)
    print("Top 5 países con más extranjeros:", resultado)
def test_barrio_mas_cultural():
    ruta_fichero = "data/extranjeriaSevilla.csv"
    registros = lee_extranjeria(ruta_fichero)
    resultado = barrio_mas_multicultural(registros)
    print("Barrio más multicultural:", resultado)
    
def test_barrio_mas_extranjeros():
    ruta_fichero = "data/extranjeriaSevilla.csv"
    registros = lee_extranjeria(ruta_fichero)
    resultado = barrio_con_mas_Extranjeros(registros, None)
    print("Barrio con más extranjeros:", resultado)
def main():
    #  test_lee_extranjeria()
    #test_secciones_distritos_con_extranjeros_nacionalidades()
    #test_total_extranjeros_por_pais()
    #test_top_n_extranjeria()
    #test_barrio_mas_cultural()
    test_barrio_mas_extranjeros()
    
if __name__ == "__main__":
    main()
    