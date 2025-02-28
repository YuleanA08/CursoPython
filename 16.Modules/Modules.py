#Recuerda que las carpetas no deben de tener espacios en su nombre, ni tampoco iniciar con números
#Esto con el fin de facilitiar la importación de clases o funciones de otros
#La manera correcta de importar un modulo es la siguiente:
# from nombre_carpeta.nombre_archivo import nombre_funcion o nombre_clase
#Ejemplo:
#from Pilares_POO.Ejercicio4_lewis import palindroma

#Ya si cometiste ese error, puedes hacer lo siguiente
# que es usar el siguiente codigo para importar:
import sys
import os

# Añadir la ruta de la carpeta al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '15.Pilares POO')))

# Importar la función desde el otro módulo
from Ejercicio4_lewis import palindroma

palindroma("cobre") # True


