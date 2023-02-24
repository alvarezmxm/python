import matplotlib.pyplot as plt

def generar_grafica_pastel():
    etiquetas = ['A', 'B', 'C']
    valor = [200, 300, 400]

    fig, ax = plt.subplots()
    ax.pie(valor, labels=etiquetas)
    plt.savefig('grafica_de_pastel.png')
    plt.close()