flag = 1;
num = 0;

while flag == 1

    try
        
    archivo = fopen('M_registro.txt','at');
    
    fprintf('\n');
	fprintf('       CALCULADORA DE FACTORIAL       \n');
	fprintf('\n');
	fprintf('######################################\n');
	fprintf('# 1. CALCULAR EL FACTORIAL ----- (f) #\n');
	fprintf('# 2. SALIR ----------------------(s) #\n'); 
	fprintf('######################################\n');
    
    fprintf('\n');
    opt = input('ELIJA UNA OPCIÓN: ','s');
    fprintf('\n');
    fact = 1;
    
    switch opt
        
        case 'f'
            
            num = input('INGRESE UN NUMERO ENTERO POSITIVO: ');
            
            if num == 0
                fact = 1;
                fprintf('EL FACTORIAL DE %g ES: %g \n', num, fact);
                fprintf(archivo, 'EL FACTORIAL DE %g ES: %g\n',num, fact);
                fclose(archivo);
                
            else
                
            if num > 0
                 
                for i = 1:num
                fact = fact*i;
                end
                
                fprintf('EL FACTORIAL DE %g ES: %g \n', num, fact);
                fprintf(archivo, 'EL FACTORIAL DE %g ES: %g\n',num, fact);
                fclose(archivo);
      
            else
                
                opt = w;
                
            end                               
            end
            
        
        case 's'
            
            flag = 0;
        
        otherwise
            
            fprintf('######################################\n');
			fprintf('# USTED NO INGRESO UNA OPCIÓN VALIDA #\n');
			fprintf('######################################\n');
 
    end
    
    catch
        fprintf('\n');
        fprintf('######################################\n');
		fprintf('# ¡ERROR! INGRESE UN ENTERO POSITIVO #\n');
		fprintf('######################################\n');
    end
        
end

fprintf('####################################\n');
fprintf('# GRACIAS POR UTILIZAR EL PROGRAMA #\n');
fprintf('####################################\n');