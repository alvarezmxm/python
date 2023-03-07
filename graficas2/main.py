import read_csv
import utils
import grafica

def run(): #esto es un comentario para verlo en docker
  datos = read_csv.lectura_csv('./data.csv')
  country = list(map(lambda item:item['Country/Territory'], datos))
 # print(country)
  #find = list(map(lambda item: item['World Population Percentage'], datos))
  #grafica.generar_grafica_pastel(country, find)
  #print(find)
  pais = input('Ingresa el nombre del pais: ')
  busqueda = utils.obtener_pais(datos, pais)

  if len(busqueda) > 0:
    pais2 = pais
    print(pais2)
    pais = busqueda[0]
    print(pais)
    etiquetas, valor = utils.obtener_poblacion(pais)
    grafica.generar_grafica_barra(pais2, etiquetas, valor)
    

if __name__ == '__main__':
  run()