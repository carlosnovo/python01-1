#Grupo 18
#Garcia Luz, Jesus Manuel
#Roncero Jimenez, Jesus

#Programa Trabajando con pokemons
#"Vamos a desarrollar el programa de Python que nos permita, a partir de una lista de #palabras, 
#encontrar la lista más larga posible de palabras de manera que la última #letra de una palabra coincida 
#con la primera de la siguiente palabra. Para probar el #programa la lista de palabras con las que vamos 
#a trabajar son la que encontramos en #el fichero pokemon.txt"

#Abrimos el fichero
f = open("pokemon.txt")
lista = []
lista_res1 = []
lista_resultado = []
contador_viejo = 0
contador = 0

# y volcamos el fichero
for line in file("pokemon.txt"):
	lista.append(line.split(' '))
	#Aqui tenemos todo el txt en la lista
f.close()

#Recorremos la lista una primera vez
for palabra in range(len(lista)-1):  
  #asignamos el ultimo caracter de la primera palabra de lista[palabra]
	ultimoCaracter = lista[palabra][len(lista[palabra])-1] #Obtenemos el ultimo caracter
	recorre = palabra + 1
	contador += 1
	lista_res1.append(lista[palabra])
	for recorre in range(len(lista)-recorre):
		if ultimoCaracter == lista[recorre][0]:
			contador += 1
			ultimoCaracter = lista[recorre][len(lista[recorre])-1]
			lista_res1.append(lista[recorre])       
	if contador > contador_viejo:
		lista_resultado = lista_res1[:] 
		contador_viejo = contador
	del lista_res1[:]
	contador = 0
print "La lista es: \n",lista_resultado,"con el valor de palabras concatenadas de: ", contador_viejo
