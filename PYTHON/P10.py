flag = True

while flag == True:

	archivo = open("Salida_P10.txt","a")
	print("")
	print("#####################################################################")
	print("# 1. MOSTRAR EL NÚMERO DE CADA VOCAl QUE TIENE UNA PALABRA ---- (v) #")
	print("# 2. SALIR ---------------------------------------------------- (s) #")
	print("#####################################################################")
	print("")

	opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
	print("")

	if opt == "v":

		palabra = input("INGRESE UNA PALABRA: ")
		palabrita = palabra.lower()

		a = palabrita.count("a")
		e = palabrita.count("e")
		i = palabrita.count("i")
		o = palabrita.count("o")
		u = palabrita.count("u")

		print("LA PALABRA ",palabra," TIENE ",a," VOCALES A.")
		print("LA PALABRA ",palabra," TIENE ",e," VOCALES E.")
		print("LA PALABRA ",palabra," TIENE ",i," VOCALES I.")
		print("LA PALABRA ",palabra," TIENE ",o," VOCALES O.")
		print("LA PALABRA ",palabra," TIENE ",u," VOCALES U.")

		archivo.write('LA PALABRA '+palabra+' TIENE %s'%a+' VOCALES A.\n')
		archivo.write('LA PALABRA '+palabra+' TIENE %s'%e+' VOCALES E.\n')
		archivo.write('LA PALABRA '+palabra+' TIENE %s'%i+' VOCALES I.\n')
		archivo.write('LA PALABRA '+palabra+' TIENE %s'%o+' VOCALES O.\n')
		archivo.write('LA PALABRA '+palabra+' TIENE %s'%u+' VOCALES U.\n')
		archivo.write('\n')
		archivo.close()

	elif opt == "s":

		flag = False

	else: 

		print("######################################")
		print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
		print("######################################")

print("")
print("####################################")
print("# GRACIAS POR UTILIZAR EL PROGRAMA #")
print("####################################")