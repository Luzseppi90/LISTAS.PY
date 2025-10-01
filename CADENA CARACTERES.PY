texto = "hola mundo"    
texto_con_espacios = "   hola mundo   "

print("capitalize: ",texto.capitalize())  # Salida: "Hola mundo - convierte primera letra en mayuscula"

print("upper: ",texto.upper())            # Salida: "HOLA MUNDO" - convierte todo a mayusculas
print("lower: ",texto.lower())            # Salida: "hola mundo" - convierte todo a minusculas
print("title: ",texto.title())            # Salida: "Hola Mundo" - convierte la primera letra de cada palabra en mayuscula
print("swapcase: ",texto.swapcase())      # Salida: "HOLA MUNDO" - convierte mayusculas en minusculas y viceversa
print("count: ",texto.count("o"))        # Salida: 2 - cuenta cuantas veces aparece un caracter o subcadena 

print("find: ",texto.find("mundo"))      # Salida: 5 - busca la posicion de un caracter o subcadena, si no lo encuentra devuelve -1
print("strip:",texto_con_espacios.strip()) # Salida: "hola mundo" - elimina espacios en blanco al inicio y al final
print("lstrip:",texto_con_espacios.lstrip()) # Salida: "hola mundo   " - elimina espacios en blanco al inicio
print("rstrip:",texto_con_espacios.rstrip()) # Salida: "   hola mundo" - elimina espacios en blanco al final
print("replace:",texto.replace("mundo","Python")) # Salida: "hola Python" - reemplaza una subcadena por otra
print("split:",texto.split())             # Salida: ['hola', 'mundo']   - divide la cadena en una lista de subcadenas
#---------------------------------- 
