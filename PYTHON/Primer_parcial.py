import psycopg2 as p
import math as m

flag = True

PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "201801580"
PSQL_DB   = "williamhernandez"

address = """ host=%s port=%s user=%s password=%s dbname=%s 
"""% (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)

try:

	connection = p.connect(address)
	cursor = connection.cursor()
	
	print("¡LA CONEXIÓN CON LA BASE DE DATOS FUE EXITOSA!")
	

except:

	print("#¡NO SE LOGRÓ HACER LA CONEXIÓN CON LA BASE DATOS, INTENTELO NUEVAMENTE!#")


while flag == True:

	try:

		archivo = open("201801580.txt","a")
		print("")
		print("¡LA CONEXIÓN CON EL .TXT FUE EXITOSA!")

	except:

		print("####################################################################################")
		print("#         ¡NO SE LOGRÓ HACER LA CONEXIÓN CON EL .TXT, INTENTELO NUEVAMENTE!        #")
		print("####################################################################################")


	print("")
	print("                                      PROGRAMAS                                     ")
	print("")
	print("####################################################################################")
	print("#  1. ALTURA Y PESO PROMEDIO ------------------------------------------------ (a)  #")
	print("#  2. DIFETRENCIA ENTRE LA SUMA DE LOS CUADRADOS Y EL CUADRADO DE LA SUMA --- (b)  #")
	print("#  3. FACTOR PRIMO MÁS GRANDE  ---------------------------------------------- (c)  #")
	print("#  4. FUNCIÓN DE SUCESIÓN DEL NÚMERO DE FIBONACCI --------------------------- (d)  #")
	print("#  5. CALCULOS DE UN CONO --------------------------------------------------- (e)  #")
	print("#  6. SALIR ----------------------------------------------------------------- (s)  #")
	print("####################################################################################")
	print("")

	opcion = input("ELIJA UNA OPCIÓN: ")
	opt = opcion.lower()
	print("")
	        		

	if opt == "b":

		print("##################################################################################################")
		print("# USTED SELECCIONÓ LA OPCIÓN DIFETRENCIA ENTRE LA SUMA DE LOS CUADRADOS Y EL CUADRADO DE LA SUMA #")
		print("##################################################################################################")
		print("")
		
		try:
			n = int(input("INGRESE UN NÚMERO N: "))
			sc = 0
			cs = 0

			if n < 0:
				n="Error"
			else:
				n = n

			for i in range (1,n+1):

				sc = sc + pow(i, 2) 
				cs = cs + i

			cds = pow(cs, 2)

			total = cds - sc

			print("LA SUMA DE LOS CUADRADOS ES: ",sc)
			print("")
			print("EL CUADRADO DE LA SUMA ES: ", cds)
			print("")
			print("LA DIFERENCIA ENTRE LA SUMA DE LOS CUADRADDOS Y EL CUADRADO DE LA SUMA ES: ", total)

			SQL = "INSERT INTO programa2(numero_n,suma_de_cuadrados,cuadrado_de_la_suma,diferencia) VALUES ('%s','%s','%s','%s')"
			datos = (n,sc,cds,total)
			cursor.execute(SQL,datos)
			connection.commit()

			archivo.write('###########################################################################################\n')
			archivo.write('# SALIDA DEL PROGRAMA DIFETRENCIA ENTRE LA SUMA DE LOS CUADRADOS Y EL CUADRADO DE LA SUMA #\n')
			archivo.write('###########################################################################################\n')
			archivo.write('\n')
			archivo.write('PARA EL NUMERO %s LA DIFERENCIA ENTRE LA SUMA DE LOS CUADRADOS Y EL CUADRADO DE LA SUMA ES: %s \n'%(n,total))
			archivo.write('\n')
			archivo.close()

		except:

			print("")
			print("##############################################")
			print("# USTED NO INGRESÓ UN NUMERO ENTERO POSITIVO #")
			print("##############################################")

	elif opt == "c":

		print("######################################################")
		print("# USTED SELECCIONÓ LA OPCIÓN FACTOR PRIMO MÁS GRANDE #")
		print("######################################################")
		print("")

		try:

			n1 = int(input("INGRESE UN NÚMERO N: "))
			primos = []
			divisores = []

			if n1 < 0:
				n1 = "error"
			else:
				n1 = n1

			for i in range (1,n1+1):
					
				if n1%i == 0:
					divisores.append(i)
				else:
					i = i

			def primo(num):
				for n in range(2, num):
					if num % n == 0:
						return False
				primos.append(num)
				return True
			
			for i in range(0, len(divisores)):

				primo(divisores[i])

			lon = len(primos) - 1
			mayor = primos[lon]
			print("EL FACTOR PRIMO MÁS GRANDE ES: ", mayor)

			SQL = "INSERT INTO programa3(numero_n,divisores,divisores_primos,mayor_factor_primo) VALUES ('%s',"'%s'","'%s'",'%s')"
			datos = (n1,divisores,primos,mayor)
			cursor.execute(SQL,datos)
			connection.commit()

			archivo.write('###############################################\n')
			archivo.write('# SALIDA DEL PROGRAMA FACTOR PRIMO MÁS GRANDE #\n')
			archivo.write('###############################################\n')
			archivo.write('\n')
			archivo.write('PARA EL NUMERO %s EL FACTOR PRIMO MÁS GRANDE ES: %s \n'%(n1,mayor))
			archivo.write('\n')
			archivo.close()

		except:

			print("")
			print("##############################################")
			print("# USTED NO INGRESÓ UN NÚMERO ENTERO POSITIVO #")
			print("##############################################")

	elif opt == "d":

		print("###############################################################")
		print("# USTED SELECCIONÓ LA OPCIÓN SUCESIÓN DEL NÚMERO DE FIBONACCI #")
		print("###############################################################")
		print("")

		try:

			fib = []
			n2 = int(input("INGRESE UN NUMERO ENTERO POSITIVO: "))

			if n2 < 0:

				n2 = "Error"

			else:

				n2 = n2 

			def fibonacci(num):
				a,b = 0,1
				for i in range(num):
					fib.append(a)
					a,b = b, a+b

			fibonacci(n2)
			print("LA SUCESIÓN DE FIBONACCI PARA EL NUMERO", n2," ESTA DADA DE LA SIGUIENTE MANERA: ", fib)

			SQL = "INSERT INTO programa4(numero_n,sucesion) VALUES ('%s',"'%s'")"
			datos = (n2,fib)
			cursor.execute(SQL,datos)
			connection.commit()

			archivo.write('########################################################\n')
			archivo.write('# SALIDA DEL PROGRAMA SUCESIÓN DEL NÚMERO DE FIBONACCI #\n')
			archivo.write('########################################################\n')
			archivo.write('\n')
			archivo.write('LA SUCESIÓN DE FIBONACCI PARA EL NÚMERO %s ESTÁ DADA DE LA SIGUIENTE MANERA: %s \n'%(n2,fib))
			archivo.write('\n')
			archivo.close()

		except:

			print("")
			print("##############################################")
			print("# USTED NO INGRESÓ UN NÚMERO ENTERO POSITIVO #")
			print("##############################################")

	elif opt == "e":

		print("##################################################")
		print("# USTED SELECCIONÓ LA OPCIÓN CALCULOS DE UN CONO #")
		print("##################################################")
		print("")

		try:

			r = float(input("INGRESE EL RADIO DEL CONO: "))
			g = float(input("INGRESE LA GENERATRIZ DEL CONO: "))
			h = float(input("INGRESE LA ALTURA DEL CONO: "))

			if r < 0 or g < 0 or h < 0:

				r = "error"

			else: 

				r = r

			ab = (m.pi)*pow(r, 2)
			al = (m.pi)*g*r
			vol = ((m.pi)*pow(r, 2)*h)/3

			print("EL CONO CON RADIO ",r,",ALTURA ",h," Y GENERATRIZ ",g," TIENE:")
			print("")
			print("AREA DE LA BASE = ",ab)
			print("AREA LATERAL = ",al)
			print("VOLUMEN = ",vol)

			SQL = "INSERT INTO programa5(radio,altura,generatriz,area_de_la_base,area_lateral,volumen) VALUES ('%s','%s','%s','%s','%s','%s')"
			datos = (r,h,g,ab,al,vol)
			cursor.execute(SQL,datos)
			connection.commit()

			archivo.write('###########################################\n')
			archivo.write('# SALIDA DEL PROGRAMA CALCULOS DE UN CONO #\n')
			archivo.write('###########################################\n')
			archivo.write('\n')
			archivo.write('EL CONO CON RADIO %s ,ALTURA %s Y GENERATRIZ %s TIENE: \n'%(r,h,g))
			archivo.write('\n')
			archivo.write('AREA DE LA BASE = %s \n'%ab)
			archivo.write('AREA LATERAL = %s \n'%al)
			archivo.write('VOLUMEN = %s \n'%vol)
			archivo.write('\n')
			archivo.close()

		except:

			print("")
			print("#######################################################")
			print("# ¡ERROR! LAS MEDIDAS NO PUEDEN SER NÚMEROS NEGATIVOS #")
			print("#######################################################")

	elif opt == "s":

		flag = False

	else:

		print("######################################")
		print("# USTED NO INGRESÓ UNA OPCIÓN VALIDA #")
		print("######################################")


cursor.close()
connection.close()
print("#####################################")
print("# GRACICAS POR UTILIZAR EL PROGRAMA #")
print("#####################################")