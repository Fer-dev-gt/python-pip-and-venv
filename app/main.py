import os 
import utils                            # aca importamos el modulo que creamos en otro archivo
import read_csv
import charts

os.system('clear')                      # Para limpiar la shell cuando se ejecute   

  
def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  countries = list(map(lambda x : x['Country/Territory'], data))
  percentages = list(map(lambda x : x ['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  
  country = (input('Type Country => ')).capitalize()
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
    
  #print(utils.A)                     # Incluso si se trata de una variable, esta la podemos importar de la misma manera que con una funcion
  #print(result)


if __name__ == '__main__':
  run()