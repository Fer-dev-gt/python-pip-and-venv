import os 
import matplotlib.pyplot as plt                   # Primero importar e "Instalar matplotlib" ya que no viene incorporado en Python, luego le damos una alias "plt"
os.system('clear')                                # Para limpiar la shell cuando se ejecute     


# Con esta función generamos la grafica de barras
def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()


# Con esta función generamo la grafica de pie
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig('chart_pie_final_este_si.png')
  plt.close()
  

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values) grafica de barras
  generate_pie_chart(labels, values)