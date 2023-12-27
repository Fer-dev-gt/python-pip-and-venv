### Este archivo servira como modulo de otro programa, el cual lo importara al escribir el nombre del archivo con "import"

def get_population(country_dictionary):
  population_dictionary = {
    '2022' : int(country_dictionary['2022 Population']),
    '2020' : int(country_dictionary['2020 Population']),
    '2015' : int(country_dictionary['2015 Population']),
    '2010' : int(country_dictionary['2010 Population']),
    '2000' : int(country_dictionary['2000 Population']),
    '1990' : int(country_dictionary['1990 Population']),
    '1980' : int(country_dictionary['1980 Population']),
    '1970' : int(country_dictionary['1970 Population']),
  }
  labels = population_dictionary.keys()
  values = population_dictionary.values()
  
  return labels, values

# Creamos una variable que la usara el otro archivo, pero la mayoria de veces solo importamos funciones
A = 'Hola'

# creamos una funcion que nos permita filtrar a un pais si concide con los solicitado

def population_by_country(data, country):
  result = list(filter(lambda item : item['Country/Territory'] == country, data))
  return result