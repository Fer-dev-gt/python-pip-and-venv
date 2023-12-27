# Para limpiar la shell cuando se ejecute
import os 
os.system('clear')

# podemos importar datos de otros archivos como "main en este caso"
import main
print(f'Example => {main.data}')
main.run()



"""Con tal de no ejecutar todo el codigo del archivo main cuando lo importamos, aislamos parte del codigo en la funcion run() y asi podemos traer variables sin problema"""