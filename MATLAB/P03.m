flag = 1;

while flag == 1
    
    fprintf('\n');
	fprintf('########################################################################\n');
	fprintf('# 1. MOSTRAR EL NÚMERO DE VOCALES QUE TIENE UNA PALABRA ---------- (v) #\n');
	fprintf('# 2. SALIR ------------------------------------------------------- (s) #\n');
	fprintf('########################################################################\n');
	fprintf('\n');

	opt = input('INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ','s');
	fprintf('\n');	                
    
    switch opt
        
        case 'v'
            
            palabra = input('INGRESE UNA PALABRA: ','s');
            fprintf('\n');
            contador = 0;
            
            for i = 1:(length(palabra))
                
                if palabra(i) == 'a' || palabra(i) == 'e' || palabra(i) == 'i' || palabra(i) == 'o' || palabra(i) == 'u'
                    contador = contador + 1;
                else
                    contador = contador;
                end
   
            end
            
            fprintf('LA PALABRA %s TIENE %g VOCALES.',palabra,contador);
        
        case 's'
            
            flag = 0;
        
        otherwise
            
            fprintf('######################################\n');
            fprintf('# USTED NO INGRESO UNA OPCIÓN VALIDA #\n');
            fprintf('######################################\n');
    end
    
    fprintf('\n');
    
end

fprintf('####################################\n');
fprintf('# GRACIAS POR UTILIZAR EL PROGRAMA #\n');
fprintf('####################################\n');