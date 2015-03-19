f = open("pokemon.txt") //Abrimos el archivo
lista = []              //lista donde volcamos el archivo txt
lista_res1 = []         //lista temporal donde guardamos el resultado de cadenas
lista_resultado = []    //lista final ganadora
contador_viejo = 0      //contador final ganador
contador = 0            //contador temporal


//Aqui tenemos todo el txt en la lista
for line in file("pokemon.txt"):
	lista.append(line.split(' '))



for fila in lista:  
	for palabra in lista:  
		ultimoCaracter = lista[fila][palabra][len(lista[fila][palabra])-1] //Ultimo caracter primera palabra
		//CUMPLE LA CONDICION
		if ultimoCaracter == lista[fila][palabra+1][0]:
			contador += 1
			ultimoCaracter = lista[fila][palabra+1][len(lista[fila][palabra+1])-1]
			lista_res1.append(lista[fila][palabra])
		else:
			contador += 1
			lista_res1.append(lista[fila][palabra])
			if contador > contador_viejo:
				lista_resultado = lista_res1[:]
				contador_viejo = contador
			del lista_res1
			contador = 0

print "La lista es: \n",lista_resultado,"con el valor de palabras concatenadas de: ", contador_viejo	
f.close()
