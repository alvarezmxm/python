import matplotlib.pyplot as plt

def generar_grafica_barra(pais2, etiquetas, valor):
  fig, ax = plt.subplots()
  ax.bar(etiquetas, valor)
  #plt.show()
  plt.savefig(f'./graficas_barra/{pais2}.png')
  plt.close()

def generar_grafica_pastel(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels= labels)
  ax.axis('equal')
  #plt.show()
  plt.savefig(f'{pais2}.png')
  plt.close()