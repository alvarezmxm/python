def obtener_pais(datos, pais):
  x = list(filter(lambda item: item['Country/Territory'] == pais, datos))
  return x

def obtener_poblacion(pais):
  diccionario_poblacion = {
    '2022': int(pais['2022 Population']),
    '2020': int(pais['2020 Population']),
    '2015': int(pais['2015 Population']),
    '2010': int(pais['2010 Population']),
    '2000': int(pais['2000 Population']),
    '1990': int(pais['1990 Population']),
    '1980': int(pais['1980 Population']),
    '1970': int(pais['1970 Population'])
  }
  etiquetas = diccionario_poblacion.keys()
  valor = diccionario_poblacion.values()
  return etiquetas, valor
