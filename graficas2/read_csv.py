import csv

def lectura_csv(path):
  with open(path, 'r') as archivo:
    lectura = csv.reader(archivo, delimiter=',')
    cabecera = next(lectura)
    nueva_lista = []
    for linea in lectura:
      concatenacion = zip(cabecera, linea)
      dict = {key: value for key, value in concatenacion}
      nueva_lista.append(dict)
      
    return nueva_lista
    

if __name__ == '__main__':
  datos = lectura_csv('./data.csv')
  print(datos)