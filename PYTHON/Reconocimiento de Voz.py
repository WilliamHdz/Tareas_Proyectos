import speech_recognition as s

flag = True

au = s.Recognizer()

while flag == True:

    print("###########################################################")
    print("#           APLICACIÓN DE RECONOCIMIENTO DE VOZ           #")
    print("#                                                         #")
    print("# 1. INICIAR CON EL RECONOCIMIENTO DE VOZ ----------- (V) #")
    print("# 2. SALIR ------------------------------------------ (S) $")
    print("###########################################################")

    opc = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
    opt = opc.lower()

    if opt == "v":

        with s.Microphone() as source:
            print("###########################")
            print("# PUEDE COMENZAR A HABLAR #")
            print("###########################  ")
            audio = au.listen(source)

            try:
                escucha = au.recognize_google(audio, language='es -GUA')
                print("LO QUE SE ESCUCHÓ FUE: {}".format(escucha))
            except:
                print("ERROR, NO SE PUDO PROCESAR")

    elif opt == "s":
        
        print("")
        print("#####################################")
        print("# GRACICAS POR UTILIZAR EL PROGRAMA #")
        print("#####################################")
    
    else:

        print("")
        print("######################################")
        print("# USTED NO INGRESÓ UNA OPCIÓN VALIDA #")
        print("######################################")


