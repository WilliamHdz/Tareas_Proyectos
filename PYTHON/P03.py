flag = True

while flag == True:

	try:

		archivo = open("Salida_P03.txt","a")
		print("")
		print("##################################################################")
		print("# 1. MOSTRAR EL NÚMERO DE VOCALES QUE TIENE UNA PALABRA ---- (v) #")
		print("# 2. SALIR --------------------------------------------------(s) #")
		print("##################################################################")
		print("")

		opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
		print("")

		if opt == "v":

			palabra = input("INGRESE UNA PALABRA O FRASE: ")
			palabrita = palabra.lower()

			a = palabrita.count("a") + palabrita.count("á")
			e = palabrita.count("e") + palabrita.count("é")
			i = palabrita.count("i") + palabrita.count("í")
			o = palabrita.count("o") + palabrita.count("ó")
			u = palabrita.count("u") + palabrita.count("ú")

			print("LA PALABRA O FRASE",palabra," TIENE ",(a+e+i+o+u)," VOCALES.")
			archivo.write('LA PALABRA O FRASE '+palabra+' TIENE: %s'%(a+e+i+o+u)+' VOCALES.\n')
			archivo.close()

		elif opt == "s":

			flag = False

		else: 

			print("######################################")
			print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
			print("######################################")

	except:

		print("USTED NO INGRESÓ UNA PALABRA")

print("")
print("####################################")
print("# GRACIAS POR UTILIZAR EL PROGRAMA #")
print("####################################")