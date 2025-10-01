# LISTAS
# ___________________________________________

lista = ["manzana", "banana", "cereza","manzana","frutilla","anana"]
print(lista)  # Salida: ['manzana', 'banana', 'cereza'] 

#indice

print(lista[0])  # Salida: 'manzana' - primer elemento
print(lista[1])  # Salida: 'banana' - segundo elemento      
print(lista[-1]) # Salida: 'cereza' - ultimo elemento   
print(lista[-2]) # Salida: 'banana' - penultimo elemento
print(lista[1:4]) # Salida: ['banana', 'cereza', 'manzana'] - elementos desde el indice 1 hasta el 3
print(lista[:3])  # Salida: ['manzana', 'banana', 'c    ereza'] - primeros 3 elementos
print(lista[2:])  # Salida: ['cereza', 'manzana', 'frutilla', 'anana'] - desde el indice 2 hasta el final
print(lista[-3:]) # Salida: ['manzana', 'frutilla', 'anana'] - ultimos 3 elementos
print(lista[:-2]) # Salida: ['manzana', 'banana', 'cereza', 'manzana'] - todos menos los ultimos 2 elementos
print(lista[::2]) # Salida: ['manzana', 'cereza', 'anana'] - todos los elementos con paso 2
print(lista[::-1]) # Salida: ['anana', 'frutilla', 'manzana', 'cereza', 'banana', 'manzana'] - lista invertida

if "banana" in lista:
    print("banana esta en la lista")  # Salida: banana esta en la lista     
else:
    print("banana no esta en la lista") 

#------------------------------------------------

lista[1]="platano"
print(lista)  # Salida: ['manzana', 'platano', 'cereza'] - modifica el segundo elemento 

print(len(lista))  # Salida: 3 - longitud de la lista   
lista.append("naranja")
print(lista)  # Salida: ['manzana', 'platano', 'cereza', 'naranja'] - agrega un elemento al final de la lista
lista.insert(1,"kiwi")
print(lista)  # Salida: ['manzana', 'kiwi', 'platano', 'cereza', 'naranja'] - agrega un elemento en la posicion 1
lista.remove("cereza")      
print(lista)  # Salida: ['manzana', 'kiwi', 'platano', 'naranja'] - elimina el primer elemento con el valor especificado