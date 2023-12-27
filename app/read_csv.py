# Para limpiar la shell cuando se ejecute
import os 
os.system('clear')

# Primero importamos un modulo nativo que tiene Python para leer archivo CSV
import csv

# De esta manera mostramos los datos fila a fila y usamos un delimitador = ',' porque asi viene la fuente de datos

# Tambien creamos una funcion que se ejecuto con if __name__... y usamos with open() y funciones del modulo csv

"""def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
      print('***' * 12)
      print(row)"""
# Los datos me los muestra como una lista []
      

# Aca mostramos los datos como una lista de diccionarios, donde la llave es el nombre de la columna para mostrar los valores
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader) # Aqui guardamos los nombres de las columnas
    data = []
    for row in reader:
      iterable = zip(header, row)
      """Imprime listas de pares llave-valor en forma de tupla
      print(list(iterable))"""
      
      # Aca lo convertimos a un formato de diccionarios con "dictionary comprehension"
      country_dictionary = {key : value for key, value in iterable}
      data.append(country_dictionary)
      
    return data
      
  
# Con esto nos aseguramos que el programa se ejecute como un script desde la terminal
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])