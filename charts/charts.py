import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['Python', 'C++', 'Ruby', 'Java']
    values = [90, 80, 75, 95]

    fig, ax = plt.subplots()            # fig es la figura, ax es el plano
    ax.pie(values, labels=labels)       # ax.pie genera el gráfico de torta, le pasamos los valores y las etiquetas
    plt.savefig('pie.png')
    plt.close()