
#----------------------------------
#Tipos de datos
#----------------------------------
# lista coleccion ordenada y mutable
lista = [1, 2, 3, 4, 5]

#tupla coleccion ordenada e inmutable
tupla = (1, 2, 3, 4, 5)

#Range coleccion inmutable de numeros 
rango = range(0,10)

# TIPOS DE DATOS DE MAPEO
#Diccionario coleccion desordenada, modificable e indexada
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}   

#TIPOS DE DATOS DE CONJUNTO
#Conjunto coleccion desordenada, no indexada y sin elementos duplicados
conjunto = {1, 2, 3, 4, 5} 

#Conjunto inmutable coleccion desordenada, no indexada y sin elementos duplicados
conjunto_inmutable = frozenset([1, 2, 3, 4, 5]) 

#TIPOS DE DATOS BOOLEANOS
#Booleano puede ser True o False    
booleano = True
booleano_falso = False
#TIPOS DE DATOS BINARIOS
#Bytes coleccion inmutable de bytes
bytes_datos = b"Hola Mundo"
#Bytearray coleccion mutable de bytes
bytearray_datos = bytearray(b"Hola Mundo")
#Memoria vista vista de memoria de un objeto binario
memoria_vista = memoryview(bytes_datos)
#TIPOS DE DATOS DE TEXTO
#Cadena de texto coleccion inmutable de caracteres
cadena_texto = "Hola Mundo"
#TIPOS DE DATOS NUMERICOS
#Entero numero entero positivo o negativo sin decimales

entero = 10
#Flotante numero real positivo o negativo con decimales
flotante = 10.5
#Complejo numero complejo con parte real e imaginaria
complejo = 2 + 3j
#----------------------------------

#Estructuras de datos
#----------------------------------
#Pila estructura de datos LIFO (Last In First Out)
pila = []       
pila.append(1)  # Agregar elemento a la pila
pila.append(2)  
pila.append(3)
elemento = pila.pop()  # Eliminar y retornar el ultimo elemento agregado
#Cola estructura de datos FIFO (First In First Out) 
from collections import deque
cola = deque()

cola.append(1)  # Agregar elemento a la cola
cola.append(2)
cola.append(3)
elemento = cola.popleft()  # Eliminar y retornar el primer elemento agregado
#Lista enlazada estructura de datos lineal donde cada elemento apunta al siguiente
