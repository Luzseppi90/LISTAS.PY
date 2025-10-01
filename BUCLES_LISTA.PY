#BUCLES EN LISTAS
#----------------------------------

frutas = ["manzana","banana","pera","mandarina","fresa", "piña"]


#bucle for estandar

for fruta in frutas:
    print("Me gusta la", fruta)

#bucle for con rango e indice

for i in range(len(frutas)): #len() devuelve la longitud de la lista
    print("Me gusta la", frutas[i]) #len() devuelve la longitud de la lista

len(frutas) #devuelve la longitud de la lista
print("Longitud de la lista:", len(frutas))

for i in range(len(frutas)): #recorre la lista en orden inverso
    print(frutas[i])
    print(i)

i=0
while i < len(frutas):  #bucle while con indice
    print("Me gusta la", frutas[i])
    i += 1 #incremento del indice


[print(frutas) for frutas in frutas]

   